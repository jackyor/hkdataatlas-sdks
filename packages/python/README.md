# HK Data Atlas SDKs

This repository contains final OpenAPI JSON and YAML descriptions and generated clients for Hong Kong public APIs. It provides one TypeScript package, `hkdataatlas`, and one Python distribution, `hkdataatlas`, with publisher modules. The proposed first version is 0.0.1. Registry availability is not implied by this draft.

The default generators are pinned Orval native fetch and openapi-python-client. Each description is under `specs/<publisher>/<family>/`; YAML is a deterministic representation of the selected JSON. Source metadata identifies publishers and links to their original material. API descriptions can be incomplete; types and generated models do not guarantee that every live response satisfies a schema. Publisher terms and attribution continue to apply.

## Usage after publication

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

See [CONTRIBUTING.md](CONTRIBUTING.md) for generation and verification, [RELEASING.md](RELEASING.md) for release setup, and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for source terms.
