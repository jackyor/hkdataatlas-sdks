// Public generation records bind retained outputs to exact public generator inputs.
import {execFileSync} from 'node:child_process';
import {readFile,rm} from 'node:fs/promises';
import {Worker} from 'node:worker_threads';
import {parse} from 'yaml';
import {isDeepStrictEqual} from 'node:util';
import {publishers,packageRoots,digest,filesIn,treeHashes,json,writeJson,ensure} from './lib/workspace.mjs';
const check=process.argv.includes('--check'),adopt=process.argv.includes('--adopt-export-baseline'),force=process.argv.includes('--force'),selection=process.argv.find(x=>x.startsWith('--source='))?.slice(9);
if(Number(process.versions.node.split('.')[0])<22||process.versions.bun)throw Error('Run generation with Node.js 22+.');
if(adopt){if(!process.env.SDK_PRIVATE_SOURCE)throw Error('Export baseline adoption is limited to the allowlist exporter.');execFileSync(process.execPath,['scripts/generate.mjs','--check'],{cwd:process.env.SDK_PRIVATE_SOURCE,stdio:'pipe',maxBuffer:32*1024*1024});}
const groups=await publishers(),legacy=new Map((await json('scripts/legacy/native-fetch-v1/sources.json')).sources.map(s=>[s.id,s.jsonSha256]));
const generatorFiles=['scripts/lib/workspace.mjs','package.json','bun.lock','pyproject.toml','uv.lock','scripts/generate.mjs','scripts/generate-worker.mjs','scripts/orval-config.mjs','scripts/legacy/native-fetch-v1/orval-config.mjs',...(await filesIn('packages/python/tools')).filter(p=>!p.endsWith('/check.py'))];
const configHash=digest(JSON.stringify(await Promise.all(generatorFiles.map(async p=>[p,digest(await readFile(p))]))));
let prior={records:[]};try{prior=await json('release/generation.json');}catch{}
const records=new Map(prior.records.map(r=>[r.id,r])),next=[],jobs=[];
for(const p of groups)for(const s of p.sources){
 const raw=await readFile(s.jsonPath),yaml=await readFile(s.yamlPath);
 if(digest(raw)!==s.jsonSha256||digest(yaml)!==s.yamlSha256||!isDeepStrictEqual(JSON.parse(raw),parse(yaml.toString())))throw Error('Canonical JSON/YAML mismatch:'+s.id);
 const roots=packageRoots(p),tsOutput=`${roots.tsPublisher}/${s.family}`,pyOutput=`${roots.pyPublisher}/${s.familyKey.replace(/[^a-zA-Z0-9_]/g,'_').toLowerCase()}`,key=digest(JSON.stringify({source:s.jsonSha256,yaml:s.yamlSha256,configHash,legacy:legacy.get(s.id)===s.jsonSha256}));
 const typescript=await treeHashes(tsOutput),python=await treeHashes(pyOutput),old=records.get(s.id);
 const intact=!(force&&(!selection||selection===s.id))&&old?.key===key&&isDeepStrictEqual(old.typescript,typescript)&&isDeepStrictEqual(old.python,python);
 if(adopt||intact)next.push({id:s.id,key,sourceSha256:s.jsonSha256,typescript,python});
 else if(check)throw Error('Generation is stale or output was changed:'+s.id);
 else jobs.push({id:s.id,publisher:p.key,input:s.jsonPath,tsOutput,pyOutput,key,legacy:legacy.get(s.id)===s.jsonSha256});
}
if(jobs.length){
 await ensure('reports');let index=0;
 await Promise.all(Array.from({length:Math.min(4,jobs.length)},()=>new Promise((resolve,reject)=>{
  const worker=new Worker(new URL('./generate-worker.mjs',import.meta.url));worker.on('error',reject);
  const advance=()=>{if(index<jobs.length)worker.postMessage(jobs[index++]);else worker.terminate().then(resolve);};
  worker.on('message',result=>{if(result.results.some(r=>r.status!=='generated')){worker.terminate();reject(Error(JSON.stringify(result)));}else advance();});advance();
 })));
 await writeJson('reports/regenerate-families.json',jobs.map(j=>j.id));
 if(force)for(const job of jobs)await rm(`packages/python/.generation/${job.id}.json`,{force:true});
 execFileSync('uv',['run','--frozen','python','scripts/generate-python.py','reports/regenerate-families.json'],{stdio:'inherit'});
 for(const job of jobs)next.push({id:job.id,key:job.key,sourceSha256:JSON.parse(await readFile(job.input))&&digest(await readFile(job.input)),typescript:await treeHashes(job.tsOutput),python:await treeHashes(job.pyOutput)});
}
if(!check){await ensure('release');await writeJson('release/generation.json',{schemaVersion:1,generators:{typescript:'orval@8.47.0',python:'openapi-python-client@0.30.0'},configHash,baseline:adopt?'retained canonical generation verified before public export':'source-bound generation records',records:next.sort((a,b)=>a.id.localeCompare(b.id))});if(!adopt)execFileSync(process.execPath,['scripts/metadata.mjs'],{stdio:'inherit'});}
console.log(`Generation ${check?'verified':adopt?'exported':'completed'}: ${next.length} families; ${jobs.length} regenerated; zero publisher requests.`);
