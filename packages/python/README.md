# HK Data Atlas SDKs

This repository contains final OpenAPI JSON and YAML descriptions and generated clients for Hong Kong public APIs. It provides one TypeScript package, `hkdataatlas`, and one Python distribution, `hkdataatlas`, with publisher modules. Version 0.0.2 keeps the public tree focused on finalized products and adds exact-byte verification for safe repeated or pending releases.

The clients were generated with Orval native fetch and openapi-python-client; producer tooling is maintained separately. Each description is under `specs/<publisher>/<family>/`; YAML is a deterministic representation of the selected JSON. Source metadata identifies publishers and links to their original material. API descriptions can be incomplete; types and generated models do not guarantee that every live response satisfies a schema. Publisher terms and attribution continue to apply.

## Usage

```sh
npm install hkdataatlas
python -m pip install hkdataatlas
```

```ts
import { banksBranchLocator } from 'hkdataatlas/hkma';
const response = await banksBranchLocator.getBanksBranchLocator(
  { lang: 'en', pagesize: 1 },
  { signal: AbortSignal.timeout(15000) },
);
console.log(response.status, response.data);
```

```python
from hkdataatlas.hkma.banks_branch_locator import Client
from hkdataatlas.hkma.banks_branch_locator.api.default import get_banks_branch_locator

with Client(base_url="https://api.hkma.gov.hk/public/bank-svf-info") as client:
    response = get_banks_branch_locator.sync_detailed(client=client, lang="en", pagesize=1)
    print(response.status_code, response.parsed)
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for product builds and verification, [RELEASING.md](RELEASING.md) for release setup, and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for source terms.
