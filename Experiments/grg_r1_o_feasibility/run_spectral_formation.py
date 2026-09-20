import json
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import run_pilot

SEEDS=list(range(100,112))

def spectral_feature(model):
    W=model.w_h.weight.detach().cpu().numpy()
    vals=np.linalg.eigvals(W)
    vals=sorted(vals,key=lambda z:(-abs(z),-z.real,-abs(z.imag)))[:4]
    vals=np.asarray(vals)
    return np.concatenate([vals.real,np.abs(vals.imag),np.abs(vals)]).astype(float)

def paired_cv(X,y,groups):
    preds=np.empty(len(y),dtype=int)
    for g in sorted(set(groups)):
        te=np.array(groups)==g
        tr=~te
        clf=make_pipeline(StandardScaler(),LogisticRegression(max_iter=2000,solver='lbfgs'))
        clf.fit(X[tr],y[tr])
        preds[te]=clf.predict(X[te])
    return float((preds==y).mean()),preds

def main(out):
    rows=[]
    for h in ['S','D']:
        for s in SEEDS:
            m=run_pilot.train_base(h,s)
            rng=np.random.default_rng(810000+s+(0 if h=='S' else 10000))
            x,y,_=run_pilot.make_batch(run_pilot.BASE_CONTEXTS,2048,rng)
            acc=run_pilot.accuracy(m,x,y)
            rows.append({'history':h,'seed':s,'base_accuracy':acc,'feature':spectral_feature(m).tolist()})
            print(h,s,acc,flush=True)
    eligible=[r for r in rows if r['base_accuracy']>=0.95]
    nS=sum(r['history']=='S' for r in eligible); nD=sum(r['history']=='D' for r in eligible)
    if nS<10 or nD<10:
        verdict='O1-SPECTRAL-INVALID'; obs=None; p=None; null=[]
    else:
        X=np.asarray([r['feature'] for r in eligible])
        y=np.asarray([1 if r['history']=='S' else 0 for r in eligible])
        groups=np.asarray([r['seed'] for r in eligible])
        obs,_=paired_cv(X,y,groups)
        rng=np.random.default_rng(20260920)
        null=[]
        for _ in range(1000):
            yp=y.copy()
            for g in sorted(set(groups)):
                if rng.random()<0.5:
                    idx=np.where(groups==g)[0]
                    yp[idx]=yp[idx][::-1]
            a,_=paired_cv(X,yp,groups)
            null.append(a)
        p=(1+sum(a>=obs for a in null))/1001
        verdict='O1-SPECTRAL-PASS' if (nS==12 and nD==12 and obs>=0.75 and p<=0.05) else 'O1-SPECTRAL-NULL'
    payload={'verdict':verdict,'eligible_S':nS,'eligible_D':nD,'observed_accuracy':obs,'permutation_p':p,'null_mean':float(np.mean(null)) if null else None,'rows':rows}
    with open(out,'w') as f: json.dump(payload,f,indent=2)
    print(json.dumps({k:v for k,v in payload.items() if k!='rows'},indent=2))

if __name__=='__main__':
    main('spectral_formation_result.json')
