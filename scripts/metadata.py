"""Generate public Python package metadata without importing private observations."""
import json
from pathlib import Path
root=Path('.');config=json.loads((root/'sdk-config.json').read_text());manifest=json.loads((root/'specs/manifest.json').read_text());package=root/'packages/python';module=package/'src'/config['python']['module'];groups={}
for source in manifest['sources']:groups.setdefault(source['publisherKey'],[]).append(source)
def emit(path,value):path.parent.mkdir(parents=True,exist_ok=True);path.write_text(value if isinstance(value,str)else json.dumps(value,indent=2)+'\n')
publishers=[]
for key,sources in groups.items():
 namespace=key.replace('-','_');data={'publisherKey':key,'publisherName':sources[0]['publisherName'],'sources':[{**s,'moduleName':s['familyKey'].replace('-','_')}for s in sources]};publishers.append(data);emit(module/namespace/'sources.json',data)
emit(module/'sources.json',{'packageVersion':config['version'],'publisherCount':len(groups),'apiFamilies':len(manifest['sources']),'generator':'openapi-python-client0.30.0','publishers':publishers,'limitations':['Explicit Client(base_url=...) is required.','attrs parsing is not complete JSON Schema validation.','No historical live response observations are included.']})
emit(module/'__init__.py','"""Hong Kong API clients grouped by publisher."""\n__version__ = '+repr(config['version'])+'\n')
emit(package/'pyproject.toml',f'''[build-system]
requires = ["hatchling==1.30.1"]
build-backend = "hatchling.build"

[project]
name = "{config['python']['name']}"
version = "{config['version']}"
description = "Hong Kong public API clients grouped by publisher"
readme = "README.md"
license = "MIT"
license-files = ["LICENSE", "THIRD_PARTY_NOTICES.md"]
requires-python = ">=3.11"
dependencies = ["httpx2==2.16.0", "attrs==26.1.0"]

[project.urls]
Repository = "https://github.com/{config['repository']}"
Issues = "https://github.com/{config['repository']}/issues"

[tool.hatch.build.targets.wheel]
packages = ["src/{config['python']['module']}"]
exclude = ["**/.ruff_cache/**", "**/__pycache__/**", "**/*.pyc"]

[tool.hatch.build.targets.sdist]
include = ["/src", "/README.md", "/LICENSE", "/THIRD_PARTY_NOTICES.md", "/pyproject.toml"]
exclude = ["**/.ruff_cache/**", "**/__pycache__/**", "**/*.pyc"]
''')
emit(package/'README.md',(root/'README.md').read_text())
