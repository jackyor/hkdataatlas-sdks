"""Generate selected Python families using the pinned authoritative generator."""
import concurrent.futures,json,sys
from pathlib import Path
sys.path.insert(0,str(Path('packages/python/tools').resolve()))
from generate import generate_one
ids=set(json.loads(Path(sys.argv[1]).read_text()));sources=[s for s in json.loads(Path('specs/manifest.json').read_text())['sources']if s['id']in ids]
with concurrent.futures.ThreadPoolExecutor(max_workers=4)as pool:
 for result in pool.map(lambda s:generate_one(s,False),sources):
  if result['status']=='failed':raise RuntimeError(result.get('error',result['sourceId']))
