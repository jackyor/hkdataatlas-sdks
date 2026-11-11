import {readFile,readdir,lstat} from 'node:fs/promises';
import {createHash} from 'node:crypto';
const excluded=new Set(['.git','.venv','node_modules','__pycache__','dist','reports','.cache','.ruff_cache']);
export const hostSourceExcludes=['.git','.venv','**/.venv','node_modules','**/node_modules','**/__pycache__','**/*.pyc','dist','**/dist','reports','**/reports','.cache','**/.cache','**/.ruff_cache'];
export async function sourceSnapshot(){
 const files=[];
 async function walk(root='.'){
  for(const item of await readdir(root,{withFileTypes:true})){
   if(excluded.has(item.name)||item.name.endsWith('.pyc'))continue;
   const path=`${root}/${item.name}`;
   if(item.isSymbolicLink())throw Error(`Package source must not contain symlinks: ${path}`);
   if(item.isDirectory())await walk(path);
   else files.push({path:path.slice(2),mode:(await lstat(path)).mode&0o777,sha256:createHash('sha256').update(await readFile(path)).digest('hex')});
  }
 }
 await walk();files.sort((a,b)=>a.path.localeCompare(b.path));return {sourceSha256:createHash('sha256').update(JSON.stringify(files)).digest('hex'),files};
}
