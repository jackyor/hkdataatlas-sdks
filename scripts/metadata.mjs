import {execFileSync} from 'node:child_process';
import {readFile,writeFile,copyFile,mkdir} from 'node:fs/promises';
import {digest,publishers,json} from './lib/workspace.mjs';
async function identity(){const groups=await publishers(),inputs=['scripts/metadata.mjs','scripts/metadata.py','scripts/scaffold.mjs','sdk-config.json','specs/manifest.json','README.md','LICENSE','THIRD_PARTY_NOTICES.md'];const configHash=digest(JSON.stringify(await Promise.all(inputs.map(async p=>[p,digest(await readFile(p))]))));const paths=['packages/typescript/package.json','packages/typescript/tsconfig.json','packages/typescript/sources.json','packages/typescript/README.md','packages/typescript/LICENSE','packages/typescript/THIRD_PARTY_NOTICES.md','packages/typescript/src/index.ts','packages/python/pyproject.toml','packages/python/README.md','packages/python/LICENSE','packages/python/THIRD_PARTY_NOTICES.md','packages/python/src/hkdataatlas/__init__.py','packages/python/src/hkdataatlas/sources.json',...groups.flatMap(p=>[`packages/typescript/src/publishers/${p.key}/index.ts`,`packages/typescript/.generation/${p.key}/tsconfig.json`,`packages/python/src/hkdataatlas/${p.namespace}/sources.json`])];return{schemaVersion:1,configHash,files:Object.fromEntries(await Promise.all(paths.map(async p=>[p,digest(await readFile(p))])))};}
if(process.argv.includes('--check')){const old=await json('release/metadata.json'),current=await identity();if(JSON.stringify(old)!==JSON.stringify(current))throw Error('Public generated package metadata is stale; run node scripts/metadata.mjs.');console.log('Public package metadata input and output hashes verified.');process.exit(0);}
const run=(...args)=>execFileSync(...args,{stdio:'inherit'});
run(process.execPath,['scripts/scaffold.mjs']);
const config=JSON.parse(await readFile('sdk-config.json'));
const path='packages/typescript/package.json',pkg=JSON.parse(await readFile(path));
pkg.repository={type:'git',url:`git+https://github.com/${config.repository}.git`,directory:'packages/typescript'};
pkg.homepage=`https://github.com/${config.repository}#readme`;
pkg.bugs={url:`https://github.com/${config.repository}/issues`};
pkg.publishConfig={access:'public'};
pkg.files.push('THIRD_PARTY_NOTICES.md');
await writeFile(path,JSON.stringify(pkg,null,2)+'\n');
await copyFile('THIRD_PARTY_NOTICES.md','packages/typescript/THIRD_PARTY_NOTICES.md');
await copyFile('THIRD_PARTY_NOTICES.md','packages/python/THIRD_PARTY_NOTICES.md');
await copyFile('LICENSE','packages/python/LICENSE');
run(process.env.SDK_EXPORT_PYTHON||'uv',process.env.SDK_EXPORT_PYTHON?['scripts/metadata.py']:['run','--frozen','python','scripts/metadata.py']);
let readme=await readFile('packages/typescript/README.md','utf8');
readme=readme.replace('URLs, hashes, origins and partial-contract markers','URLs, hashes and partial-contract markers').replace(' Hey API remains available as the retained comparison generator and baseline, outside this shipped package.','');
await writeFile('packages/typescript/README.md',readme);

await mkdir('release',{recursive:true});await writeFile('release/metadata.json',JSON.stringify(await identity(),null,2)+'\n');
