import {readFile}from'node:fs/promises';import{execFileSync}from'node:child_process';import{sourceSnapshot}from'./source-snapshot.mjs';import{treeHashes}from'./lib/workspace.mjs';
const receipt=JSON.parse(await readFile('reports/dagger.json'));
if(receipt.status!=='passed'||!receipt.sourceUnchanged||receipt.sourceCommit!==execFileSync('git',['rev-parse','HEAD'],{encoding:'utf8'}).trim()||receipt.sourceSha256!==(await sourceSnapshot()).sourceSha256)throw Error('Passing receipt does not bind the current committed source.');
const files=await treeHashes('dist');for(const[path,hash]of Object.entries(receipt.check.artifacts))if(files[path]!==hash)throw Error('Artifact changed:'+path);
console.log(`Verified source ${receipt.sourceCommit}, ${Object.keys(receipt.check.artifacts).length} checked artifacts; zero publication actions.`);
