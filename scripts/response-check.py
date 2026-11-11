"""An explicit bounded live response/schema observation; output stays in ignored reports/."""
import argparse,hashlib,json
from pathlib import Path
from datetime import datetime,timezone
from urllib.parse import urljoin
import httpx,jsonschema
p=argparse.ArgumentParser();p.add_argument('--source',required=True,help='family id in specs/manifest.json');p.add_argument('--operation',required=True,help='exact GET operationId');p.add_argument('--params',default='{}',help='JSON object of declared query values');p.add_argument('--timeout',type=float,default=15);p.add_argument('--max-bytes',type=int,default=2_000_000);a=p.parse_args()
sources=json.loads(Path('specs/manifest.json').read_text())['sources'];source=next(s for s in sources if s['id']==a.source);raw=Path('specs',source['json']).read_bytes();assert hashlib.sha256(raw).hexdigest()==source['jsonSha256'];spec=json.loads(raw);matches=[(path,item,op)for path,item in spec['paths'].items()for method,op in item.items()if method=='get'and op.get('operationId')==a.operation];assert len(matches)==1,'Select exactly one declared GET operation'
path,item,op=matches[0];assert'{'not in path,'This bounded command supports query-only GET operations';assert not op.get('security',spec.get('security')),'Authenticated operations require a caller-managed integration';params=json.loads(a.params);assert isinstance(params,dict)
declared={v['name']:v for v in item.get('parameters',[])+op.get('parameters',[])if isinstance(v,dict)and v.get('in')=='query'};assert set(params)<=set(declared),'Unknown query parameter';assert all(name in params for name,v in declared.items()if v.get('required')),'Missing required query parameter'
servers=op.get('servers',item.get('servers',spec.get('servers',[])));assert servers and servers[0]['url'].startswith('https://');url=servers[0]['url'].rstrip('/')+'/'+path.lstrip('/');body=bytearray();schema_status='not_checked';status=None
try:
 with httpx.stream('GET',url,params=params,timeout=a.timeout,follow_redirects=False)as r:
  status=r.status_code
  for chunk in r.iter_bytes():
   if len(body)+len(chunk)>a.max_bytes:raise RuntimeError('Response exceeded byte bound; no full-body/schema claim')
   body.extend(chunk)
  response=op['responses'].get(str(status),op['responses'].get('default',{}));media=r.headers.get('content-type','').split(';')[0];schema=response.get('content',{}).get(media,{}).get('schema')
  if schema is not None:
   value=json.loads(body)if media=='application/json'or media.endswith('+json')else body.decode('utf-8')
   jsonschema.Draft202012Validator(schema,resolver=jsonschema.RefResolver.from_schema(spec)).validate(value);schema_status='passed'
  else:schema_status='schema_not_declared_for_returned_status_and_media'
finally:
 record={'kind':'bounded-live-response-observation','observedAt':datetime.now(timezone.utc).isoformat(),'sourceId':a.source,'sourceSha256':source['jsonSha256'],'operationId':a.operation,'statusCode':status,'bytes':len(body),'bodySha256':hashlib.sha256(body).hexdigest(),'schema':schema_status,'accepted':False,'limitations':['One bounded observation only. No body or credentials are published. Not acceptance or complete contract coverage.']};Path('reports').mkdir(exist_ok=True);Path('reports/response-observation.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2))
if status is None or not 200<=status<300 or schema_status!='passed':raise SystemExit(1)
