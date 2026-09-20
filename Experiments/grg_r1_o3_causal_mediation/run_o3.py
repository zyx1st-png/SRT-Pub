import argparse
import copy
import json
import numpy as np
import torch
import torch.nn as nn

from Experiments.grg_r1_neuro_transfer_pilot import run_pilot

DONOR_SEEDS=list(range(200,212))
RECIPIENT_SEEDS=list(range(300,312))
CHECKPOINTS=[0,5,10,20,40,80,160,320,600]
RECIPIENT_STEPS=600

def source_sorted_top4(model):
    W=model.w_h.weight.detach().cpu().numpy()
    vals=np.linalg.eigvals(W)
    vals=np.sort(vals)[::-1]
    return vals[:4]

def transplant(model, scaffold):
    m=copy.deepcopy(model)
    W=m.w_h.weight.detach().cpu().numpy()
    e,V=np.linalg.eig(W)
    en=e.copy()
    en[:4]=scaffold
    Wc=V @ np.diag(en) @ np.linalg.inv(V)
    imag_res=float(np.max(np.abs(np.imag(Wc))))
    Wnew=np.real(Wc).astype(np.float32)
    dist=float(np.linalg.norm(Wnew-W))
    rad0=float(np.max(np.abs(np.linalg.eigvals(W))))
    rad1=float(np.max(np.abs(np.linalg.eigvals(Wnew))))
    with torch.no_grad():
        m.w_h.weight.copy_(torch.from_numpy(Wnew))
    return m,{'fro_distance':dist,'spectral_radius_before':rad0,'spectral_radius_after':rad1,'imag_residual':imag_res}

def balanced_eval(seed):
    rng=np.random.default_rng(950000+seed)
    return run_pilot.make_balanced_base(410,rng)[:2]

def fixed_batches(seed):
    rng=np.random.default_rng(960000+seed)
    out=[]
    for _ in range(RECIPIENT_STEPS):
        x,y,_=run_pilot.make_batch(run_pilot.BASE_CONTEXTS,run_pilot.BATCH,rng)
        out.append((x,y))
    return out

def train_curve(model,batches,eval_xy):
    opt=torch.optim.Adam(model.parameters(),lr=0.01)
    lossfn=nn.BCEWithLogitsLoss()
    acc={0:run_pilot.accuracy(model,eval_xy[0],eval_xy[1])}
    losses=[]
    for step,(x,y) in enumerate(batches,start=1):
        model.train(); opt.zero_grad(set_to_none=True)
        logits=model(x)
        loss=lossfn(logits,y)
        losses.append(float(loss.detach().item()))
        loss.backward(); opt.step()
        if step in CHECKPOINTS:
            acc[step]=run_pilot.accuracy(model,eval_xy[0],eval_xy[1])
    vals=[acc[s] for s in CHECKPOINTS]
    auc=float(np.trapezoid(vals,x=CHECKPOINTS)/600.0)
    loss_auc=float(np.mean(losses))
    return auc,loss_auc,{str(s):acc[s] for s in CHECKPOINTS}

def updates95(curve):
    for s in CHECKPOINTS:
        if curve[str(s)]>=0.95:
            return s
    return 601

def bootstrap_ci(arr,seed,n=10000):
    arr=np.asarray(arr,dtype=float)
    rng=np.random.default_rng(seed)
    means=np.empty(n)
    for i in range(n):
        means[i]=arr[rng.integers(0,len(arr),size=len(arr))].mean()
    return [float(np.quantile(means,0.025)),float(np.quantile(means,0.975))]

def main(out):
    donors=[]
    tops={'S':[],'D':[]}
    for h in ['S','D']:
        for seed in DONOR_SEEDS:
            m=run_pilot.train_base(h,seed)
            rng=np.random.default_rng(940000+seed+(0 if h=='S' else 10000))
            x,y,_=run_pilot.make_batch(run_pilot.BASE_CONTEXTS,2048,rng)
            acc=run_pilot.accuracy(m,x,y)
            vals=source_sorted_top4(m)
            donors.append({'history':h,'seed':seed,'base_accuracy':acc,
                           'top4_real':[float(z.real) for z in vals],
                           'top4_imag':[float(z.imag) for z in vals]})
            tops[h].append(vals)
            print('donor',h,seed,acc,flush=True)
    scaffold_S=np.mean(np.stack(tops['S']),axis=0)
    scaffold_D=np.mean(np.stack(tops['D']),axis=0)
    recipients=[]
    for seed in RECIPIENT_SEEDS:
        base=run_pilot.SimpleRNN(seed)
        IS,metaS=transplant(base,scaffold_S)
        ID,metaD=transplant(base,scaffold_D)
        I0=copy.deepcopy(base)
        batches=fixed_batches(seed)
        eval_xy=balanced_eval(seed)
        auc0,loss0,c0=train_curve(I0,batches,eval_xy)
        aucS,lossS,cS=train_curve(IS,batches,eval_xy)
        aucD,lossD,cD=train_curve(ID,batches,eval_xy)
        row={'seed':seed,'auc_I0':auc0,'auc_IS':aucS,'auc_ID':aucD,
             'C_SD':aucS-aucD,'C_S0':aucS-auc0,
             'loss_I0':loss0,'loss_IS':lossS,'loss_ID':lossD,
             'curve_I0':c0,'curve_IS':cS,'curve_ID':cD,
             'updates95_I0':updates95(c0),'updates95_IS':updates95(cS),'updates95_ID':updates95(cD),
             'meta_IS':metaS,'meta_ID':metaD}
        recipients.append(row)
        print('recipient',seed,round(auc0,4),round(aucS,4),round(aucD,4),flush=True)
    donorS=sum(r['base_accuracy']>=0.95 for r in donors if r['history']=='S')
    donorD=sum(r['base_accuracy']>=0.95 for r in donors if r['history']=='D')
    csd=np.array([r['C_SD'] for r in recipients])
    cs0=np.array([r['C_S0'] for r in recipients])
    ciSD=bootstrap_ci(csd,20260921)
    ciS0=bootstrap_ci(cs0,20260922)
    medSD=float(np.median(csd)); medS0=float(np.median(cs0))
    invalid=(donorS<12 or donorD<12 or len(recipients)!=12 or
             any(not np.isfinite(r['meta_IS']['imag_residual']) for r in recipients))
    if invalid:
        verdict='O3-CAUSAL-INVALID'
    else:
        passed=(medSD>=0.03 and medS0>=0.03 and ciSD[0]>0 and ciS0[0]>0)
        verdict='O3-CAUSAL-PASS' if passed else 'O3-CAUSAL-NULL'
    summary={'verdict':verdict,'donor_S_eligible':donorS,'donor_D_eligible':donorD,
             'recipient_n':len(recipients),'median_C_SD':medSD,'median_C_S0':medS0,
             'mean_C_SD':float(csd.mean()),'mean_C_S0':float(cs0.mean()),
             'bootstrap95_mean_C_SD':ciSD,'bootstrap95_mean_C_S0':ciS0,
             'mean_auc_I0':float(np.mean([r['auc_I0'] for r in recipients])),
             'mean_auc_IS':float(np.mean([r['auc_IS'] for r in recipients])),
             'mean_auc_ID':float(np.mean([r['auc_ID'] for r in recipients])),
             'target_data_used':False}
    payload={'summary':summary,'scaffold_S_real':[float(z.real) for z in scaffold_S],
             'scaffold_S_imag':[float(z.imag) for z in scaffold_S],
             'scaffold_D_real':[float(z.real) for z in scaffold_D],
             'scaffold_D_imag':[float(z.imag) for z in scaffold_D],
             'donors':donors,'recipients':recipients}
    with open(out,'w') as f: json.dump(payload,f,indent=2)
    print(json.dumps(summary,indent=2))

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--out',default='o3_result.json')
    args=ap.parse_args()
    main(args.out)
