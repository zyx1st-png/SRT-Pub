import argparse
import copy
import json
import math
import os
import numpy as np
import torch
import torch.nn as nn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold


torch.set_num_threads(1)

BASE_CONTEXTS = [(0,0),(1,0),(2,0),(0,1),(1,1)]
TARGET_CONTEXT = (2,1)
HIDDEN = 32
SEQ_LEN = 5
INPUT_DIM = 6
BASE_STEPS = 1200
BATCH = 128
TARGET_STEPS = 80
CHECKPOINTS = [0,5,10,20,40,60,80]
N_RANDOM = 8
SEEDS = list(range(12))


class SimpleRNN(nn.Module):
    def __init__(self, seed, hidden=HIDDEN):
        super().__init__()
        torch.manual_seed(seed)
        self.hidden = hidden
        self.w_in = nn.Linear(INPUT_DIM, hidden, bias=False)
        self.w_h = nn.Linear(hidden, hidden, bias=True)
        self.out = nn.Linear(hidden, 1)
        nn.init.xavier_uniform_(self.w_in.weight)
        nn.init.orthogonal_(self.w_h.weight, gain=0.8)
        nn.init.zeros_(self.w_h.bias)
        nn.init.xavier_uniform_(self.out.weight)
        nn.init.zeros_(self.out.bias)

    def forward(self, x, intervention=None, return_hidden=False):
        h = torch.zeros(x.shape[0], self.hidden, dtype=x.dtype)
        hidden_seq = []
        for t in range(x.shape[1]):
            h = torch.tanh(self.w_in(x[:,t]) + self.w_h(h))
            if intervention is not None and t >= 1:
                h = intervention(h, t)
            hidden_seq.append(h)
        logit = self.out(h).squeeze(-1)
        if return_hidden:
            return logit, torch.stack(hidden_seq, dim=1)
        return logit


def make_batch(contexts, n, rng):
    cidx = rng.integers(0, len(contexts), size=n)
    bits = rng.integers(0, 2, size=(n,3), dtype=np.int64)
    x = np.zeros((n, SEQ_LEN, INPUT_DIM), dtype=np.float32)
    ctx = np.asarray(contexts, dtype=np.int64)[cidx]
    feat = ctx[:,0]
    inv = ctx[:,1]
    rows = np.arange(n)
    x[rows,0,feat] = 1.0
    x[rows,1,3+inv] = 1.0
    x[:,2:,5] = bits
    val = bits[rows,feat]
    y = np.where(inv == 1, 1 - val, val).astype(np.float32)
    labels = cidx.astype(np.int64)
    return torch.from_numpy(x), torch.from_numpy(y), labels


def make_balanced_base(n_per_context, rng):
    xs=[]; ys=[]; labs=[]
    for ci,c in enumerate(BASE_CONTEXTS):
        x,y,_ = make_batch([c], n_per_context, rng)
        xs.append(x); ys.append(y); labs.append(np.full(n_per_context,ci,dtype=np.int64))
    x=torch.cat(xs); y=torch.cat(ys); lab=np.concatenate(labs)
    perm=rng.permutation(len(lab))
    return x[perm], y[perm], lab[perm]


def accuracy(model, x, y, intervention=None):
    model.eval()
    with torch.no_grad():
        logits=model(x, intervention=intervention)
        pred=(torch.sigmoid(logits)>=0.5).float()
        return float((pred==y).float().mean().item())


def train_base(history, seed):
    model=SimpleRNN(seed)
    opt=torch.optim.Adam(model.parameters(), lr=0.01)
    lossfn=nn.BCEWithLogitsLoss()
    rng=np.random.default_rng(100000 + seed + (0 if history=='S' else 50000))
    schedule=[]
    if history=='S':
        schedule=[([(0,0),(1,0),(2,0)],300), ([(0,1),(1,1)],300), (BASE_CONTEXTS,600)]
    else:
        schedule=[(BASE_CONTEXTS,1200)]
    model.train()
    for contexts,steps in schedule:
        for _ in range(steps):
            x,y,_=make_batch(contexts,BATCH,rng)
            opt.zero_grad(set_to_none=True)
            loss=lossfn(model(x),y)
            loss.backward()
            opt.step()
    return model


def identify_O(model, seed):
    rng=np.random.default_rng(200000+seed)
    x,y,labels=make_balanced_base(300,rng)
    model.eval()
    with torch.no_grad():
        _,hs=model(x,return_hidden=True)
    X=hs[:,-1].numpy()
    skf=StratifiedKFold(n_splits=4,shuffle=True,random_state=300000+seed)
    scores={k:[] for k in [1,2,3,4]}
    for tr,te in skf.split(X,labels):
        dec=LogisticRegression(max_iter=1000,solver='lbfgs')
        dec.fit(X[tr],labels[tr])
        coef=dec.coef_ - dec.coef_.mean(axis=0,keepdims=True)
        _,_,vt=np.linalg.svd(coef,full_matrices=False)
        basis4=vt[:4].T
        for k in [1,2,3,4]:
            B=basis4[:,:k]
            ztr=X[tr]@B; zte=X[te]@B
            d2=LogisticRegression(max_iter=1000,solver='lbfgs')
            d2.fit(ztr,labels[tr])
            scores[k].append(d2.score(zte,labels[te]))
    A={k:float(np.mean(v)) for k,v in scores.items()}
    ref=A[4]
    kstar=next(k for k in [1,2,3,4] if A[k]>=0.90*ref)
    dec=LogisticRegression(max_iter=1000,solver='lbfgs')
    dec.fit(X,labels)
    coef=dec.coef_ - dec.coef_.mean(axis=0,keepdims=True)
    _,_,vt=np.linalg.svd(coef,full_matrices=False)
    basis=torch.tensor(vt[:kstar].T,dtype=torch.float32)
    admitted=A[kstar]>=0.80
    return A,kstar,basis,admitted,(x,y)


def projection_intervention(basis):
    def fn(h,t):
        return h - (h@basis)@basis.T
    return fn


def random_basis(hidden,k,rng):
    a=rng.normal(size=(hidden,k))
    q,_=np.linalg.qr(a)
    return torch.tensor(q[:,:k],dtype=torch.float32)


def calibrate_noise(model,basis,base_xy,seed):
    x,_=base_xy
    model.eval()
    norms=[]
    with torch.no_grad():
        h=torch.zeros(x.shape[0],HIDDEN)
        for t in range(x.shape[1]):
            h=torch.tanh(model.w_in(x[:,t])+model.w_h(h))
            if t>=1:
                disp=(h@basis)@basis.T
                norms.append(torch.linalg.norm(disp,dim=1).numpy())
    target=float(np.mean(np.concatenate(norms)))
    sigma=target/math.sqrt(HIDDEN)
    rng=np.random.default_rng(400000+seed)
    sample=rng.normal(scale=sigma,size=(20000,HIDDEN))
    actual=float(np.linalg.norm(sample,axis=1).mean())
    if actual>0:
        sigma*=target/actual
    sample=rng.normal(scale=sigma,size=(20000,HIDDEN))
    actual2=float(np.linalg.norm(sample,axis=1).mean())
    valid=(target==0 and actual2==0) or (target>0 and abs(actual2-target)/target<=0.10)
    return sigma,target,actual2,valid


class NoiseIntervention:
    def __init__(self,sigma,seed):
        self.sigma=sigma
        self.gen=torch.Generator().manual_seed(seed)
    def __call__(self,h,t):
        return h + torch.randn(h.shape,generator=self.gen,dtype=h.dtype)*self.sigma


def target_batches(seed):
    rng=np.random.default_rng(500000+seed)
    batches=[]
    for _ in range(TARGET_STEPS):
        x,y,_=make_batch([TARGET_CONTEXT],BATCH,rng)
        batches.append((x,y))
    erng=np.random.default_rng(600000+seed)
    ex,ey,_=make_batch([TARGET_CONTEXT],1024,erng)
    return batches,(ex,ey)


def run_arm(base_model, intervention_factory, batches, eval_xy, arm_seed):
    model=copy.deepcopy(base_model)
    opt=torch.optim.Adam(model.parameters(),lr=0.005)
    lossfn=nn.BCEWithLogitsLoss()
    checkpoints={}
    def eval_now(step):
        intervention=intervention_factory(step, True) if intervention_factory else None
        checkpoints[step]=accuracy(model,eval_xy[0],eval_xy[1],intervention)
    eval_now(0)
    for step,(x,y) in enumerate(batches, start=1):
        model.train(); opt.zero_grad(set_to_none=True)
        intervention=intervention_factory(step, False) if intervention_factory else None
        loss=lossfn(model(x,intervention=intervention),y)
        loss.backward(); opt.step()
        if step in CHECKPOINTS:
            eval_now(step)
    vals=[checkpoints[s] for s in CHECKPOINTS]
    auc=float(np.trapezoid(vals,x=CHECKPOINTS)/80.0)
    return auc,{str(s):checkpoints[s] for s in CHECKPOINTS}


def fixed_projection_factory(basis):
    fn=projection_intervention(basis)
    return lambda step,is_eval: fn


def noise_factory(sigma,seedbase):
    return lambda step,is_eval: NoiseIntervention(sigma, seedbase + step*17 + (1 if is_eval else 0))


def base_intervention_accuracy(model,base_xy,basis,sigma,seed):
    x,y=base_xy
    io=accuracy(model,x,y,projection_intervention(basis))
    noise=accuracy(model,x,y,NoiseIntervention(sigma,700000+seed))
    return io,noise


def updates_to_85(curve):
    for s in CHECKPOINTS:
        if curve[str(s)]>=0.85:
            return s
    return 81


def bootstrap_ci(arr,seed=20260920,n=10000):
    arr=np.asarray(arr,dtype=float)
    rng=np.random.default_rng(seed)
    means=np.empty(n)
    m=len(arr)
    for i in range(n):
        means[i]=arr[rng.integers(0,m,size=m)].mean()
    return [float(np.quantile(means,0.025)),float(np.quantile(means,0.975))]


def main(out_path):
    results=[]
    for history in ['S','D']:
        for seed in SEEDS:
            model=train_base(history,seed)
            brng=np.random.default_rng(800000+seed+(0 if history=='S' else 10000))
            bx,by,_=make_batch(BASE_CONTEXTS,2048,brng)
            base_acc=accuracy(model,bx,by)
            row={'history':history,'seed':seed,'base_accuracy':base_acc,'base_eligible':base_acc>=0.95}
            if not row['base_eligible']:
                results.append(row); continue
            A,k,basis,admitted,base_xy=identify_O(model,seed+(0 if history=='S' else 1000))
            row.update({'context_cv':{str(kk):vv for kk,vv in A.items()},'kstar':k,'O_admitted':admitted})
            if not admitted:
                results.append(row); continue
            sigma,target_disp,noise_disp,noise_valid=calibrate_noise(model,basis,base_xy,seed+(0 if history=='S' else 1000))
            row.update({'noise_sigma':sigma,'target_disp':target_disp,'noise_disp':noise_disp,'noise_valid':noise_valid})
            batches,eval_xy=target_batches(seed)
            auc0,curve0=run_arm(model,None,batches,eval_xy,seed)
            auco,curveo=run_arm(model,fixed_projection_factory(basis),batches,eval_xy,seed)
            aucn,curven=run_arm(model,noise_factory(sigma,900000+seed),batches,eval_xy,seed) if noise_valid else (None,None)
            rng=np.random.default_rng(1000000+seed+(0 if history=='S' else 10000))
            raucs=[]; rcurves=[]
            for ri in range(N_RANDOM):
                rb=random_basis(HIDDEN,k,rng)
                a,c=run_arm(model,fixed_projection_factory(rb),batches,eval_xy,seed+ri)
                raucs.append(a); rcurves.append(c)
            delta_o=auc0-auco
            delta_r=auc0-float(np.mean(raucs))
            delta_n=(auc0-aucn) if aucn is not None else None
            row.update({
                'auc_intact':auc0,'auc_O':auco,'auc_N':aucn,'auc_random':raucs,
                'curve_intact':curve0,'curve_O':curveo,'curve_N':curven,'curve_random':rcurves,
                'delta_O':delta_o,'delta_R':delta_r,'delta_N':delta_n,
                'C_R':delta_o-delta_r,'C_N':(delta_o-delta_n) if delta_n is not None else None,
                'zero_shot_intact':curve0['0'],'zero_shot_O':curveo['0'],'zero_shot_N':curven['0'] if curven else None,
                'updates85_intact':updates_to_85(curve0),'updates85_O':updates_to_85(curveo),'updates85_N':updates_to_85(curven) if curven else None,
            })
            io_base,in_base=base_intervention_accuracy(model,base_xy,basis,sigma,seed)
            row['base_acc_O']=io_base; row['base_acc_N']=in_base
            results.append(row)
            print(history,seed,'base',round(base_acc,3),'k',k,'A',round(A[k],3),'auc',round(auc0,3),round(auco,3),round(float(np.mean(raucs)),3),round(aucn,3) if aucn else None,flush=True)

    eligible=[r for r in results if r.get('base_eligible') and r.get('O_admitted') and r.get('noise_valid')]
    eS=sum(r['history']=='S' for r in eligible); eD=sum(r['history']=='D' for r in eligible)
    cr=np.array([r['C_R'] for r in eligible],dtype=float) if eligible else np.array([])
    cn=np.array([r['C_N'] for r in eligible],dtype=float) if eligible else np.array([])
    if len(eligible):
        ci_r=bootstrap_ci(cr,20260920); ci_n=bootstrap_ci(cn,20260921)
        med_r=float(np.median(cr)); med_n=float(np.median(cn))
        pass_flag=(eS>=8 and eD>=8 and med_r>=0.03 and med_n>=0.03 and ci_r[0]>0 and ci_n[0]>0)
        verdict='PILOT-PASS' if pass_flag else 'PILOT-NULL'
    else:
        ci_r=ci_n=[None,None]; med_r=med_n=None; verdict='PILOT-INVALID'
    if eS<8 or eD<8:
        verdict='PILOT-INVALID'
    summary={
        'verdict':verdict,'eligible_S':eS,'eligible_D':eD,'eligible_total':len(eligible),
        'median_C_R':med_r,'median_C_N':med_n,'mean_C_R':float(cr.mean()) if len(cr) else None,'mean_C_N':float(cn.mean()) if len(cn) else None,
        'bootstrap95_mean_C_R':ci_r,'bootstrap95_mean_C_N':ci_n,
        'mean_delta_O':float(np.mean([r['delta_O'] for r in eligible])) if eligible else None,
        'mean_delta_R':float(np.mean([r['delta_R'] for r in eligible])) if eligible else None,
        'mean_delta_N':float(np.mean([r['delta_N'] for r in eligible])) if eligible else None,
        'mean_auc_intact':float(np.mean([r['auc_intact'] for r in eligible])) if eligible else None,
        'mean_auc_O':float(np.mean([r['auc_O'] for r in eligible])) if eligible else None,
        'mean_auc_R':float(np.mean([np.mean(r['auc_random']) for r in eligible])) if eligible else None,
        'mean_auc_N':float(np.mean([r['auc_N'] for r in eligible])) if eligible else None,
    }
    payload={'summary':summary,'networks':results,'config':{
        'base_contexts':BASE_CONTEXTS,'target_context':TARGET_CONTEXT,'hidden':HIDDEN,'base_steps':BASE_STEPS,'target_steps':TARGET_STEPS,'checkpoints':CHECKPOINTS,'n_random':N_RANDOM,'seeds':SEEDS}}
    os.makedirs(os.path.dirname(out_path),exist_ok=True)
    with open(out_path,'w') as f: json.dump(payload,f,indent=2)
    print(json.dumps(summary,indent=2),flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--out',default='results.json'); args=ap.parse_args(); main(args.out)
