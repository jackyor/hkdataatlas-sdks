# HK Data Atlas — Hong Kong data SDK

One npm package, `hkdataatlas`, with 84 publisher modules and 1360 API families, generated with Orval 8.47.0 native fetch.

```ts
import { banksBranchLocator } from 'hkdataatlas/hkma';
const result = await banksBranchLocator.getBanksBranchLocator(
  { lang: 'en' }, { signal: AbortSignal.timeout(15000) },
);
console.log(result.status, result.data);
```

Each function takes its generated path/query/body/header arguments, followed by native RequestInit options and an optional fetch function. See its declaration for the exact signature. Responses expose data, status and Headers. Publisher subpaths are modules within one package, not separately installable packages. Native fetch has no runtime package dependency. Static TypeScript types do not validate network responses.

The bundled sources.json records URLs, hashes and partial-contract markers. Canonical JSON/YAML files remain unchanged in the repository. Generator-only equivalent input normalization preserves mandatory query parameters with defaults and required-only anyOf alternatives. Distinct API hosts and contracts remain separate family modules.

Authored code is MIT licensed; publisher materials retain their terms. Install the single public package with `npm install hkdataatlas`.
