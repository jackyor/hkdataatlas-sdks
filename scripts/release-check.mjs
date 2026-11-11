import{execFileSync}from'node:child_process';import{readFile,readdir,writeFile,copyFile}from'node:fs/promises';import{createHash}from'node:crypto';
execFileSync(process.execPath,['scripts/verify-ci.mjs'],{stdio:'inherit'});
const config=JSON.parse(await readFile('sdk-config.json')),pkg=JSON.parse(await readFile('packages/typescript/package.json'));
if(process.env.GITHUB_REF!==`refs/tags/v${config.version}`)throw Error('Release tag must match configured package version.');
if(config.repository!==process.env.GITHUB_REPOSITORY||pkg.repository.url!==`git+https://github.com/${process.env.GITHUB_REPOSITORY}.git`)throw Error('Configure the final public GitHub repository identity before release.');
const python=await readFile('packages/python/pyproject.toml','utf8');if(!python.includes(`version = "${config.version}"`))throw Error('Python version mismatch');
await copyFile('scripts/npm-release.mjs','dist/npm-release.mjs');
const hashes=[createHash('sha256').update(await readFile('dist/npm-release.mjs')).digest('hex')+'  dist/npm-release.mjs'];for(const dir of['dist/typescript','dist/python'])for(const file of(await readdir(dir)).sort()){const path=`${dir}/${file}`;hashes.push(createHash('sha256').update(await readFile(path)).digest('hex')+'  '+path);}
await writeFile('dist/SHA256SUMS',hashes.join('\n')+'\n');
