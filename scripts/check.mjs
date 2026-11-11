import {spawnSync} from 'node:child_process';
import {readFile,writeFile,mkdir,rm,cp} from 'node:fs/promises';
import {resolve} from 'node:path';
import {publishers,packageRoots,digest,filesIn,treeHashes,json,writeJson} from './lib/workspace.mjs';
const run=(cmd,args,options={})=>{const r=spawnSync(cmd,args,{stdio:'inherit',...options});if(r.error)throw r.error;if(r.status)throw Error(`${cmd} exited ${r.status}`);};
const started=Date.now();run(process.execPath,['--test','tests/registry-release.test.mjs']);run(process.execPath,['tests/final-products.mjs']);run(process.execPath,['scripts/public-metadata-check.mjs']);

const groups=await publishers(),compiler=digest(await readFile('bun.lock'));await mkdir('.cache/public/compiled',{recursive:true});await rm('packages/typescript/dist',{recursive:true,force:true});await mkdir('packages/typescript/dist',{recursive:true});
let executed=0,reused=0,index=0;
// Each independent publisher compiles once. Cached output is reused only after input and output hash verification.
const {spawn}=await import('node:child_process');
await Promise.all(Array.from({length:3},async()=>{while(index<groups.length){const p=groups[index++],r=packageRoots(p);await mkdir(`reports/typescript/${p.key}`,{recursive:true});await writeJson(r.buildConfig,{extends:resolve('packages/typescript/tsconfig.json'),include:[resolve(r.tsPublisher,'**/*.ts')]});const cache=`.cache/public/compiled/${p.key}`,receipt=`.cache/public/compiled/${p.key}.json`,key=digest(JSON.stringify({compiler,source:await treeHashes(r.tsPublisher),config:await readFile('packages/typescript/tsconfig.json','utf8'),publisherConfig:await readFile(r.buildConfig,'utf8')}));let old;try{old=await json(receipt);}catch{}
 let intact=false;if(old?.key===key)try{intact=JSON.stringify(await treeHashes(cache))===JSON.stringify(old.files);}catch{}
 if(intact){await cp(cache,r.tsDist,{recursive:true});reused++;continue;}
 await new Promise((ok,no)=>{const c=spawn(process.execPath,['node_modules/typescript/bin/tsc','-p',r.buildConfig],{stdio:'inherit'});c.on('error',no);c.on('exit',code=>code?no(Error(`TypeScript ${p.key} failed`)):ok());});
 await rm(cache,{recursive:true,force:true});await cp(r.tsDist,cache,{recursive:true});await writeJson(receipt,{key,files:await treeHashes(cache)});executed++;
}}));
run(process.execPath,['scripts/build-entrypoints.mjs']);await rm('dist',{recursive:true,force:true});await mkdir('dist/typescript',{recursive:true});await mkdir('dist/python',{recursive:true});
run('bun',['pm','pack','--destination',resolve('dist/typescript'),'--quiet'],{cwd:'packages/typescript'});
run('uv',['build','packages/python','--out-dir','dist/python','--no-build-isolation','--python',resolve('.venv/bin/python')]);
await rm('dist/python/.gitignore',{force:true});
run(process.execPath,['tests/installed.mjs']);
run('uv',['run','--frozen','python','tests/installed.py']);
run('uv',['build',(await filesIn('dist/python')).find(p=>p.endsWith('.tar.gz')),'--wheel','--out-dir','dist/rebuilt','--no-build-isolation','--python',resolve('.venv/bin/python')]);
run('uv',['run','--frozen','python','tests/archive-parity.py']);
const artifacts=Object.fromEntries(Object.entries(await treeHashes('dist')).filter(([p])=>!p.startsWith('rebuilt/')));
await writeJson('dist/check.json',{schemaVersion:1,status:'passed',families:groups.reduce((n,p)=>n+p.sources.length,0),publisherModules:groups.length,typescriptCompilations:{executed,reused},npmPackages:1,pythonDistributions:1,publisherRequests:0,artifacts,durationMs:Date.now()-started,checks:['release orchestration fake-registry tests','final product metadata and JSON/YAML hashes','canonical JSON/YAML hashes and semantic parity','all publisher TypeScript compilations','one npm tarball, one wheel and one sdist','installed npm and wheel imports for all publishers and families','synthetic sync/async Python and TypeScript response calls','independent synthetic response schema check','wheel/sdist rebuilt file parity'],limitations:['Package builds and synthetic consumer checks do not establish universal live API correctness.']});
