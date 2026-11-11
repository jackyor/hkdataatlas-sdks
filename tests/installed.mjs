import {execFileSync}from'node:child_process';import{mkdtemp,mkdir,writeFile,readdir,rm,readFile}from'node:fs/promises';import{tmpdir}from'node:os';import{join,resolve}from'node:path';import{publishers}from'../scripts/lib/workspace.mjs';
const temp=await mkdtemp(join(tmpdir(),'hkdataatlas-public-npm-'));try{
const tarballs=(await readdir('dist/typescript')).filter(p=>p.endsWith('.tgz'));if(tarballs.length!==1)throw Error('Expected one npm package');
await writeFile(join(temp,'package.json'),'{"private":true,"type":"module"}\n');
execFileSync('bun',['add','--ignore-scripts',resolve('dist/typescript',tarballs[0])],{cwd:temp,stdio:'inherit'});
const parkingFixture=JSON.parse(await readFile('tests/fixtures/carpark-without-opening-hours.json'));
const groups=await publishers(),code=groups.map(p=>`await import('hkdataatlas/${p.key}');`).join('\n')+groups.flatMap(p=>p.sources.map(s=>`await import(${JSON.stringify('file://'+join(temp,'node_modules/hkdataatlas/dist/publishers',p.key,s.family,'index.js'))});`)).join('\n')+`
import assert from 'node:assert/strict';
const {banksBranchLocator}=await import('hkdataatlas/hkma');
const seen=[];const fakeFetch=async(input,init)=>{seen.push(new Request(input,init));return new Response(JSON.stringify({header:{success:true},result:{datasize:0,records:[]}}),{status:200,headers:{'Content-Type':'application/json'}});};
const response=await banksBranchLocator.getBanksBranchLocator({lang:'en',pagesize:1},{},fakeFetch);
assert.equal(response.status,200);assert.equal(response.data.header.success,true);assert.equal(new URL(seen[0].url).searchParams.get('pagesize'),'1');
await assert.rejects(import('hkdataatlas/publishers/hkma'),{code:'ERR_PACKAGE_PATH_NOT_EXPORTED'});
`;
await writeFile(join(temp,'verify.mjs'),code);execFileSync(process.execPath,[join(temp,'verify.mjs')],{stdio:'inherit'});
await writeFile(join(temp,'consumer.ts'),`import {banksBranchLocator} from 'hkdataatlas/hkma';\nconst call=()=>banksBranchLocator.getBanksBranchLocator({lang:'en',pagesize:1});\n// @ts-expect-error invalid language must not typecheck\nconst invalid=()=>banksBranchLocator.getBanksBranchLocator({lang:'xx'});\nvoid call;void invalid;\nimport {parkingVacancyDataApi} from 'hkdataatlas/dpo';\nconst optionalOpeningHours: parkingVacancyDataApi.CarparkInfo = ${JSON.stringify(parkingFixture)};\nvoid optionalOpeningHours;\n`);
execFileSync(process.execPath,['node_modules/typescript/bin/tsc','--noEmit','--strict','--skipLibCheck','--target','ES2022','--module','NodeNext','--moduleResolution','NodeNext',join(temp,'consumer.ts')],{stdio:'inherit'});
console.log(`Installed npm: ${groups.length} publishers and ${groups.reduce((n,p)=>n+p.sources.length,0)} family imports, typed HKMA example and one synthetic response passed.`);
}finally{await rm(temp,{recursive:true,force:true});}
