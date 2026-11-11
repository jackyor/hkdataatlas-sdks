"""The wheel rebuilt from sdist must contain exactly the directly built package files."""
import tarfile,zipfile,hashlib
from pathlib import Path

def files(path):
 with zipfile.ZipFile(path)as z:return {n:hashlib.sha256(z.read(n)).hexdigest()for n in z.namelist()if n.startswith('hkdataatlas/')}
original=list(Path('dist/python').glob('*.whl'));rebuilt=list(Path('dist/rebuilt').glob('*.whl'));assert len(original)==len(rebuilt)==1
assert files(original[0])==files(rebuilt[0]),'Wheel built from sdist differs from direct wheel'
for wheel in [original[0],rebuilt[0]]:
 with zipfile.ZipFile(wheel)as z:
  names=z.namelist();assert any(n.endswith('/licenses/LICENSE')for n in names);assert any(n.endswith('/licenses/THIRD_PARTY_NOTICES.md')for n in names)
  assert not any('/.generation/'in n or'/tools/'in n or'/tests/'in n or'/.ruff_cache/'in n or'/__pycache__/'in n or n.endswith('.pyc') for n in names)
for archive in Path('dist/python').glob('*.tar.gz'):
 with tarfile.open(archive)as t:
  names=t.getnames();assert not any('/.generation/'in n or'/tools/'in n or'/tests/'in n or'/.ruff_cache/'in n or'/__pycache__/'in n or n.endswith('.pyc') for n in names)
print('Direct wheel and sdist-rebuilt wheel contain identical package files, licenses and notices; generator state and tests excluded.')
