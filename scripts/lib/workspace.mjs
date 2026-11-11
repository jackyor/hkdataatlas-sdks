import { readFile, readdir, mkdir, writeFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
export const digest = (value) => createHash('sha256').update(value).digest('hex');
export const snake = (value) => value.replace(/[^a-zA-Z0-9_]/g, '_').replace(/^([0-9])/, '_$1').toLowerCase();
export const camel = (value) => snake(value).replace(/_([a-z0-9])/g, (_, c) => c.toUpperCase()).replace(/^([0-9])/, '_$1');
export async function json(path) { return JSON.parse(await readFile(path, 'utf8')); }
export async function writeJson(path, value) { await writeFile(path, JSON.stringify(value, null, 2) + '\n'); }
export async function filesIn(root) {
  const result = [];
  async function walk(path) {
    for (const entry of await readdir(path, { withFileTypes: true })) {
      if (['__pycache__', '.ruff_cache', '.venv', 'dist', 'node_modules'].includes(entry.name) || entry.name.endsWith('.pyc')) continue;
      const current = `${path}/${entry.name}`;
      if (entry.isSymbolicLink()) throw new Error(`Unexpected symlink: ${current}`);
      if (entry.isDirectory()) await walk(current);
      else result.push(current);
    }
  }
  await walk(root);
  return result.sort();
}
export async function treeHashes(root) {
  return Object.fromEntries(await Promise.all((await filesIn(root)).map(async (path) => [path.slice(root.length + 1), digest(await readFile(path))])));
}
export async function publishers() {
  const manifest = await json('specs/manifest.json');
  if (manifest.version !== 2) throw new Error('Expected a finalized version2 specification manifest.');
  const groups = new Map();
  for (const entry of manifest.sources) {
    if (!/^[a-z][a-z0-9-]*$/.test(entry.publisherKey)) throw new Error(`Invalid publisher key ${entry.publisherKey}`);
    const family = snake(entry.familyKey);
    if (!/^[a-z_][a-z0-9_]*$/.test(family)) throw new Error(`Invalid family ${family}`);
    const source = { ...entry, family, jsonPath: `specs/${entry.json}`, yamlPath: `specs/${entry.yaml}` };
    let group = groups.get(entry.publisherKey);
    if (!group) { group = { key: entry.publisherKey, namespace: snake(entry.publisherKey), name: entry.publisherName, sources: [] }; groups.set(entry.publisherKey, group); }
    if (group.sources.some((item) => item.family === family)) throw new Error(`Duplicate family ${entry.publisherKey}/${family}`);
    group.sources.push(source);
  }
  return [...groups.values()].sort((a,b) => a.key.localeCompare(b.key));
}
export async function ensure(path) { await mkdir(path, { recursive: true }); }
export function packageRoots(publisher) {
  return { ts: 'packages/typescript', py: 'packages/python', tsPublisher: `packages/typescript/src/publishers/${publisher.key}`, pyPublisher: `packages/python/src/hkdataatlas/${publisher.namespace}`, tsDist: `packages/typescript/dist/publishers/${publisher.key}`, buildConfig: `reports/typescript/${publisher.key}/tsconfig.json`, pyModule: `hkdataatlas.${publisher.namespace}` };
}
