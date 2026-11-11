import { readFile } from 'node:fs/promises';
import { publishers, filesIn } from './lib/workspace.mjs';
// Preserved original source bodies are opaque publisher bytes, not public metadata.
const paths=[...(await filesIn('specs')).filter(p=>p.endsWith('.json')&&!p.endsWith('/openapi.json')&&!/^specs\/history\/[^/]+\/sources\//.test(p))];
paths.push('packages/typescript/sources.json','packages/python/src/hkdataatlas/sources.json');
for(const publisher of await publishers()) paths.push(`packages/python/src/hkdataatlas/${publisher.namespace}/sources.json`);
const failures=[];
const privateKeys=new Set(['associations','inventoryAssociations','datasetAssociations','inventorySourceIds','inventorySourceId','datasetId','resourceId','resourceIds']);
function inspect(value,path,location=''){
 if(typeof value==='string'&&/^\/(?:home|Users|tmp|root)\//.test(value))failures.push({path,location,reason:'absolute-environment-path'});
 if(Array.isArray(value))value.forEach((v,i)=>inspect(v,path,`${location}[${i}]`));
 else if(value&&typeof value==='object')for(const[k,v]of Object.entries(value)){
  if(privateKeys.has(k))failures.push({path,location:location?`${location}.${k}`:k,reason:'private-inventory-association'});
  inspect(v,path,location?`${location}.${k}`:k);
 }
}
for(const path of paths)inspect(JSON.parse(await readFile(path,'utf8')),path);
if(failures.length){console.error(JSON.stringify(failures,null,2));throw new Error(`${failures.length} public metadata privacy failures (matched values omitted).`);}
console.log(`Public metadata check passed: ${paths.length} files, no environment paths or private inventory association fields.`);
