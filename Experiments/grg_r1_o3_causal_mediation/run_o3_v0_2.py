import argparse
import copy
import json
import os
import sys

import numpy as np
import torch
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'grg_r1_neuro_transfer_pilot'))
import run_pilot

DONOR_SEEDS=list(range(200,212))
RECIPIENT_SEEDS=list(range(300,312))
RESET_UPDATES=[0,50,100,150,200,250,300]
CHECKPOINTS=[0,10,25,50,100,150,200,300,400,600,800,1200]

def top4_singular(model):
    W=model.w_h.weight.detach().cpu().numpy()
    return np.linalg.svd(W,compute_uv=False)[:4].astype(float)

def paired_cv(X,y,groups):
    pred=np.empty(len(y),dtype=int)
    for g in sorted(set(groups)):
        te=(groups==g); tr=~te
        clf=make_pipeline(StandardScaler(),LogisticRegression(max_iter=2000,solver='lbfgs'))
        clf.fit(X[tr],y[tr])
        pred[te]=clf.predict(X[te])
    return float((pred==y).mean())

def donor_admission(rows):
    X=np.asarray([r['s4'] for r in rows],dtype=float)
    y=np.asarray([1 if r['history']=='S' else 0 for r in rows],dtype=int)
    groups=np.asarray([r['seed'] for r in rows],dtype=int)
    obs=paired_cv(X,y,groups)
    rng=np.random.default_rng(20260921)
    null=[]
    for _ in range(1000):
        yp=y.copy()
        for g in sorted(set(groups)):
            idx=np.where(groups==g)[0]
            if rng.random()<0.5:
                yp[idx]=yp[idx][::-1]
        null.append(paired_cv(X,yp,groups))
    p=(1+sum(v>=obs for v in null))/1001
    return obs,float(p),float(np.mean(null)),[float(np.quantile(null,0.025)),float(np.quantile(null,0.975))]

def set_top4_singular(model,target):
    with torch.no_grad():
        W=model.w_h.weight.detach().cpu().numpy()
        U,s,Vh=np.linalg.svd(W,full_matrices=False)
        before=s[:4].copy()
        s2=s.copy()
        s2[:4]=np.asarray(target,dtype=float)
        W2=(U*s2)@Vh
        fro=float(np.linalg.norm(W2-W))
        model.w_h.weight.copy_(torch.tensor(W2,dtype=model.w_h.weight.dtype))
    return before,np.asarray(target,dtype=float).copy(),fro

def random_target(current,dS,seed):
    L=float(np.linalg.norm(dS))
    if L<=1e-12:
        return current.copy(),np.zeros_like(current)
    rng=np.random.default_rng(seed)
    nd=float(np.linalg.norm(dS))
    for _ in range(1000):
        q=rng.normal(size=4)
        q=q/np.linalg.norm(q)
        cos=abs(float(np.dot(q,dS)/(nd+1e-12)))
        if cos>0.25:
            continue
        delta=q*L
        cand=current+delta
        if np.all(cand>1e-6):
            return cand,delta
    raise RuntimeError('no valid random spectral direction')

def balanced_eval(seed):
    rng=np.random.default_rng(700000+seed)
    x,y,_=run_pilot.make_balanced_base(500,rng)
    return x,y

def make_batches(seed):
    rng=np.random.default_rng(900000+seed)
    out=[]
    for _ in range(1200):
        x,y,_=run_pilot.make_batch(run_pilot.BASE_CONTEXTS,run_pilot.BATCH,rng)
        out.append((x,y))
    return out

def auc(curve,max_update):
    xs=[u for u in CHECKPOINTS if u<=max_update]
    ys=[curve[str(u)] for u in xs]
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

def train_donors():
    rows=[]
    for h in ['S','D']:
        for seed in DONOR_SEEDS:
            m=run_pilot.train_base(h,seed)
            rng=np.random.default_rng(820000+seed+(0 if h=='S' else 10000))
            x,y,_=run_pilot.make_batch(run_pilot.BASE_CONTEXTS,2048,rng)
            acc=run_pilot.accuracy(m,x,y)
            row={'history':h,'seed':seed,'base_accuracy':acc,'s4':top4_singular(m).tolist()}
            rows.append(row)
            print('donor',h,seed,round(acc,4),row['s4'],flush=True)
    return rows

def train_recipient(seed,muS):
    base=run_pilot.SimpleRNN(seed)
    arms={k:copy.deepcopy(base) for k in ['I','S','R']}
    opts={k:torch.optim.Adam(arms[k].parameters(),lr=0.01) for k in arms}
    lossfn=torch.nn.BCEWithLogitsLoss()
    batches=make_batches(seed)
    ex,ey=balanced_eval(seed)
    curves={k:{'0':run_pilot.accuracy(m,ex,ey)} for k,m in arms.items()}
    resets=[]

    def do_reset(update,idx):
        curS=top4_singular(arms['S'])
        dS=np.asarray(muS)-curS
        bS,aS,fS=set_top4_singular(arms['S'],muS)

        curR=top4_singular(arms['R'])
        targetR,deltaR=random_target(curR,dS,20260921+1000*seed+idx)
        bR,aR,fR=set_top4_singular(arms['R'],targetR)

        resets.append({
            'update':update,
            'requested_norm':float(np.linalg.norm(dS)),
            'random_delta_norm':float(np.linalg.norm(deltaR)),
            'S_before':bS.tolist(),'S_after':aS.tolist(),'S_fro_delta':fS,
            'R_before':bR.tolist(),'R_after':aR.tolist(),'R_fro_delta':fR
        })

    do_reset(0,0)

    for step,(x,y) in enumerate(batches,start=1):
        for k,m in arms.items():
            m.train()
            opts[k].zero_grad(set_to_none=True)
            loss=lossfn(m(x),y)
            loss.backward()
            opts[k].step()

        if step in RESET_UPDATES[1:]:
            do_reset(step,RESET_UPDATES.index(step))

        if step in CHECKPOINTS[1:]:
            for k,m in arms.items():
                curves[k][str(step)]=run_pilot.accuracy(m,ex,ey)

    metrics={}
    for k in arms:
        metrics[k]={
            'auc_0_400':auc(curves[k],400),
            'auc_0_1200':auc(curves[k],1200),
            'final_accuracy':curves[k]['1200'],
            'updates_to_95':first95(curves[k]),
            'curve':curves[k]
        }

    return {
        'seed':seed,'valid':True,'metrics':metrics,'resets':resets,
        'C_SR':metrics['S']['auc_0_400']-metrics['R']['auc_0_400'],
        'C_SI':metrics['S']['auc_0_400']-metrics['I']['auc_0_400']
    }

def main(out):
    donors=train_donors()
    competentS=sum(r['base_accuracy']>=0.95 for r in donors if r['history']=='S')
    competentD=sum(r['base_accuracy']>=0.95 for r in donors if r['history']=='D')
    obs,p,null_mean,null95=donor_admission(donors)
    admitted=(competentS==12 and competentD==12 and obs>=0.75 and p<=0.05)

    muS=np.mean([r['s4'] for r in donors if r['history']=='S'],axis=0)
    muD=np.mean([r['s4'] for r in donors if r['history']=='D'],axis=0)

    recipients=[]
    if admitted:
        for seed in RECIPIENT_SEEDS:
            try:
                row=train_recipient(seed,muS)
            except Exception as e:
                row={'seed':seed,'valid':False,'error':repr(e)}
            recipients.append(row)
            print('recipient',seed,row.get('C_SR'),row.get('C_SI'),row.get('valid'),flush=True)

    valid=[r for r in recipients if r.get('valid')]

    if not admitted:
        verdict='O3-SCAFFOLD-NOT-ADMITTED'
        summary={}
    elif len(valid)<10:
        verdict='O3-INVALID'
        summary={'valid_recipients':len(valid)}
    else:
        csr=np.asarray([r['C_SR'] for r in valid],dtype=float)
        csi=np.asarray([r['C_SI'] for r in valid],dtype=float)
        ciSR=bootstrap_ci(csr,20260921)
        ciSI=bootstrap_ci(csi,20260922)
        medSR=float(np.median(csr)); medSI=float(np.median(csi))
        passed=(len(valid)==12 and medSR>=0.02 and medSI>=0.02 and ciSR[0]>0 and ciSI[0]>0)
        verdict='O3-CAUSAL-PASS' if passed else 'O3-CAUSAL-NULL'
        summary={
            'valid_recipients':len(valid),
            'median_C_SR':medSR,'median_C_SI':medSI,
            'mean_C_SR':float(csr.mean()),'mean_C_SI':float(csi.mean()),
            'bootstrap95_mean_C_SR':ciSR,'bootstrap95_mean_C_SI':ciSI,
            'mean_auc_S':float(np.mean([r['metrics']['S']['auc_0_400'] for r in valid])),
            'mean_auc_R':float(np.mean([r['metrics']['R']['auc_0_400'] for r in valid])),
            'mean_auc_I':float(np.mean([r['metrics']['I']['auc_0_400'] for r in valid]))
        }

    payload={
        'verdict':verdict,
        'donor_admission':{
            'competent_S':competentS,'competent_D':competentD,
            'paired_cv_accuracy':obs,'permutation_p':p,
            'null_mean':null_mean,'null_95':null95,
            'mu_S':muS.tolist(),'mu_D':muD.tolist()
        },
        'summary':summary,
        'donors':donors,'recipients':recipients,
        'target_data_used':False,
        'protocol_version':'v0.2'
    }
    with open(out,'w') as f:
        json.dump(payload,f,indent=2)
    print(json.dumps({'verdict':verdict,'donor_admission':payload['donor_admission'],'summary':summary},indent=2),flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--out',default='o3_v0_2_result.json')
    a=ap.parse_args()
    main(a.out)
