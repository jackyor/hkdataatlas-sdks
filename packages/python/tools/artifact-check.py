"""Run with an isolated wheel-installed interpreter; no repository imports required."""
import asyncio,importlib,inspect,json,pkgutil,typing
from enum import Enum
from importlib.resources import files
import httpx2
import hkdataatlas as root
metadata=json.loads((files(root)/'sources.json').read_text())
assert metadata['publisherCount']==len(metadata['publishers'])
assert metadata['apiFamilies']==sum(len(p['sources']) for p in metadata['publishers'])
assert metadata['generator']=='openapi-python-client0.30.0'
count=0;modules=0;partials=[]
for publisher in metadata['publishers']:
 for source in publisher['sources']:
  assert not any(key in source for key in ['origin','originLabel','originCategory'])
  prefix='hkdataatlas.'+publisher['publisherKey'].replace('-','_')+'.'+source['moduleName']
  package=importlib.import_module(prefix);count+=1
  for item in pkgutil.walk_packages(package.__path__,package.__name__+'.'):
   importlib.import_module(item.name);modules+=1
  if source['readiness']['contractScope']=='explicit_partial_contract'and source['readiness']['responseCoverage']['unknownRecordSchemas']:partials.append(package)
assert count==metadata['apiFamilies'] and len(partials)==7

def enum_value(method,name,value):
 annotation=typing.get_type_hints(method).get(name)
 for typ in typing.get_args(annotation)or(annotation,):
  if inspect.isclass(typ)and issubclass(typ,Enum):return typ(value)
 return value

async def exercise(package,module,body,kwargs):
 calls=[]
 def handle(request):calls.append(request);return httpx2.Response(200,json=body)
 for mode in ['sync','async']:
  client=package.Client(base_url='https://example.invalid',httpx_args={'transport':httpx2.MockTransport(handle)})
  try:
   response=module.sync_detailed(client=client,**kwargs)if mode=='sync'else await module.asyncio_detailed(client=client,**kwargs)
   assert response.status_code==200 and response.parsed is not None
   assert json.loads(response.content)==body
   if 'result'in body:assert response.parsed.to_dict()['result']['records']==body['result']['records']
  finally:
   if mode=='sync':client.get_httpx_client().close()
   else:await client.get_async_httpx_client().aclose()
 return len(calls)

async def main():
 package=importlib.import_module('hkdataatlas.censtatd.c_sd_web_table_api')
 module=importlib.import_module(package.__name__+'.api.statistical_tables.get_statistical_table')
 body={'header':{'status':{'name':'Success','code':0,'description':'Synthetic package test'},'count':{}},'dataSet':[{'new_field':[1,None]}]}
 kwargs={'id':'110-01001','lang':enum_value(module.sync_detailed,'lang','en'),'full_series':enum_value(module.sync_detailed,'full_series','1')}
 calls=await exercise(package,module,body,kwargs)
 package=partials[0]
 module=next(importlib.import_module(item.name)for item in pkgutil.walk_packages(package.__path__,package.__name__+'.')if'.api.'in item.name and hasattr(importlib.import_module(item.name),'sync_detailed'))
 body={'header':{'success':True},'result':{'datasize':4,'records':[{},7,None,{'future_field':[1,2]}]}}
 hints=typing.get_type_hints(module.sync_detailed);kwargs={}
 for name,parameter in inspect.signature(module.sync_detailed).parameters.items():
  if name=='client'or parameter.default is not inspect.Parameter.empty:continue
  annotation=hints[name];candidates=typing.get_args(annotation)or(annotation,);typ=next((x for x in candidates if x is not type(None)and getattr(x,'__name__','')!='Unset'),str)
  kwargs[name]=typing.get_args(annotation)[0]if typing.get_origin(annotation)is typing.Literal else next(iter(typ))if inspect.isclass(typ)and issubclass(typ,Enum)else 1 if typ is int else 'synthetic'
 calls+=await exercise(package,module,body,kwargs)
 print(json.dumps({'installedFamilies':count,'publisherModules':len(metadata['publishers']),'importedModules':modules,'partialUnknownRecordFamilies':len(partials),'nativeSyncAsyncMockCalls':calls,'upstreamRequests':0}))
asyncio.run(main())
