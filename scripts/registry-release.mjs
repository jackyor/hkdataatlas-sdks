// Registry success means exact public archive bytes, never just a successful upload command.
import {createHash} from 'node:crypto';
import {readFile,writeFile,mkdir,appendFile,mkdtemp,rm} from 'node:fs/promises';
import {spawnSync} from 'node:child_process';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {pathToFileURL} from 'node:url';
const hash=bytes=>createHash('sha256').update(bytes).digest('hex');
export const intentName=(registry,manifest)=>`publication-intent-${registry}-${manifest.name}-${manifest.version}`;
const fail=message=>{throw Error(message);};
async function request(url,fetcher){return fetcher(url,{redirect:'error',headers:{accept:'application/json','cache-control':'no-cache'},signal:AbortSignal.timeout(30000)});}
export async function registryState(registry,manifest,{fetcher=fetch}={}){
 const artifacts=manifest.artifacts.filter(a=>a.registry===registry);
 if(!['npm','pypi'].includes(registry)||artifacts.length!==(registry==='npm'?1:2))fail('Unexpected registry or artifact count');
 const url=registry==='npm'?`https://registry.npmjs.org/${encodeURIComponent(manifest.name)}/${encodeURIComponent(manifest.version)}`:`https://pypi.org/pypi/${encodeURIComponent(manifest.name)}/${encodeURIComponent(manifest.version)}/json`;
 const response=await request(url+'?release_check='+Date.now(),fetcher);
 if(response.status===404)return {status:'missing',verified:[]};
 if(response.status!==200)fail(`Registry metadata unavailable (${response.status}); no submission is authorized`);
 const data=await response.json(),info=registry==='npm'?data:data.info;
 if(info?.name!==manifest.name||info?.version!==manifest.version)fail('Registry name/version mismatch');
 const available=registry==='npm'?[{filename:artifacts[0].filename,url:data.dist?.tarball,integrity:data.dist?.integrity}]:data.urls;
 if(!Array.isArray(available)||available.some(a=>!artifacts.some(e=>e.filename===a.filename)))fail('Unexpected registry file set');
 const verified=[];
 for(const expected of artifacts){
  const found=available.filter(a=>a.filename===expected.filename);
  if(found.length>1)fail('Duplicate registry archive metadata');
  if(!found.length)continue;
  const item=found[0],archiveUrl=new URL(item.url),host=registry==='npm'?'registry.npmjs.org':'files.pythonhosted.org';
  if(archiveUrl.protocol!=='https:'||archiveUrl.hostname!==host)fail('Unexpected registry archive host');
  if(item.digests?.sha256&&item.digests.sha256!==expected.sha256)fail('Existing registry archive has different bytes');
  if(item.integrity&&expected.integrity&&item.integrity!==expected.integrity)fail('Existing npm archive has different integrity');
  const archive=await request(archiveUrl.href,fetcher);
  if(archive.status!==200)fail(`Registry archive unavailable (${archive.status})`);
  const bytes=Buffer.from(await archive.arrayBuffer());
  if(bytes.length!==expected.bytes||hash(bytes)!==expected.sha256)fail('Existing registry archive has different bytes');
  verified.push({filename:expected.filename,sha256:expected.sha256,bytes:bytes.length,url:archiveUrl.href});
 }
 return {status:verified.length===artifacts.length?'verified':'partial',verified};
}
export async function pollRegistry(registry,manifest,{fetcher=fetch,sleep=ms=>new Promise(r=>setTimeout(r,ms)),maxAttempts=20,deadlineMs=600000,now=Date.now,onObservation=async()=>{},submissionFailed=false}={}){
 const start=now();
 for(let attempt=1;attempt<=maxAttempts;attempt++){
  const state=await registryState(registry,manifest,{fetcher});await onObservation({attempt,...state});
  if(state.status==='verified')return {status:'verified',attempts:attempt,archives:state.verified};
  if(submissionFailed)fail('Publisher failed and public archives are incomplete; reconcile before any new submission');
  if(attempt===maxAttempts||now()-start>=deadlineMs)break;
  await sleep(Math.min(45000,10000*2**Math.min(attempt-1,3),Math.max(0,deadlineMs-(now()-start))));
 }
 fail('Public registry validation remains pending; receipt retained, do not resubmit');
}
export async function priorPublicationIntents(registry,manifest,{fetcher=fetch,repository=process.env.GITHUB_REPOSITORY,token=process.env.GH_TOKEN}={}){
 if(repository!==manifest.repository||!token)fail('GitHub Actions identity/token required for publication-intent lookup');
 const response=await fetcher(`https://api.github.com/repos/${repository}/actions/artifacts?name=${encodeURIComponent(intentName(registry,manifest))}&per_page=100`,{redirect:'error',headers:{accept:'application/vnd.github+json',authorization:`Bearer ${token}`,'X-GitHub-Api-Version':'2026-03-10'},signal:AbortSignal.timeout(30000)});
 if(response.status!==200)fail(`Publication-intent lookup failed (${response.status}); no submission is authorized`);
 const body=await response.json();
 if(!Array.isArray(body.artifacts))fail('Invalid GitHub artifact response');
 return body.artifacts.map(a=>({id:a.id,expired:a.expired,runId:a.workflow_run?.id}));
}
export function publicationDecision(state,intents){
 if(state.status==='verified')return {publish:false,status:'already_public_identical'};
 if(state.status==='partial')fail('Only part of this version is public; reconcile instead of resubmitting');
 return intents.length?{publish:false,status:'prior_intent_reconcile_only'}:{publish:true,status:'new_submission'};
}
export function submissionReceipt(result,environment={}){
 const text=(result.stdout||'')+(result.stderr||'');
 return {status:result.status===0?'accepted_requires_public_verification':'failed_or_unknown',published:false,exitCode:result.status,errorCode:text.match(/\b(E[A-Z0-9_]+)\b/)?.[1],phase:text.includes('/oidc/token/exchange')?'oidc_exchange':'publisher',workflowRef:environment.GITHUB_WORKFLOW_REF,environment:'npm'};
}
async function save(registry,kind,value){await mkdir('dist/release-receipts',{recursive:true});await writeFile(`dist/release-receipts/${registry}-${kind}.json`,JSON.stringify(value,null,2)+'\n');}
async function checkedManifest(){
 const manifest=JSON.parse(await readFile('dist/release-manifest.json'));
 if(manifest.schemaVersion!==1||manifest.name!=='hkdataatlas')fail('Unexpected release manifest');
 for(const a of manifest.artifacts){const bytes=await readFile(a.path);if(bytes.length!==a.bytes||hash(bytes)!==a.sha256)fail('Release artifact changed after checks');}
 return manifest;
}
async function main(){
 const [mode,registry]=process.argv.slice(2),manifest=await checkedManifest();
 if(!['npm','pypi'].includes(registry))fail('Choose npm or pypi');
 if(mode==='prepare'){
  const state=await registryState(registry,manifest),intents=state.status==='verified'?[]:await priorPublicationIntents(registry,manifest),decision=publicationDecision(state,intents);
  const plan={...decision,registry,name:manifest.name,version:manifest.version,sourceCommit:manifest.sourceCommit,artifactHashes:manifest.artifacts.filter(a=>a.registry===registry).map(a=>a.sha256),priorIntents:intents,runId:process.env.GITHUB_RUN_ID,runAttempt:process.env.GITHUB_RUN_ATTEMPT};
  await save(registry,'plan',plan);
  if(decision.publish)await save(registry,'intent',plan);
  if(process.env.GITHUB_OUTPUT)await appendFile(process.env.GITHUB_OUTPUT,`publish=${decision.publish}\nintent_name=${intentName(registry,manifest)}\n`);
  console.log(JSON.stringify(plan));return;
 }
 if(mode==='submit'&&registry==='npm'){
  const plan=JSON.parse(await readFile('dist/release-receipts/npm-plan.json'));
  if(!plan.publish||plan.runId!==process.env.GITHUB_RUN_ID||plan.runAttempt!==process.env.GITHUB_RUN_ATTEMPT)fail('No current publication intent authorizes submission');
  const artifact=manifest.artifacts.find(a=>a.registry==='npm');await save(registry,'submission',{status:'started',published:false,sourceCommit:manifest.sourceCommit});
  const temporary=await mkdtemp(join(tmpdir(),'hkdataatlas-oidc-'));let result;
  try{
   const config=join(temporary,'npmrc'),globalConfig=join(temporary,'global-npmrc');await writeFile(config,'registry=https://registry.npmjs.org/\n',{mode:0o600});await writeFile(globalConfig,'',{mode:0o600});
   const environment={...process.env,NPM_CONFIG_USERCONFIG:config,NPM_CONFIG_GLOBALCONFIG:globalConfig};delete environment.NPM_TOKEN;delete environment.NODE_AUTH_TOKEN;
   result=spawnSync('npm',['publish',artifact.path,'--access','public','--provenance','--ignore-scripts'],{env:environment,encoding:'utf8',maxBuffer:16*1024*1024,timeout:180000});
  }finally{await rm(temporary,{recursive:true,force:true});}
  const receipt={...submissionReceipt(result,process.env),sourceCommit:manifest.sourceCommit};
  await save(registry,'submission',receipt);console.log(JSON.stringify(receipt));if(result.status!==0)fail('npm submission failed; diagnostics redacted and reconciliation required');return;
 }
 if(mode==='verify'){
  const observations=[];try{
   const result=await pollRegistry(registry,manifest,{submissionFailed:process.env.SUBMISSION_OUTCOME==='failure',onObservation:async observation=>{observations.push(observation);await save(registry,'verification',{status:'pending',published:false,sourceCommit:manifest.sourceCommit,observations});}});
   await save(registry,'verification',{...result,published:true,sourceCommit:manifest.sourceCommit,observations});console.log(JSON.stringify(result));
  }catch(error){await save(registry,'verification',{status:'failed_or_pending',published:false,sourceCommit:manifest.sourceCommit,error:error.message,observations});throw error;}return;
 }
 fail('Choose prepare, submit npm, or verify');
}
if(process.argv[1]&&import.meta.url===pathToFileURL(process.argv[1]).href)main().catch(error=>{console.error(error.message);process.exitCode=1;});
