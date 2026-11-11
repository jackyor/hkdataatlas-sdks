"""All-family imports, source-valid synthetic payloads and native sync/async calls."""
from __future__ import annotations
import ast,asyncio,datetime,hashlib,importlib,inspect,json,keyword,pkgutil,re,sys,typing
from enum import Enum
from pathlib import Path
import httpx2
import jsonschema
ROOT=Path(__file__).resolve().parents[3]
PACKAGE=ROOT/'packages/python'
if '--installed'not in sys.argv:sys.path.insert(0,str(PACKAGE/'src'))
METHODS={'get','put','post','delete','options','head','patch','trace'}
def snake(s):return re.sub(r'[^a-zA-Z0-9_]','_',s).lower()
def deref(spec,schema):
 seen=set()
 while isinstance(schema,dict)and isinstance(schema.get('$ref'),str)and schema['$ref'].startswith('#/')and schema['$ref']not in seen:
  seen.add(schema['$ref']);schema=schema['$ref'][2:].split('/');schema=__import__('functools').reduce(lambda a,k:a[int(k)]if isinstance(a,list)else a[k.replace('~1','/').replace('~0','~')],schema,spec)
 return schema

def sample(spec,schema,depth=0,all_fields=False):
 schema=deref(spec,schema)
 if schema is False:return None
 if schema is True or not schema:return {'unknown_record':[{'future':1},7,None]}
 if depth>10:return {}
 if 'const'in schema:return schema['const']
 if schema.get('enum'):return schema['enum'][0]
 if schema.get('allOf'):
  values=[sample(spec,s,depth+1,all_fields)for s in schema['allOf']]
  if all(isinstance(x,dict)for x in values):return {k:v for x in values for k,v in x.items()}
  return values[-1]
 if schema.get('oneOf')or schema.get('anyOf'):return sample(spec,(schema.get('oneOf')or schema['anyOf'])[0],depth+1,all_fields)
 typ=schema.get('type');typ=next((x for x in typ if x!='null'),'null')if isinstance(typ,list)else typ
 if typ=='object'or'properties'in schema:
  names=schema.get('properties',{})if all_fields else schema.get('required',[])
  return {name:sample(spec,schema.get('properties',{}).get(name,{}),depth+1,all_fields)for name in names}
 if typ=='array':return [sample(spec,schema.get('items',{}),depth+1,all_fields)for _ in range(max(0,schema.get('minItems',0)))]
 if typ in ['number','integer']:
  value=max(0,schema.get('minimum',0));value=value+1 if isinstance(schema.get('exclusiveMinimum'),(int,float))and not isinstance(schema.get('exclusiveMinimum'),bool)else value
  return int(value)if typ=='integer'else value
 if typ=='boolean':return True
 if typ=='null':return None
 if typ=='string':
  if schema.get('format')=='date':return '2026-01-01'
  if schema.get('format')=='date-time':return '2026-01-01T00:00:00Z'
  return 'x'*max(1,schema.get('minLength',0))
 return {'unknown_record':[{'future':1},7,None]}

def validator(spec,schema):
 if isinstance(schema,bool):return jsonschema.Draft202012Validator(schema)
 schema={**schema,'components':spec.get('components',{})}
 return jsonschema.Draft202012Validator(schema)

def endpoint_identity(module):
 tree=ast.parse(Path(module.__file__).read_text())
 for node in ast.walk(tree):
  if isinstance(node,ast.Dict):
   values={k.value:v for k,v in zip(node.keys,node.values)if isinstance(k,ast.Constant)and isinstance(k.value,str)}
   if 'method'in values and'url'in values:
    method=values['method'];url=values['url']
    if isinstance(url,ast.Call)and isinstance(url.func,ast.Attribute)and url.func.attr=='format':url=url.func.value
    if isinstance(method,ast.Constant)and isinstance(url,ast.Constant):return method.value.lower(),re.sub(r'\{[^}]+\}','{}',url.value)
 raise RuntimeError('No native endpoint identity: '+module.__name__)

def parameter_value(spec,parameter):
 schema=deref(spec,parameter.get('schema',{}));value=sample(spec,schema)
 if schema.get('type')=='array'and value==[]:value=[sample(spec,schema.get('items',{}))]
 return value

def coerce(value,annotation):
 origin=typing.get_origin(annotation);types=typing.get_args(annotation)
 if origin is list:return [coerce(x,types[0])for x in value]
 if origin in [typing.Union,__import__('types').UnionType]:
  for typ in types:
   if typ is type(None)or getattr(typ,'__name__','')=='Unset':continue
   if typing.get_origin(typ)is list and isinstance(value,list):return coerce(value,typ)
   if inspect.isclass(typ)and issubclass(typ,Enum):return typ(value)
  return coerce(value,next((x for x in types if x is not type(None)and getattr(x,'__name__','')!='Unset'),typing.Any))
 if inspect.isclass(annotation)and issubclass(annotation,Enum):return annotation(value)
 if annotation is datetime.date:return datetime.date.fromisoformat(value)
 if annotation is datetime.datetime:return datetime.datetime.fromisoformat(value.replace('Z','+00:00'))
 return value

def kwargs_for(module,spec,item,operation,fixture):
 signature=inspect.signature(module.sync_detailed);hints=typing.get_type_hints(module.sync_detailed);args={}
 for raw in [*item.get('parameters',[]),*operation.get('parameters',[])]:
  p=deref(spec,raw);name=p['name'];candidate=re.sub(r'([a-z0-9])([A-Z])',r'\1_\2',name);candidate=re.sub(r'[^a-zA-Z0-9_]','_',candidate).lower();compact=re.sub(r'[^a-zA-Z0-9_]','',name).lower();choices=[name,candidate,name+'_',candidate+'_','field_'+candidate,compact,compact+'_']
  pyname=next((n for n in choices if n in signature.parameters),None)
  if pyname is None:raise RuntimeError(f'Parameter missing: {module.__name__}/{name}')
  value=coerce(parameter_value(spec,p),hints.get(pyname))
  args[pyname]=value;fixture['parameters'].append({'name':name,'in':p['in'],'value':value.value if isinstance(value,Enum)else value.isoformat()if isinstance(value,(datetime.date,datetime.datetime))else value})
 if 'requestBody'in operation:
  body=deref(spec,operation['requestBody']);media=next(iter(body['content']));body_value=sample(spec,body['content'][media].get('schema',{}),all_fields=True);name=next(n for n in ['body','json_body']if n in signature.parameters);annotation=hints[name]
  cls=next((x for x in (typing.get_args(annotation)or(annotation,))if inspect.isclass(x)and hasattr(x,'from_dict')),None);args[name]=cls.from_dict(body_value)if cls else body_value;fixture['requestBody']={'contentType':media,'body':body_value}
 return args

async def exercise(module,Client,args,fixture):
 outcomes={}
 for mode in ['sync','async']:
  captured=[]
  def handle(request):
   captured.append(request)
   kw={'json':fixture['body']}if'json'in fixture['contentType']else{'content':str(fixture['body']).encode()}
   return httpx2.Response(fixture['status'],headers={'Content-Type':fixture['contentType'],'X-SDK-Mock':'yes'},**kw)
  client=Client(base_url='https://example.invalid',httpx_args={'transport':httpx2.MockTransport(handle)})
  try:
   response=module.sync_detailed(client=client,**args)if mode=='sync'else await module.asyncio_detailed(client=client,**args)
   assert len(captured)==1 and captured[0].method.lower()==fixture['method']
   assert int(response.status_code)==fixture['status']
   if fixture['expectsParsed']:assert response.parsed is not None,(module.__name__,'success response omitted')
   if fixture['method']!='head'and fixture['status']!=204:
    expected_raw=json.dumps(fixture['body']).encode()if'json'in fixture['contentType']else str(fixture['body']).encode()
    if'json'in fixture['contentType']:assert json.loads(response.content)==fixture['body']
    else:assert response.content==expected_raw
   if fixture.get('unknownRecordsProbe'):assert response.parsed.to_dict()['result']['records']==fixture['body']['result']['records']
   outcomes[mode]={'passed':True,'parsed':response.parsed is not None,'parsedType':type(response.parsed).__name__,'rawRetained':response.headers.get('X-SDK-Mock')=='yes'}
  except Exception as e:outcomes[mode]={'passed':False,'error':type(e).__name__+': '+str(e)}
  finally:
   if mode=='sync':client.get_httpx_client().close()
   else:await client.get_async_httpx_client().aclose()
 return outcomes

async def main():
 manifest=json.loads((ROOT/'specs/manifest.json').read_text());selected={a.split('=',1)[1]for a in sys.argv if a.startswith('--source=')}
 scope_arg=next((a.split('=',1)[1]for a in sys.argv if a.startswith('--operations-from=')),None)
 scope=json.loads((ROOT/scope_arg).read_text())if scope_arg else None
 if scope and not selected:selected={row['sourceId']for row in scope['entries']}
 affected={row['sourceId']:{(o['method'].lower(),o['path'])for o in row.get('affectedOperations',[])}for row in scope['entries']}if scope else {}
 if selected:
  manifest={**manifest,'sources':[source for source in manifest['sources']if source['id']in selected]}
  assert {source['id']for source in manifest['sources']}==selected,'Unknown source selection'
 wrong_types=0;raw_media_calls=0
 expected_count=sum(sum(m in METHODS and(not affected or(m,p)in affected[source['id']])for m in item)for source in manifest['sources']for p,item in json.loads((ROOT/'specs'/source['json']).read_text())['paths'].items());results=[];fixtures=[];errors=[];imported=0
 for source in manifest['sources']:
  spec=json.loads((ROOT/'specs'/source['json']).read_text())
  state=json.loads((PACKAGE/'.generation'/(source['id']+'.json')).read_text())
  # Recreate equivalent generator input from the final contract; no private saved inputs are needed.
  from generate import normalize,normalize_wire
  retained={row['id']:row['jsonSha256']for row in json.loads((ROOT/'scripts/legacy/native-fetch-v1/sources.json').read_text())['sources']}
  derived_spec=json.loads(json.dumps(spec));normalizations=[]
  if retained.get(source['id'])!=source['jsonSha256']:normalize_wire(derived_spec,normalizations)
  normalize(derived_spec,normalizations)
  derived_bytes=(json.dumps(derived_spec,indent=2)+'\n').encode()
  assert hashlib.sha256(derived_bytes).hexdigest()==state['derivedInputSha256']
  restored=json.loads(derived_bytes)
  def at(node,pointer):
   for key in pointer.split('/')[1:]:node=node[int(key)]if isinstance(node,list)else node[key.replace('~1','/').replace('~0','~')]
   return node
  for change in reversed(state['normalizations']):
   target=at(restored,change['pointer']);original=at(spec,change['pointer'])
   if change['rule']=='inline_local_parameter_reference':
    target.clear();target.update(change['sourceReference'])
   elif change['rule']=='text_media_raw_wire_response':
    assert target['schema']['type']=='string';target['schema']=change['sourceSchema']
   elif change['rule']=='const_to_singleton_enum':
    assert target['enum']==[original['const']];del target['enum'];target['const']=original['const']
   else:assert target['items']=={};del target['items']
  assert restored==spec,'Generator-only representation does not reconstruct canonical source'
  prefix='hkdataatlas.'+snake(source['publisherKey'])+'.'+snake(source['familyKey'])
  try:
   package=importlib.import_module(prefix);endpoints={}
   if '--installed'in sys.argv:assert Path(package.__file__).is_relative_to(Path(sys.prefix)),package.__file__
   for item in pkgutil.walk_packages(package.__path__,package.__name__+'.'):
    module=importlib.import_module(item.name);imported+=1
    if hasattr(module,'sync_detailed')and hasattr(module,'asyncio_detailed'):endpoints[endpoint_identity(module)]=module
   expected={(method,path)for path,item in spec['paths'].items()for method in item if method in METHODS};assert set(endpoints)=={(m,re.sub(r'\{[^}]+\}','{}',p))for m,p in expected},(source['id'],'operation coverage',expected,set(endpoints))
   for method,path in sorted(expected):
    if affected and(method,path)not in affected[source['id']]:continue
    operation=spec['paths'][path][method];responses=operation.get('responses',{});status=next((k for k in responses if str(k).startswith('2')),None)or('default'if'default'in responses else next(iter(responses)))
    statuscode=int(status)if str(status).isdigit()else 200;response=deref(spec,responses[status]);content=response.get('content',{});media=next(iter(content),'application/json');schema=content.get(media,{}).get('schema',{});payload=None
    for all_fields in [False,True]:
     candidate=sample(spec,schema,all_fields=all_fields)
     if content.get(media,{}).get('x-jsonp-callback'):
      argument=sample(spec,content[media].get('x-jsonp-argument-schema',{}),all_fields=all_fields)
      candidate=content[media]['x-jsonp-callback']+'('+json.dumps(argument)+')'
     if validator(spec,schema).is_valid(candidate):payload=candidate;break
    if payload is None and not validator(spec,schema).is_valid(None):raise RuntimeError('Cannot create source-valid response: '+source['id']+path)
    unknown=schema=={}or schema is True or(isinstance(schema,dict)and not set(schema)&{'$ref','type','properties','items','oneOf','anyOf','allOf','enum','const','additionalProperties'})
    probe=bool(source.get('readiness',{}).get('responseCoverage',{}).get('unknownRecordSchemas',[]))
    if probe:
     payload={'header':{'success':True},'result':{'datasize':4,'records':[{},7,None,{'future_field':[1,2]}]}}
     assert validator(spec,schema).is_valid(payload),'Partial fixture invalid'
    resolved_schema=deref(spec,schema);declared_type=resolved_schema.get('type')if isinstance(resolved_schema,dict)else None
    wrong=[]if declared_type=='object'or isinstance(resolved_schema,dict)and'properties'in resolved_schema else {}if declared_type in ['string','array','integer','number','boolean']else None
    if wrong is not None and not validator(spec,schema).is_valid(wrong):wrong_types+=1
    native_media_supported=media.startswith('text/')or media in {'application/json','application/octet-stream'}or media.endswith('+json')
    expects=bool(content)and method!='head'and statuscode!=204 and not unknown and native_media_supported
    schema_value=payload
    logical_text='json'not in media and(media.startswith('text/')or'xml'in media)and not isinstance(payload,str)
    if logical_text:payload='<mock/>'
    fixture={'sourceId':source['id'],'sourceSha256':source['jsonSha256'],'operationId':operation.get('operationId'),'method':method,'path':path,'status':statuscode,'contentType':media,'body':payload,'schemaValue':schema_value,'schemaValidAppliesTo':'schemaValue','wireRepresentation':'synthetic_text_transport_bytes_not_XML_schema_fit'if logical_text else'logical_fixture_serialization','schemaValid':True,'expectsParsed':expects,'unknownSchema':unknown,'nativeResponseSupport':'raw_only_unsupported_media'if not native_media_supported else'raw_only_unknown_schema'if unknown else'parsed_schema','unknownRecordsProbe':bool(probe),'parameters':[]}
    module=endpoints[(method,re.sub(r'\{[^}]+\}','{}',path))];args=kwargs_for(module,spec,spec['paths'][path],operation,fixture);fixture['python']={'module':module.__name__,'kwargs':{k:v.value if isinstance(v,Enum)else v.isoformat()if isinstance(v,(datetime.date,datetime.datetime))else v for k,v in args.items()}};fixtures.append(fixture)
    outcomes=await exercise(module,package.Client,args,fixture)
    if any('json'not in kind for kind in content):
     for actual_media in content:
      if'json'in actual_media:continue
      raw_fixture={**fixture,'contentType':actual_media,'body':'native \u0000 bytes \ufffd','expectsParsed':False,'unknownRecordsProbe':False}
      raw_outcomes=await exercise(module,package.Client,args,raw_fixture)
      assert all(v['passed']for v in raw_outcomes.values()),raw_outcomes
      raw_media_calls+=2
    results.append({'sourceId':source['id'],'method':method,'path':path,'module':module.__name__,**outcomes})
  except Exception as e:errors.append({'sourceId':source['id'],'error':type(e).__name__+': '+str(e)})
 out={'version':1,'manifestSha256':hashlib.sha256((ROOT/'specs/manifest.json').read_bytes()).hexdigest(),'installedArtifact':'--installed'in sys.argv,'equivalentInputProofs':len(manifest['sources']),'inputProofMeaning':'Exact reversible canonical reconstruction; XML/text wire selections do not assert logical-model validation equivalence.','expectedOperations':expected_count,'families':len(manifest['sources']),'operations':len(fixtures),'sourceUnknownResponseOperations':sum(x['unknownSchema']for x in fixtures),'partialUnknownRecordProbes':sum(x['unknownRecordsProbe']for x in fixtures),'imports':imported,'syncPassed':sum(x['sync']['passed']for x in results),'asyncPassed':sum(x['async']['passed']for x in results),'failures':errors+[x for x in results if not x['sync']['passed']or not x['async']['passed']],'results':results,'wrongTypeSchemaRejections':wrong_types,'additionalNativeMediaSyncAsyncCalls':raw_media_calls,'liveApiCalls':0,'fixtureMeaning':'Independent logical source-schema fixtures; non-JSON transport bytes separately labelled and do not establish XML wire-schema fit or publisher live-response evidence.'}
 (ROOT/'reports').mkdir(exist_ok=True);(ROOT/('reports/python-correction-fixtures.json'if selected else'reports/python-mock-fixtures.json')).write_text(json.dumps({'version':1,'operations':fixtures},indent=2,default=str)+'\n');(ROOT/('reports/python-corrections.json'if selected else'reports/python-installed-adoption.json'if'--installed'in sys.argv else'reports/python-adoption.json')).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in ['results','failures']},indent=2));print(json.dumps(out['failures'][:20],indent=2))
 if out['failures']or len(fixtures)!=expected_count:sys.exit(1)
if __name__=='__main__':asyncio.run(main())
