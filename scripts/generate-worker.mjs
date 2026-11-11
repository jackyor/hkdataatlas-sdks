import { parentPort } from 'node:worker_threads';
import { generateOrval } from './orval-config.mjs';
import { generateOrval as legacyGenerateOrval } from './legacy/native-fetch-v1/orval-config.mjs';
parentPort.on('message',async job=>{
 const startedAt=Date.now();let result;
 try{result=await (job.legacy?legacyGenerateOrval:generateOrval)(job);}catch(error){result={language:'typescript',status:'generator-failed',message:String(error?.stack||error)};}
 parentPort.postMessage({id:job.id,results:[result],durationMs:Date.now()-startedAt});
});
