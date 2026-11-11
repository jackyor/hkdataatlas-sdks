// Check finalized products and package metadata; no producer or SDK generation runs here.
import assert from 'node:assert/strict';
import {readFile,access} from 'node:fs/promises';
import {parse} from 'yaml';
import {digest,publishers,json} from '../scripts/lib/workspace.mjs';
for(const path of ['scripts/generate.mjs','scripts/legacy','scripts/response-check.py','packages/python/tools','packages/python/.generation','packages/typescript/.generation','.github/workflows/response-check.yml']){await assert.rejects(access(path),error=>error.code==='ENOENT',`Private producer path in public tree: ${path}`);}
const config=await json('sdk-config.json'),typescript=await json('packages/typescript/package.json'),python=await readFile('packages/python/pyproject.toml','utf8');
assert.equal(config.generators,undefined);assert.deepEqual(Object.keys((await json('package.json')).devDependencies).sort(),['typescript','yaml']);
assert.equal(typescript.name,config.typescript.name);assert.equal(typescript.version,config.version);assert.equal(config.typescript.name,config.python.name);
assert.ok(python.includes(`name = "${config.python.name}"`));assert.ok(python.includes(`version = "${config.version}"`));assert.equal(typescript.repository.url,`git+https://github.com/${config.repository}.git`);
const groups=await publishers();let families=0;
for(const p of groups)for(const s of p.sources){const raw=await readFile(s.jsonPath),yaml=await readFile(s.yamlPath);assert.equal(digest(raw),s.jsonSha256);assert.equal(digest(yaml),s.yamlSha256);assert.deepEqual(JSON.parse(raw),parse(yaml.toString()));families++;}
assert.equal((await json('packages/typescript/sources.json')).packageVersion,config.version);assert.equal((await json('packages/python/src/hkdataatlas/sources.json')).packageVersion,config.version);
console.log(`Final products verified: ${groups.length} publishers, ${families} canonical JSON/YAML pairs and aligned package metadata.`);
