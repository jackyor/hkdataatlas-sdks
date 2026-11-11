import { generate } from 'orval';
import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { join } from 'node:path';
import { digest } from './lib/workspace.mjs';
const methods=new Set(['get','post','put','patch','delete','head','options','trace']);
// These generator-only representations preserve validation semantics and all
// original annotations. Canonical source bytes are never rewritten.
export function normalizeOrvalInput(original) {
 const spec=structuredClone(original),changes=[];
 function schemas(value,path='$') {
  if(!value||typeof value!=='object')return;
  if(Array.isArray(value)){value.forEach((v,i)=>schemas(v,`${path}/${i}`));return;}
  for(const[k,v]of Object.entries(value))schemas(v,`${path}/${k}`);
  if(value.type==='object'&&value.properties&&value.anyOf?.length&&value.anyOf.every(b=>b&&Object.keys(b).every(k=>k==='required')&&Array.isArray(b.required))){
   const {anyOf,...parent}=value;
   const variants=anyOf.map(branch=>({...structuredClone(parent),required:[...new Set([...(parent.required??[]),...branch.required])]}));
   for(const key of Object.keys(value))delete value[key];
   value.anyOf=variants;changes.push({path,rule:'distribute-required-only-anyOf',proof:'A AND (B OR C) = (A AND B) OR (A AND C); full parent constraints and annotations retained in each branch'});
  }
 }
 schemas(spec);
 const effectiveServers=Object.entries(spec.paths??{}).flatMap(([,item])=>Object.entries(item).filter(([method])=>methods.has(method)).map(([,op])=>op.servers??item.servers??spec.servers));
 if(effectiveServers.length&&effectiveServers.every(servers=>servers?.length&&JSON.stringify(servers)===JSON.stringify(effectiveServers[0]))&&JSON.stringify(spec.servers)!==JSON.stringify(effectiveServers[0])){
  spec.servers=structuredClone(effectiveServers[0]);changes.push({path:'$/servers',rule:'promote-identical-effective-operation-servers',proof:'Every operation has this identical effective server list, including operation/path overrides. Root fallback is changed without changing any effective operation server.'});
 }else if(!spec.servers)throw Error('Root server fallback requires identical explicit effective servers for every operation');
 for(const[path,item]of Object.entries(spec.paths??{}))for(const[method,operation]of Object.entries(item))if(methods.has(method)){
  for(const [status,response]of Object.entries(operation.responses??{}))for(const [mediaType,media]of Object.entries(response.content??{}))if(/^(?:text\/|application\/(?:xml|[^;]+\+xml)(?:;|$))/i.test(mediaType)&&media.schema){
   const schema=media.schema,raw=schema.type==='string'&&!schema.$ref;if(!raw){media.schema={type:'string',description:'Raw native text; the canonical logical XML model is retained in the original specification and component schemas.'};changes.push({path:`$/paths/${path}/${method}/responses/${status}/content/${mediaType}`,rule:'text-media-raw-wire-response',sourceSchema:schema,proof:'Native fetch exposes XML/text as text without a decoder; raw wire type is string. Canonical logical response model and source constraints remain unchanged in the preserved specification.'});}
  }
  for(const parameter of [...(item.parameters??[]),...(operation.parameters??[])])if(parameter.in==='query'&&parameter.required===true&&parameter.schema&&Object.hasOwn(parameter.schema,'default')){
   parameter.schema={allOf:[parameter.schema]};changes.push({path:`$/paths/${path}/${method}/parameters/${parameter.name}`,rule:'required-default-allOf',proof:'A schema S and allOf:[S] accept the same instances and preserve the default annotation; prevents default metadata from weakening mandatory query presence'});
  }
 }
 return {spec,changes};
}
export function operations(spec) {
 return Object.entries(spec.paths??{}).flatMap(([path,item])=>Object.entries(item).filter(([method])=>methods.has(method)).map(([method,operation])=>({method:method.toUpperCase(),path,operationId:operation.operationId??null})));
}
export async function generateOrval(job) {
 const bytes=await readFile(job.input),original=JSON.parse(bytes),{spec,changes}=normalizeOrvalInput(original);
 await mkdir(job.tsOutput,{recursive:true});
 await generate({input:{target:spec},output:{target:join(job.tsOutput,'index.ts'),client:'fetch',mode:'single',headers:true,allParamsOptional:false,baseUrl:{getBaseUrlFromSpecification:true},urlEncodeParameters:true,operationManifest:{types:false},override:{fetch:{useRuntimeFetcher:true}}}},process.cwd(),{throwOnError:true,failOnWarnings:true});
 await writeFile(join(job.tsOutput,'generation.json'),JSON.stringify({generator:'orval',version:'8.47.0',sourceId:job.id,sourceSha256:digest(bytes),originalOperations:operations(original),normalizations:changes},null,2)+'\n');
 return {language:'typescript',status:'generated',operations:operations(original).length,normalizations:changes};
}
