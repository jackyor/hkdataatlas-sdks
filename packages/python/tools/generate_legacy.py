"""Generate isolated native clients from exact canonical sources and equivalent inputs."""
from __future__ import annotations
import argparse,concurrent.futures,hashlib,importlib.metadata,json,os,re,shutil,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
PACKAGE=ROOT/'packages/python'
STATE=PACKAGE/'.generation'
MODULE=PACKAGE/'src/hkdataatlas'
METHODS={'get','put','post','delete','options','head','patch','trace'}
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(p,v):p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2)+'\n')
def snake(s):return re.sub(r'[^a-zA-Z0-9_]','_',s).lower()
def normalize(node,changes,path=''):
 if isinstance(node,dict):
  if 'const'in node and 'enum'not in node:
   value=node.pop('const');node['enum']=[value];changes.append({'pointer':path,'rule':'const_to_singleton_enum'})
  if (node.get('type')=='array' or isinstance(node.get('type'),list)and'array'in node['type'])and'items'not in node and'prefixItems'not in node:
   node['items']={};changes.append({'pointer':path,'rule':'explicit_unknown_array_items'})
  for k,v in node.items():normalize(v,changes,path+'/'+k.replace('~','~0').replace('/','~1'))
 elif isinstance(node,list):
  for i,v in enumerate(node):normalize(v,changes,path+'/'+str(i))
def tree(p):return {str(f.relative_to(p)):sha(f)for f in sorted(Path(p).rglob('*'))if f.is_file()and not any(x in f.parts for x in ['__pycache__','.ruff_cache'])and f.suffix!='.pyc'}
def operations(spec):return [{'method':method,'path':path,'operationId':op.get('operationId'),'tags':op.get('tags',[])}for path,item in spec['paths'].items()for method,op in item.items()if method in METHODS]
def generate_one(source,check):
 publisher=source['publisherKey'];family=snake(source['familyKey']);out=MODULE/snake(publisher)/family;state=STATE/(source['id']+'.json');canonical=ROOT/'specs'/source['json'];spec=json.loads(canonical.read_text());assert sha(canonical)==source['jsonSha256'];changes=[];normalize(spec,changes)
 inputs=STATE/'inputs'/publisher/(family+'.json');config_path=STATE/'configs'/(source['id']+'.json')
 reserved={'Response','Client','AuthenticatedClient','File','Unset','UNSET'};names=set(spec.get('components',{}).get('schemas',{}));overrides={}
 for name in sorted(names&reserved):
  chosen='Source'+name.title().replace('_','')+'Model'
  while chosen in names:chosen+='Model'
  names.add(chosen);overrides[name]={'class_name':chosen,'module_name':re.sub(r'(?<!^)(?=[A-Z])','_',chosen).lower()}
 config={'literal_enums':True,'package_name_override':family,'project_name_override':'hkdataatlas-'+source['id'],'class_overrides':overrides}
 key=hashlib.sha256(json.dumps({'source':sha(canonical),'spec':spec,'config':config,'generator':'0.30.0','builder':sha(__file__)},sort_keys=True).encode()).hexdigest()
 prior=json.loads(state.read_text())if state.exists()else None
 if prior and prior['key']==key and out.exists()and prior['outputs']==tree(out):return{**prior,'status':'reused'}
 if check:raise RuntimeError('Stale Python generation: '+source['id'])
 dump(inputs,spec);dump(config_path,config);out.parent.mkdir(parents=True,exist_ok=True)
 command=[str(Path(sys.executable).parent/'openapi-python-client'),'generate','--path',str(inputs),'--config',str(config_path),'--meta','none','--output-path',str(out),'--overwrite']
 run=subprocess.run(command,capture_output=True,text=True,env={**os.environ,'PATH':str(Path(sys.executable).parent)+os.pathsep+os.environ['PATH']})
 log=(run.stdout+run.stderr).replace(str(ROOT),'<repository>');logpath=ROOT/'reports/python-generation'/f'{source["id"]}.log';logpath.parent.mkdir(parents=True,exist_ok=True);logpath.write_text(log)
 row={'sourceId':source['id'],'publisherKey':publisher,'family':family,'status':'generated'if run.returncode==0 else'failed','key':key,'sourceSha256':source['jsonSha256'],'derivedInputSha256':sha(inputs),'normalizations':changes,'classOverrides':overrides,'operations':operations(spec),'warnings':'Warning(s)'in log,'log':'reports/python-generation/'+source['id']+'.log','outputs':tree(out)if out.exists()else{}}
 if run.returncode:row['error']=log
 dump(state,row);return row

def metadata(manifest,check):
 groups={}
 for source in manifest['sources']:groups.setdefault(source['publisherKey'],[]).append(source)
 def emit(path,value):
  text=json.dumps(value,indent=2)+'\n'if not isinstance(value,str)else value
  if check:
   if path.read_text()!=text:raise RuntimeError('Python metadata stale: '+str(path))
  else:path.parent.mkdir(parents=True,exist_ok=True);path.write_text(text)
 publishers=[]
 for key,sources in groups.items():
  data={'publisherKey':key,'publisherName':sources[0]['publisherName'],'sources':[{**{k:v for k,v in s.items()if k not in ['origin','originLabel','originCategory']},'moduleName':snake(s['familyKey'])}for s in sources]};publishers.append(data)
  emit(MODULE/snake(key)/'sources.json',data);emit(MODULE/snake(key)/'__init__.py','"""'+sources[0]['publisherName']+' native API client families."""\n')
 emit(MODULE/'sources.json',{'packageVersion':'0.0.1','publisherCount':len(groups),'apiFamilies':len(manifest['sources']),'generator':'openapi-python-client0.30.0','publishers':publishers,'limitations':['Client(base_url=...) is explicit; see source server metadata.','attrs parsing is not complete JSON Schema validation.','Canonical source contracts and origin/readiness metadata remain authoritative.']})
 emit(MODULE/'__init__.py','"""One SDK distribution, with native synchronous and asynchronous publisher clients."""\n__version__ = "0.0.1"\n')
 emit(PACKAGE/'pyproject.toml','''[build-system]
requires = ["hatchling==1.30.1"]
build-backend = "hatchling.build"

[project]
name = "hkdataatlas"
version = "0.0.1"
description = "Hong Kong public API clients grouped by publisher"
readme = "README.md"
license = "MIT"
license-files = ["LICENSE"]
requires-python = ">=3.11"
dependencies = ["httpx2==2.16.0", "attrs==26.1.0"]

[tool.hatch.build.targets.wheel]
packages = ["src/hkdataatlas"]
''')
 emit(PACKAGE/'README.md','''# HK Data Atlas Python SDK

One distribution, `hkdataatlas`, contains 25 publisher modules and 254 API families. Native clients are generated by openapi-python-client0.30.0. Each family exposes Client, AuthenticatedClient, typed endpoint functions and attrs models. The canonical specifications remain unchanged; equivalent generator-only inputs make constants and unknown array items explicit. Source provenance and readiness remain in sources.json.

```python
from hkdataatlas.censtatd.c_sd_web_table_api import Client
from hkdataatlas.censtatd.c_sd_web_table_api.api.statistical_tables import get_statistical_table

with Client(base_url="https://www.censtatd.gov.hk/api") as client:
    response = get_statistical_table.sync_detailed(client=client, id="110-01001", lang="en", full_series="1")
    print(response.status_code, response.parsed)
```

Each endpoint also provides `asyncio_detailed` for native asynchronous calls. Base URLs are explicitly caller-selected; source server metadata is retained in the specifications. Detailed calls preserve status, headers and content. Parsed attrs models do not replace full JSON Schema validation. Unknown response fields remain unknown. This package is provisional and unpublished. Previous Hey output remains preserved outside the default package as comparison material.
''')

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args();assert importlib.metadata.version('openapi-python-client')=='0.30.0'
 manifest=json.loads((ROOT/'specs/manifest.json').read_text());STATE.mkdir(parents=True,exist_ok=True)
 results=[]
 with concurrent.futures.ThreadPoolExecutor(max_workers=4)as pool:
  for future in concurrent.futures.as_completed([pool.submit(generate_one,s,args.check)for s in manifest['sources']]):results.append(future.result())
 metadata(manifest,args.check)
 report={'version':1,'generator':'openapi-python-client','generatorVersion':'0.30.0','manifestSha256':sha(ROOT/'specs/manifest.json'),'families':len(results),'publishers':len({r['publisherKey']for r in results}),'expectedOperations':sum(len(r['operations'])for r in results),'generated':sum(r['status']=='generated'for r in results),'reused':sum(r['status']=='reused'for r in results),'failed':sum(r['status']=='failed'for r in results),'warningFamilies':[r['sourceId']for r in results if r['warnings']],'results':sorted(results,key=lambda r:r['sourceId']),'liveApiCalls':0,'canonicalInputsChanged':False}
 dump(ROOT/'reports/python-generation.json',report);print(json.dumps({k:v for k,v in report.items()if k!='results'}))
 if report['failed']:sys.exit(1)
if __name__=='__main__':main()
