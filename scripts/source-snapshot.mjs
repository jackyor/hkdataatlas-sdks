import { readFile, readdir, lstat } from 'node:fs/promises';
import { createHash } from 'node:crypto';
// Keep host-copy filters aligned with the exact source identity below.
export const hostSourceExcludes = ['.git','.cache','**/.cache','**/.ruff_cache','node_modules','**/node_modules','.venv','**/.venv','**/__pycache__','**/*.pyc','**/dist','dist','reports','**/reports','openapi-ts-error-*.log','**/openapi-ts-error-*.log','experiments/*/.build','experiments/*/artifacts','experiments/**/.ruff_cache','experiments/*/.build-generation-output.json','experiments/**/*.log','experiments/hey-api-comparison/generated'];
function experimentBuildOutput(path) {
  const parts=path.replace(/^\.\//,'').split('/');
  return parts[0]==='experiments' && ((parts[1]==='hey-api-comparison'&&parts[2]==='generated') || parts.slice(2).includes('.ruff_cache') || (parts.length===3 && ['.build','artifacts','.ruff_cache','.build-generation-output.json'].includes(parts[2])) || path.endsWith('.log'));
}
export async function sourceSnapshot() {
  const exclude = new Set(['.git', '.venv', 'node_modules', '__pycache__', 'dist', 'reports', '.cache', '.ruff_cache']);
  const files = [];
  async function walk(root = '.') {
    for (const item of await readdir(root, { withFileTypes: true })) {
      if (exclude.has(item.name) || item.name.endsWith('.pyc') || item.name.startsWith('openapi-ts-error-')) continue;
      const path = `${root}/${item.name}`;
      if (experimentBuildOutput(path)) continue;
      if (item.isSymbolicLink()) throw new Error(`CI source must not contain symlinks: ${path}`);
      if (item.isDirectory()) await walk(path);
      else files.push({ path: path.slice(2), mode: (await lstat(path)).mode & 0o777, sha256: createHash('sha256').update(await readFile(path)).digest('hex') });
    }
  }
  await walk();
  files.sort((a,b) => a.path.localeCompare(b.path));
  return { sourceSha256: createHash('sha256').update(JSON.stringify(files)).digest('hex'), files };
}
