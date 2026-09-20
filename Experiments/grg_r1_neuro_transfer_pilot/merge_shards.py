import argparse
import json
import numpy as np

def bootstrap_ci(arr,seed,n=10000):
    arr=np.asarray(arr,dtype=float)
    rng=np.random.default_rng(seed)
    means=np.empty(n)
    m=len(arr)
    for i in range(n):
        means[i]=arr[rng.integers(0,m,size=m)].mean()
    return [float(np.quantile(means,0.025)),float(np.quantile(means,0.975))]

def main(paths,out):
    networks=[]
    configs=[]
    for p in paths:
        with open(p) as f:
            d=json.load(f)
        networks.extend(d["networks"])
        configs.append(d.get("config",{}))
    keys={(r["history"],r["seed"]) for r in networks}
    expected={(h,s) for h in ["S","D"] for s in range(12)}
    if keys != expected or len(networks)!=24:
        raise SystemExit(f"incomplete/duplicate shards: got {len(networks)} rows and {len(keys)} unique keys")
    networks=sorted(networks,key=lambda r:(r["history"],r["seed"]))
    eligible=[r for r in networks if r.get("base_eligible") and r.get("O_admitted") and r.get("noise_valid")]
    eS=sum(r["history"]=="S" for r in eligible); eD=sum(r["history"]=="D" for r in eligible)
    cr=np.array([r["C_R"] for r in eligible],dtype=float) if eligible else np.array([])
    cn=np.array([r["C_N"] for r in eligible],dtype=float) if eligible else np.array([])
    if len(eligible):
        ci_r=bootstrap_ci(cr,20260920); ci_n=bootstrap_ci(cn,20260921)
        med_r=float(np.median(cr)); med_n=float(np.median(cn))
        passed=(eS>=8 and eD>=8 and med_r>=0.03 and med_n>=0.03 and ci_r[0]>0 and ci_n[0]>0)
        verdict="PILOT-PASS" if passed else "PILOT-NULL"
    else:
        ci_r=ci_n=[None,None]; med_r=med_n=None; verdict="PILOT-INVALID"
    if eS<8 or eD<8:
        verdict="PILOT-INVALID"
    summary={
      "verdict":verdict,"eligible_S":eS,"eligible_D":eD,"eligible_total":len(eligible),
      "median_C_R":med_r,"median_C_N":med_n,
      "mean_C_R":float(cr.mean()) if len(cr) else None,
      "mean_C_N":float(cn.mean()) if len(cn) else None,
      "bootstrap95_mean_C_R":ci_r,"bootstrap95_mean_C_N":ci_n,
      "mean_delta_O":float(np.mean([r["delta_O"] for r in eligible])) if eligible else None,
      "mean_delta_R":float(np.mean([r["delta_R"] for r in eligible])) if eligible else None,
      "mean_delta_N":float(np.mean([r["delta_N"] for r in eligible])) if eligible else None,
      "mean_auc_intact":float(np.mean([r["auc_intact"] for r in eligible])) if eligible else None,
      "mean_auc_O":float(np.mean([r["auc_O"] for r in eligible])) if eligible else None,
      "mean_auc_R":float(np.mean([np.mean(r["auc_random"]) for r in eligible])) if eligible else None,
      "mean_auc_N":float(np.mean([r["auc_N"] for r in eligible])) if eligible else None,
    }
    payload={"summary":summary,"networks":networks,"config":configs[0] if configs else {},"execution":{"sharded":True,"shards":paths}}
    with open(out,"w") as f: json.dump(payload,f,indent=2)
    print(json.dumps(summary,indent=2))

if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--out",required=True); ap.add_argument("paths",nargs="+"); a=ap.parse_args(); main(a.paths,a.out)
