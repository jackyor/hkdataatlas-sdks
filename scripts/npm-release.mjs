// Initial interactive bootstrap and OIDC releases may address the same immutable version.
// Reuse is permitted only when registry tarball integrity equals the checked local bytes.
import {execFileSync,spawnSync}from'node:child_process';
import{readdir,readFile}from'node:fs/promises';
import{createHash}from'node:crypto';
import{resolve}from'node:path';
const paths=(await readdir('dist/typescript')).filter(p=>p.endsWith('.tgz'));if(paths.length!==1)throw Error('Expected exactly one checked npm tarball.');
const tarball=resolve('dist/typescript',paths[0]),pkg=JSON.parse(execFileSync('tar',['-xOf',tarball,'package/package.json'],{encoding:'utf8'}));
const integrity='sha512-'+createHash('sha512').update(await readFile(tarball)).digest('base64');
const response=await fetch(`https://registry.npmjs.org/${encodeURIComponent(pkg.name)}/${encodeURIComponent(pkg.version)}`,{signal:AbortSignal.timeout(30000)});
if(response.status===200){const version=await response.json();if(version.dist?.integrity!==integrity)throw Error('This npm version already exists with different bytes. Choose a new version; it cannot be overwritten.');console.log(JSON.stringify({name:pkg.name,version:pkg.version,status:'already_published_identical_tarball',published:false}));}
else if(response.status===404){if(process.argv.includes('--check-only'))console.log(JSON.stringify({name:pkg.name,version:pkg.version,status:'version_not_present',published:false,packagePublishPermission:'not_established'}));else{const result=spawnSync('npm',['publish',tarball,'--access','public','--provenance'],{stdio:'inherit'});if(result.error)throw result.error;if(result.status)process.exit(result.status);}}
else throw Error(`Registry metadata read failed (${response.status}); publication was not attempted.`);
