"""Verify the built wheel in an isolated install with synthetic network responses only."""
import json,subprocess,sys,tempfile
from pathlib import Path
with tempfile.TemporaryDirectory(prefix='hkdataatlas-public-wheel-')as temp:
 wheels=list(Path('dist/python').glob('*.whl'));assert len(wheels)==1
 subprocess.run(['uv','venv',temp+'/venv','--python',sys.executable],check=True)
 python=temp+'/venv/bin/python';subprocess.run(['uv','pip','install','--python',python,str(wheels[0])],check=True)
 manifest=json.loads(Path('specs/manifest.json').read_text());modules=['hkdataatlas.'+s['publisherKey'].replace('-','_')+'.'+s['familyKey'].replace('-','_')for s in manifest['sources']]
 parking_fixture=json.loads(Path('tests/fixtures/carpark-without-opening-hours.json').read_text())
 code='''import asyncio,importlib,httpx2,json
from hkdataatlas.hkma.banks_branch_locator import Client
from hkdataatlas.hkma.banks_branch_locator.api.default import get_banks_branch_locator
seen=[]
def handler(request):
 seen.append(request)
 return httpx2.Response(200,json={"header":{"success":True},"result":{"datasize":0,"records":[]}})
client=Client(base_url="https://api.hkma.gov.hk/public/bank-svf-info").set_httpx_client(httpx2.Client(transport=httpx2.MockTransport(handler),base_url="https://api.hkma.gov.hk/public/bank-svf-info"))
response=get_banks_branch_locator.sync_detailed(client=client,lang="en",pagesize=1)
assert response.status_code==200 and response.parsed.header.success is True
assert seen[0].url.params['pagesize']=='1'
async def check_async():
 client=Client(base_url="https://api.hkma.gov.hk/public/bank-svf-info").set_async_httpx_client(httpx2.AsyncClient(transport=httpx2.MockTransport(handler),base_url="https://api.hkma.gov.hk/public/bank-svf-info"))
 response=await get_banks_branch_locator.asyncio_detailed(client=client,lang="en",pagesize=1)
 assert response.status_code==200 and response.parsed.header.success is True
 await client.get_async_httpx_client().aclose()
asyncio.run(check_async())
'''+f'\nfrom hkdataatlas.dpo.parking_vacancy_data_api.models.carpark_info import CarparkInfo\nfrom hkdataatlas.dpo.parking_vacancy_data_api.types import UNSET\nparking=CarparkInfo.from_dict({parking_fixture!r})\nassert parking.opening_hours is UNSET and \"openingHours\" not in parking.to_dict()\nfor name in {modules!r}:importlib.import_module(name)\nprint("Installed wheel: {len(modules)} family imports, sync/async synthetic HKMA responses passed.")'
 script=Path(temp)/'verify.py';script.write_text(code)
 subprocess.run([python,str(script)],check=True)
 # Validate the synthetic payload independently against the canonical response schema.
 import jsonschema
 spec=json.loads(Path('specs/hkma/banks-branch-locator/openapi.json').read_text());schema=spec['paths']['/banks-branch-locator']['get']['responses']['200']['content']['application/json']['schema']
 jsonschema.Draft202012Validator(schema,resolver=jsonschema.RefResolver.from_schema(spec)).validate({'header':{'success':True},'result':{'datasize':0,'records':[]}})

 parking_spec=json.loads(Path('specs/dpo/parking-vacancy-data-api/openapi.json').read_text())
 jsonschema.Draft202012Validator(parking_spec['components']['schemas']['CarparkInfo'],resolver=jsonschema.RefResolver.from_schema(parking_spec)).validate(parking_fixture)
