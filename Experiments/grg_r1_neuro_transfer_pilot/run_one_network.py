import argparse
import json
import numpy as np
import run_pilot

def run_one(history, seed, out):
    model=run_pilot.train_base(history,seed)
    brng=np.random.default_rng(800000+seed+(0 if history=='S' else 10000))
    bx,by,_=run_pilot.make_batch(run_pilot.BASE_CONTEXTS,2048,brng)
    base_acc=run_pilot.accuracy(model,bx,by)
    row={'history':history,'seed':seed,'base_accuracy':base_acc,'base_eligible':base_acc>=0.95}
    if row['base_eligible']:
        A,k,basis,admitted,base_xy=run_pilot.identify_O(model,seed+(0 if history=='S' else 1000))
        row.update({'context_cv':{str(kk):vv for kk,vv in A.items()},'kstar':k,'O_admitted':admitted})
        if admitted:
            sigma,target_disp,noise_disp,noise_valid=run_pilot.calibrate_noise(model,basis,base_xy,seed+(0 if history=='S' else 1000))
            row.update({'noise_sigma':sigma,'target_disp':target_disp,'noise_disp':noise_disp,'noise_valid':noise_valid})
            if noise_valid:
                batches,eval_xy=run_pilot.target_batches(seed)
                auc0,curve0=run_pilot.run_arm(model,None,batches,eval_xy,seed)
                auco,curveo=run_pilot.run_arm(model,run_pilot.fixed_projection_factory(basis),batches,eval_xy,seed)
                aucn,curven=run_pilot.run_arm(model,run_pilot.noise_factory(sigma,900000+seed),batches,eval_xy,seed)
                rng=np.random.default_rng(1000000+seed+(0 if history=='S' else 10000))
                raucs=[]; rcurves=[]
                for ri in range(run_pilot.N_RANDOM):
                    rb=run_pilot.random_basis(run_pilot.HIDDEN,k,rng)
                    a,c=run_pilot.run_arm(model,run_pilot.fixed_projection_factory(rb),batches,eval_xy,seed+ri)
                    raucs.append(a); rcurves.append(c)
                delta_o=auc0-auco
                delta_r=auc0-float(np.mean(raucs))
                delta_n=auc0-aucn
                row.update({
                    'auc_intact':auc0,'auc_O':auco,'auc_N':aucn,'auc_random':raucs,
                    'curve_intact':curve0,'curve_O':curveo,'curve_N':curven,'curve_random':rcurves,
                    'delta_O':delta_o,'delta_R':delta_r,'delta_N':delta_n,
                    'C_R':delta_o-delta_r,'C_N':delta_o-delta_n,
                    'zero_shot_intact':curve0['0'],'zero_shot_O':curveo['0'],'zero_shot_N':curven['0'],
                    'updates85_intact':run_pilot.updates_to_85(curve0),
                    'updates85_O':run_pilot.updates_to_85(curveo),
                    'updates85_N':run_pilot.updates_to_85(curven),
                })
                io_base,in_base=run_pilot.base_intervention_accuracy(model,base_xy,basis,sigma,seed)
                row['base_acc_O']=io_base; row['base_acc_N']=in_base
    with open(out,'w') as f:
        json.dump({'networks':[row],'config':{'seeds':[seed]}},f,indent=2)
    print(json.dumps(row,indent=2))

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--history',choices=['S','D'],required=True)
    ap.add_argument('--seed',type=int,required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    if a.seed not in range(12):
        raise SystemExit('seed must be preregistered 0..11')
    run_one(a.history,a.seed,a.out)
