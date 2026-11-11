# Contributing

Change the canonical final OpenAPI description or supported generator configuration rather than hand-editing generated output. Preserve publisher attribution, official source URLs and applicable terms. Describe the evidence and limits of a contract correction without including private captures, credentials or personal information.

Install the pinned toolchain specified by the repository, then run:

```sh
bun install --ignore-scripts --frozen-lockfile
uv sync --frozen
bun run generate
bun run generate:check
bun run check
```

The public pipeline starts from the final JSON/YAML descriptions and does not require private inputs. To reproduce a single family from scratch, use `node scripts/generate.mjs --force --source=<source-id>`. The checks verify generated output hashes, compile publisher modules, import packaged families, exercise synthetic HKMA responses in Python sync and async clients, and compare Python source and wheel contents. They do not validate every possible live response.

Commit the candidate before running `bun run ci` and `bun run ci:verify`: Dagger builds from a clean Git archive of HEAD and rejects dirty or untracked source. Live response checks are optional, separate bounded observations; they are not required for a release and do not establish universal contract validity.
