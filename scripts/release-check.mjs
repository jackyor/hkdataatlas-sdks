import{execFileSync}from'node:child_process';
import{readFile,readdir,writeFile,copyFile}from'node:fs/promises';
import{createHash}from'node:crypto';
execFileSync(process.execPath,['scripts/verify-ci.mjs'],{stdio:'inherit'});
const config=JSON.parse(await readFile('sdk-config.json')),pkg=JSON.parse(await readFile('packages/typescript/package.json')),receipt=JSON.parse(await readFile('reports/dagger.json'));
if(process.env.GITHUB_REF!==`refs/tags/v${config.version}`)throw Error('Release tag must match configured package version.');
if(config.repository!==process.env.GITHUB_REPOSITORY||pkg.repository.url!==`git+https://github.com/${process.env.GITHUB_REPOSITORY}.git`)throw Error('Configure the final public GitHub repository identity before release.');
const python=await readFile('packages/python/pyproject.toml','utf8');
if(!python.includes(`version = "${config.version}"`)||pkg.version!==config.version||pkg.name!==config.python.name)throw Error('Package name/version mismatch');
const artifacts=[];
for(const[registry,dir,expected]of[['npm','typescript',[`${pkg.name}-${config.version}.tgz`]],['pypi','python',[`${pkg.name}-${config.version}-py3-none-any.whl`,`${pkg.name}-${config.version}.tar.gz`]]]){
 const files=(await readdir(`dist/${dir}`)).sort();if(JSON.stringify(files)!==JSON.stringify(expected.sort()))throw Error('Unexpected release archive set');
 for(const filename of files){const path=`dist/${dir}/${filename}`,bytes=await readFile(path),sha256=createHash('sha256').update(bytes).digest('hex');if(receipt.check.artifacts[`${dir}/${filename}`]!==sha256)throw Error('Archive does not match exact source receipt');artifacts.push({registry,filename,path,bytes:bytes.length,sha256,...(registry==='npm'?{integrity:'sha512-'+createHash('sha512').update(bytes).digest('base64')}:{})});}
}
await copyFile('scripts/registry-release.mjs','dist/registry-release.mjs');
await writeFile('dist/release-manifest.json',JSON.stringify({schemaVersion:1,name:pkg.name,version:config.version,repository:config.repository,sourceCommit:receipt.sourceCommit,sourceSha256:receipt.sourceSha256,artifacts},null,2)+'\n');
const files=['dist/registry-release.mjs','dist/release-manifest.json',...artifacts.map(a=>a.path)];
await writeFile('dist/SHA256SUMS',(await Promise.all(files.map(async path=>createHash('sha256').update(await readFile(path)).digest('hex')+'  '+path))).join('\n')+'\n');
