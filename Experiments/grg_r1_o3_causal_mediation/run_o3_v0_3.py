import argparse
import copy
import json
import os
import sys
import numpy as np
import torch

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'grg_r1_neuro_transfer_pilot'))
import run_pilot

MU_S=np.array([6.236416260401408,5.4331406354904175,4.753790895144145,3.9411832094192505],dtype=float)
MU_D=np.array([4.691598852475484,3.5389750401178994,2.8467652002970376,2.503405749797821],dtype=float)
RECIPIENT_SEEDS=list(range(400,412))
RESET_UPDATES=[0,50,100,150,200,250,300]
CHECKPOINTS=[0,10,25,50,100,150,200,300,400,600,800,1200]

def top4(model):
    W=model.w_h.weight.detach().cpu().numpy()
    return np.linalg.svd(W,compute_uv=False)[:4].astype(float)

def set_top4(model,target):
    with torch.no_grad():
        W=model.w_h.weight.detach().cpu().numpy()
        U,s,Vh=np.linalg.svd(W,full_matrices=False)
        before=s[:4].copy()
        s2=s.copy(); s2[:4]=np.asarray(target,dtype=float)
        W2=(U*s2)@Vh
        fro=float(np.linalg.norm(W2-W))
        model.w_h.weight.copy_(torch.tensor(W2,dtype=model.w_h.weight.dtype))
    return before,np.asarray(target,dtype=float).copy(),fro

def balanced_eval(seed):
    rng=np.random.default_rng(710000+seed)
    x,y,_=run_pilot.make_balanced_base(500,rng)
    return x,y

def batches(seed):
    rng=np.random.default_rng(920000+seed)
    out=[]
    for _ in range(1200):
        x,y,_=run_pilot.make_batch(run_pilot.BASE_CONTEXTS,run_pilot.BATCH,rng)
        out.append((x,y))
    return out

def curve_auc(curve,max_update,center=False):
    xs=[u for u in CHECKPOINTS if u<=max_update]
    ys=np.array([curve[str(u)] for u in xs],dtype=float)
    if center:
        ys=ys-ys[0]
    return float(np.trapezoid(ys,x=xs)/max_update)

def first95(curve):
    for u in CHECKPOINTS:
        if curve[str(u)]>=0.95:
            return u
    return 1201

def bootstrap_ci(arr,seed,n=10000):
    arr=np.asarray(arr,dtype=float)
    rng=np.random.default_rng(seed)
    means=np.empty(n)
    for i in range(n):
        means[i]=arr[rng.integers(0,len(arr),size=len(arr))].mean()
    return [float(np.quantile(means,0.025)),float(np.quantile(means,0.975))]

def run_seed(seed):
    base=run_pilot.SimpleRNN(seed)
    arms={k:copy.deepcopy(base) for k in ['I','S','D']}
    opts={k:torch.optim.Adam(arms[k].parameters(),lr=0.01) for k in arms}
    lossfn=torch.nn.BCEWithLogitsLoss()
    bs=batches(seed)
    ex,ey=balanced_eval(seed)
    resets=[]

    def reset(update):
        sS=top4(arms['S'])
        dS=MU_S-sS
        L=float(np.linalg.norm(dS))
        bS,aS,fS=set_top4(arms['S'],MU_S)

        sD=top4(arms['D'])
        rawD=MU_D-sD
        nD=float(np.linalg.norm(rawD))
        if nD<=1e-12:
            if L>1e-12:
                raise RuntimeError('D direction undefined with nonzero S displacement')
            targetD=sD.copy()
        else:
            targetD=sD+(rawD/nD)*L
        if np.any(targetD<=0):
            raise RuntimeError('nonpositive D target singular value')
        bD,aD,fD=set_top4(arms['D'],targetD)
        resets.append({'update':update,'L':L,
                       'S_before':bS.tolist(),'S_after':aS.tolist(),'S_fro':fS,
                       'D_before':bD.tolist(),'D_after':aD.tolist(),'D_fro':fD,
                       'D_displacement':float(np.linalg.norm(aD-bD))})

    reset(0)
    curves={k:{'0':run_pilot.accuracy(m,ex,ey)} for k,m in arms.items()}

    for step,(x,y) in enumerate(bs,start=1):
        for k,m in arms.items():
            m.train(); opts[k].zero_grad(set_to_none=True)
            loss=lossfn(m(x),y); loss.backward(); opts[k].step()
        if step in RESET_UPDATES[1:]:
            reset(step)
        if step in CHECKPOINTS[1:]:
            for k,m in arms.items():
                curves[k][str(step)]=run_pilot.accuracy(m,ex,ey)

    metrics={}
    for k in arms:
        metrics[k]={
          'gain_auc_0_400':curve_auc(curves[k],400,True),
          'raw_auc_0_400':curve_auc(curves[k],400,False),
          'gain_auc_0_1200':curve_auc(curves[k],1200,True),
          'final_accuracy':curves[k]['1200'],
          'updates_to_95':first95(curves[k]),
          'curve':curves[k]
        }
    return {'seed':seed,'valid':True,'metrics':metrics,'resets':resets,
            'C_SD':metrics['S']['gain_auc_0_400']-metrics['D']['gain_auc_0_400'],
            'C_SI':metrics['S']['gain_auc_0_400']-metrics['I']['gain_auc_0_400']}

def main(out):
    rows=[]
    for seed in RECIPIENT_SEEDS:
        try:
            r=run_seed(seed)
        except Exception as e:
            r={'seed':seed,'valid':False,'error':repr(e)}
        rows.append(r)
        print(seed,r.get('valid'),r.get('C_SD'),r.get('C_SI'),flush=True)

    valid=[r for r in rows if r.get('valid')]
    if len(valid)<10:
        verdict='O3-INVALID'
        summary={'valid_recipients':len(valid)}
    else:
        csd=np.asarray([r['C_SD'] for r in valid])
        csi=np.asarray([r['C_SI'] for r in valid])
        ciSD=bootstrap_ci(csd,20260923)
        ciSI=bootstrap_ci(csi,20260924)
        medSD=float(np.median(csd)); medSI=float(np.median(csi))
        passed=(len(valid)==12 and medSD>=0.02 and medSI>=0.02 and ciSD[0]>0 and ciSI[0]>0)
        verdict='O3-CAUSAL-PASS' if passed else 'O3-CAUSAL-NULL'
        summary={
          'valid_recipients':len(valid),
          'median_C_SD':medSD,'median_C_SI':medSI,
          'mean_C_SD':float(csd.mean()),'mean_C_SI':float(csi.mean()),
          'bootstrap95_mean_C_SD':ciSD,'bootstrap95_mean_C_SI':ciSI,
          'mean_gain_auc_S':float(np.mean([r['metrics']['S']['gain_auc_0_400'] for r in valid])),
          'mean_gain_auc_D':float(np.mean([r['metrics']['D']['gain_auc_0_400'] for r in valid])),
          'mean_gain_auc_I':float(np.mean([r['metrics']['I']['gain_auc_0_400'] for r in valid])),
          'mean_update0_S':float(np.mean([r['metrics']['S']['curve']['0'] for r in valid])),
          'mean_update0_D':float(np.mean([r['metrics']['D']['curve']['0'] for r in valid])),
          'mean_update0_I':float(np.mean([r['metrics']['I']['curve']['0'] for r in valid]))
        }
    payload={'verdict':verdict,'summary':summary,'recipients':rows,
             'donor_admission':{'status':'PASS','paired_cv_accuracy':1.0,'permutation_p':0.001998001998001998,
                                'mu_S':MU_S.tolist(),'mu_D':MU_D.tolist()},
             'target_data_used':False,'protocol_version':'v0.3'}
    with open(out,'w') as f: json.dump(payload,f,indent=2)
    print(json.dumps({'verdict':verdict,'summary':summary},indent=2),flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--out',default='o3_v0_3_result.json')
    a=ap.parse_args(); main(a.out)
