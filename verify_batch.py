"""Validate isolated skill archives, or rerun the actually installed MEA skills.
No installation, credentials, network calls, or edits to installed skills.
"""
from pathlib import Path
import argparse,json,subprocess,sys,tempfile,zipfile,hashlib,math
def check(actual,expected):
    if isinstance(expected,dict):
        for k,v in expected.items():check(actual[k],v)
    elif isinstance(expected,(bool,list)) or expected is None:
        assert actual==expected,(actual,expected)
    elif isinstance(expected,(int,float)):
        assert type(actual) in (int,float) and math.isclose(actual,expected,rel_tol=1e-8,abs_tol=1e-8),(actual,expected)
    else:assert actual==expected
def main():
    a=argparse.ArgumentParser();a.add_argument('--installed-root');a.add_argument('--out',required=True);args=a.parse_args()
    base=Path(__file__).resolve().parent;out=Path(args.out).resolve();out.mkdir(parents=True,exist_ok=True)
    catalog=json.loads((base/'catalog/batch-01.json').read_text(encoding='utf8'));results=[]
    for row in catalog:
        name=row['Skill英文原名'];record={'skill':name,'mode':'installed' if args.installed_root else 'archive','passed':False}
        try:
            with tempfile.TemporaryDirectory(prefix='mea-skill-test-') as tmp:
                if args.installed_root:
                    root=Path(args.installed_root)/name
                    assert (root/'SKILL.md').is_file(),'技能未安装'
                    reference=base/'skills'/name
                    for f in reference.rglob('*'):
                        if f.is_file() and '__pycache__' not in f.parts:
                            installed=root/f.relative_to(reference)
                            assert installed.is_file() and hashlib.sha256(installed.read_bytes()).digest()==hashlib.sha256(f.read_bytes()).digest(),'安装内容不一致: '+f.relative_to(reference).as_posix()
                else:
                    with zipfile.ZipFile(base/'downloads'/f'{name}.zip') as z:
                        assert z.testzip() is None,'压缩包损坏'
                        for item in z.infolist():
                            assert not item.filename.startswith(('/', '\\')) and '..' not in Path(item.filename).parts,'非法压缩路径'
                        z.extractall(tmp)
                    root=Path(tmp)/name
                casefile=root/'tests/cases.json'
                cases=json.loads(casefile.read_text(encoding='utf8')) if casefile.exists() else [{'id':'normal','input':row['sample'],'expected':row['expected'],'expected_exit_code':0}]
                record['cases']=[]
                for case in cases:
                    dest=out/name/case['id'];dest.mkdir(parents=True,exist_ok=True)
                    inputfile=dest/'input.json';inputfile.write_text(json.dumps(case['input'],ensure_ascii=False),encoding='utf8')
                    # Fresh output directory ensures an old report cannot pass a failed run.
                    with tempfile.TemporaryDirectory(prefix='result-') as resultdir:
                        run=subprocess.run([sys.executable,str(root/row['script']),'--input',str(inputfile),'--out',resultdir],capture_output=True,text=True,encoding='utf8',timeout=30)
                        (dest/'stdout.txt').write_text(run.stdout,encoding='utf8');(dest/'stderr.txt').write_text(run.stderr,encoding='utf8')
                        assert run.returncode==case['expected_exit_code'],f'exit={run.returncode}, expected={case["expected_exit_code"]}'
                        if run.returncode==0:
                            actual=json.loads((Path(resultdir)/'report.json').read_text(encoding='utf8'));check(actual,case['expected'])
                            for filename in ['report.json','report.md']:(dest/filename).write_bytes((Path(resultdir)/filename).read_bytes())
                        else:assert not (Path(resultdir)/'report.json').exists(),'失败用例生成了成功报告'
                    record['cases'].append({'id':case['id'],'exit_code':run.returncode,'passed':True})
                record['passed']=True
        except Exception as exc:record['error']=str(exc)
        results.append(record)
    result={'mode':'installed' if args.installed_root else 'archive','total':len(results),'passed':sum(r['passed'] for r in results),'results':results,'meaning':'installed模式验证实际安装文件及脚本；不能单凭此脚本证明模型自动路由/触发每项技能。archive模式只验证交付包。'}
    (out/'summary.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
    print(json.dumps({k:result[k] for k in ['mode','total','passed']},ensure_ascii=False));return 0 if result['passed']==result['total'] else 1
if __name__=='__main__':raise SystemExit(main())
