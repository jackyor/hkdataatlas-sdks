# Contributing

This repository contains finalized OpenAPI descriptions, generated SDK products and consumer documentation. Conversion, SDK generation, templates, intake and live-response analysis are maintained in the private producer workflow. They are not prerequisites for building or using these public products. Earlier Git history is preserved; moving a file out of the current tree does not remove its historical publication.

Report contract issues with the publisher URL, affected source ID and a bounded explanation of the expected behavior. Do not attach private captures, credentials or personal information. Producer changes should transfer the selected final JSON/YAML and generated products together, with aligned package versions and preserved publisher terms; do not hand-edit generated clients independently of their descriptions.

Install the pinned build tools, then check the already-generated products:

```sh
bun install --ignore-scripts --frozen-lockfile
uv sync --frozen
bun run check
```

The checks compare final JSON/YAML hashes and semantics, compile publisher modules, import the packaged families, exercise synthetic consumer calls and compare direct/rebuilt Python wheels. They make no publisher API requests and do not establish universal live-response correctness.

Commit the candidate before running `bun run ci` and `bun run ci:verify`. The minimal Dagger package wrapper builds from the exact clean Git archive and rejects dirty or untracked source. Registry publication remains a separate OIDC release workflow described in [RELEASING.md](RELEASING.md).
