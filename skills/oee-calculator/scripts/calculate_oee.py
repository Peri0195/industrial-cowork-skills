import argparse,json,math
from pathlib import Path
def calculate(data):
    required=['planned_minutes','run_minutes','ideal_cycle_minutes','total_count','good_count']
    for k in required:
        v=data.get(k)
        if isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v):
            raise ValueError(k+': 必须为有限数字')
        if v<0: raise ValueError(k+': 不得为负数')
    p,r,c,n,g=(data[k] for k in required)
    if p<=0 or c<=0: raise ValueError('计划时间与理想节拍必须大于0')
    if r>p: raise ValueError('运行时间超过计划时间')
    if int(n)!=n or int(g)!=g: raise ValueError('产量必须是整数')
    if g>n: raise ValueError('良品数超过总产量')
    if r==0 and n>0: raise ValueError('运行时间为0但有产量')
    if n*c>r+1e-9: raise ValueError('性能率超过100%，请复核单位、产量或理想节拍；不自动截断')
    a=r/p; perf=n*c/r if r else 0; q=g/n if n else 0
    return {'availability_pct':round(a*100,6),'performance_pct':round(perf*100,6),'quality_pct':round(q*100,6),'oee_pct':round(a*perf*q*100,6),'downtime_minutes':p-r,'reject_count':n-g,'warnings':['无产出，质量率和性能率按0计，不能据此评价工艺质量'] if n==0 else []}
def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--out',required=True);a=p.parse_args()
    try:
        data=json.loads(Path(a.input).read_text(encoding='utf-8-sig')); result=calculate(data)
    except (ValueError,OSError) as e:
        print(json.dumps({'error':str(e)},ensure_ascii=False));return 2
    out=Path(a.out);out.mkdir(parents=True,exist_ok=True)
    (out/'report.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
    report='# 设备综合效率结果\n\n'+'\n'.join(f'- {k}: {v}' for k,v in result.items())
    (out/'report.md').write_text(report,encoding='utf8');print(json.dumps(result,ensure_ascii=False));return 0
if __name__=='__main__':raise SystemExit(main())
