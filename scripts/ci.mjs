// Build from a clean committed export, never ignored build output from a checkout.
import {execFileSync,spawnSync} from 'node:child_process';
import {mkdtemp,mkdir,rm,writeFile,readFile} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join,resolve} from 'node:path';
import {sourceSnapshot,hostSourceExcludes} from './source-snapshot.mjs';
if(!execFileSync('dagger',['version'],{encoding:'utf8'}).includes('v1.0.0-beta.21'))throw Error('Pinned Dagger v1.0.0-beta.21 is required.');
if(execFileSync('git',['status','--porcelain','--untracked-files=normal'],{encoding:'utf8'}).trim())throw Error('Commit the intended public source before running source-bound release checks.');
const sourceCommit=execFileSync('git',['rev-parse','HEAD'],{encoding:'utf8'}).trim(),snapshot=await sourceSnapshot(),temporary=await mkdtemp(join(tmpdir(),'hkdataatlas-public-source-'));
const startedAt=new Date().toISOString(),at=Date.now();await mkdir('reports',{recursive:true});
try{
 const archive=execFileSync('git',['archive','--format=tar',sourceCommit],{maxBuffer:1024*1024*1024});
 execFileSync('tar',['-xf','-','-C',temporary],{input:archive});
 const args=['api','call','--engine=image://registry.dagger.io/engine:v1.0.0-beta.21','--progress=plain','-M','host','directory',`--path=${temporary}`,'--exclude='+hostSourceExcludes.join(','),'docker-build','--dockerfile=ci/Dockerfile','with-mounted-cache','--path=/work/.cache','--cache=hkdataatlas-public-sdk-ci-v1','--sharing=LOCKED','with-env-variable','--name=SDK_CHECK_RUN','--value='+startedAt,'with-exec','--args=node,scripts/check.mjs','directory','--path=/work/dist','export','--path='+resolve('dist')];
 await rm('dist',{recursive:true,force:true});
 const result=spawnSync('dagger',args,{encoding:'utf8',maxBuffer:128*1024*1024,env:{...process.env,DAGGER_NO_NAG:'1'}});process.stdout.write(result.stdout||'');process.stderr.write(result.stderr||'');await writeFile('reports/dagger.log',(result.stdout||'')+(result.stderr||''));
 const after=await sourceSnapshot(),unchanged=after.sourceSha256===snapshot.sourceSha256;let check;if(result.status===0)check=JSON.parse(await readFile('dist/check.json'));
 const receipt={kind:'public-sdk-source-bound-dagger',status:result.status===0&&unchanged?'passed':'failed',sourceCommit,sourceSha256:snapshot.sourceSha256,files:snapshot.files,sourceUnchanged:unchanged,startedAt,completedAt:new Date().toISOString(),durationMs:Date.now()-at,engine:'image://registry.dagger.io/engine:v1.0.0-beta.21',exitCode:result.status,check,limitations:['Offline packaging/source checks only. Zero publisher requests. No registry publication or hosted status is implied by this local receipt.']};
 await writeFile('reports/dagger.json',JSON.stringify(receipt,null,2)+'\n');if(result.error)throw result.error;if(receipt.status!=='passed')process.exitCode=1;
}finally{await rm(temporary,{recursive:true,force:true});}
