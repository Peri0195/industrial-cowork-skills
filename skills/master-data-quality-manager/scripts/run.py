import argparse,json,math,statistics
from datetime import date,timedelta
from pathlib import Path
def require(ok,message):
    if not ok:raise ValueError(message)
def finite(v,key):
    require(type(v) in (int,float) and math.isfinite(v),key+': 必须为有限数字');return v
def nonneg(v,key):
    v=finite(v,key);require(v>=0,key+': 必须非负');return v
def positive(v,key):
    v=finite(v,key);require(v>0,key+': 必须大于0');return v
def num(d,k):return nonneg(d[k],k)
def pos(d,k):return positive(d[k],k)
def prob(v):
    v=finite(v,'概率');require(0<=v<=1,'概率须在0到1之间');return v
def frac(d,k,upper=True):
    v=prob(d[k]);require(upper or v<1,k+': 必须小于1');return v
def integer(d,k,positive=False):
    v=num(d,k);require(int(v)==v,k+': 必须为整数');require(not positive or v>0,k+': 必须大于0');return int(v)
def text(d,k):
    v=d[k];require(isinstance(v,str) and v.strip(),k+': 字符串不能为空');return v
def nums(d,k,minimum=1):
    v=d[k];require(isinstance(v,list) and len(v)>=minimum,k+': 数组过短');return [nonneg(x,k) for x in v]
def records(d,k):
    v=d[k];require(isinstance(v,list) and v and all(isinstance(x,dict) for x in v),k+': 需要非空对象数组');return v
def mapping(d,k):
    v=d[k];require(isinstance(v,dict) and v,k+': 需要非空对象');return v
def unique(rows,key):
    keys=[text(r,key) for r in rows];require(len(set(keys))==len(keys),key+': 标识不唯一')

def calculate(d):
    rows=records(d,'items');required=d['required'];units=d['allowed_units'];require(isinstance(required,list) and required and all(isinstance(k,str) and k for k in required),'必填字段列表无效');require(isinstance(units,list) and units,'单位词表为空');counts={};missing=[];bad=[]
    for i,r in enumerate(rows,1):
     key=r.get('sku');
     if key is not None and str(key).strip():counts[str(key)]=counts.get(str(key),0)+1
     for field in required:
      if r.get(field) is None or str(r[field]).strip()=='':missing.append({'row':i,'field':field})
     if r.get('unit') not in (None,'') and r['unit'] not in units:bad.append(i)
    return dict(duplicate_ids=sorted(k for k,v in counts.items() if v>1),missing_count=len(missing),invalid_unit_count=len(bad),missing=missing,invalid_unit_rows=bad)

def main():
    parser=argparse.ArgumentParser(description='离线计算入口，只读取指定JSON并写入结果目录')
    parser.add_argument('--input',required=True);parser.add_argument('--out',required=True);args=parser.parse_args()
    try:
        data=json.loads(Path(args.input).read_text(encoding='utf-8-sig'))
        require(isinstance(data,dict),'输入必须为JSON对象')
        result=calculate(data)
        encoded=json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)
    except (ValueError,KeyError,TypeError,OverflowError,ZeroDivisionError,OSError) as error:
        print(json.dumps({'status':'error','message':str(error)},ensure_ascii=False));return 2
    output=Path(args.out);output.mkdir(parents=True,exist_ok=True)
    (output/'report.json').write_text(encoded,encoding='utf8')
    (output/'report.md').write_text('# 计算结果\n\n```json\n'+encoded+'\n```\n',encoding='utf8')
    print(encoded);return 0
if __name__=='__main__':raise SystemExit(main())
