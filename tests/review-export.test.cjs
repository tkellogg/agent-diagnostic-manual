const test = require('node:test');
const assert = require('node:assert/strict');
const { collect, clearAll, undoClear, lastClear, STORE_KEY, BACKUP_KEY, VERSION } = require('../website/assets/adm-review.js');
const record = (id, page, extra = {}) => ({
  schema: 2, id, page: 'agent-diagnostic-manual:' + page,
  url: 'https://diag.timkellogg.me/' + page, type: 'highlight', author: 'Reviewer',
  text: 'Clarify this.', anchor: { exact: 'A working explanation', prefix: 'Keep ', suffix: ' provisional.' },
  replies: [{ id: 'reply-' + id, text: 'An additional thought.', author: 'Reviewer' }],
  createdAt: '2026-10-27T10:00:00Z', updatedAt: '2026-10-27T10:00:00Z', ...extra,
});
const storage = comments => ({ getItem(key) { assert.equal(key, STORE_KEY); return JSON.stringify({ comments }); } });
const exportReview = (store, current = []) => collect(store, current, VERSION, 'https://diag.timkellogg.me', '2026-10-27T12:00:00Z');

test('one export retains separate pages, anchors, replies, and resolved comments', () => {
  const first = record('c1', 'D001');
  const second = record('c2', 'docs/authoring-symptom.md', { resolved: true, status: 'resolved' });
  const data = exportReview(storage([first, second]), [first]);
  assert.equal(data.kind, 'adm-review-export');
  assert.equal(data.commentCount, 2);
  assert.equal(data.pageCount, 2);
  assert.equal(data.comments, undefined); // Native import must not flatten a batch onto the current page.
  const diagnosis = data.pages.find(page => page.entryId === 'D001');
  assert.deepEqual(diagnosis.comments, [first]);
  assert.equal(diagnosis.kind, 'annotate-export');
  const guide = data.pages.find(page => page.document === 'docs/authoring-symptom.md');
  assert.deepEqual(guide.comments, [second]);
});

test('includes current-page work even if its storage write failed', () => {
  const old = record('c1', 'S001');
  const edited = { ...old, text: 'Updated comment', updatedAt: '2026-10-27T11:00:00Z' };
  const unsaved = record('c3', 'S001');
  const data = exportReview(storage([old, record('c2', 'D001')]), [edited, unsaved]);
  assert.equal(data.commentCount, 3);
  assert.equal(data.pages.find(page => page.entryId === 'S001').comments.find(c => c.id === 'c1').text, 'Updated comment');
});

test('does not overwrite a newer edit saved by another tab', () => {
  const stale = record('c1', 'S001');
  const newer = { ...stale, text: 'Newer edit', updatedAt: '2026-10-27T11:00:00Z' };
  assert.equal(exportReview(storage([newer]), [stale]).pages[0].comments[0].text, 'Newer edit');
});

test('isolates this project and removes only runtime keys', () => {
  const c = record('c1', 'S001', { __node: { cannotExport: true }, history: [{ text: 'Original text' }] });
  const other = record('c2', 'D001', { page: 'unrelated-project:D001' });
  const data = exportReview(storage([c, other]));
  assert.equal(data.commentCount, 1);
  assert.equal(data.pages[0].comments[0].__node, undefined);
  assert.deepEqual(data.pages[0].comments[0].history, c.history);
  assert.ok(c.__node); // Export never edits the store or in-memory comments.
});

test('reports unavailable or corrupt storage rather than silently exporting a partial review', () => {
  for (const store of [
    { getItem() { throw new Error('Denied'); } },
    { getItem() { return '{'; } },
    { getItem() { return '{}'; } },
    storage([null]),
  ]) assert.throws(() => exportReview(store, [record('c1', 'S001')]), /Nothing was changed/);
});

test('empty reviews are empty and unsupported upstream versions fail explicitly', () => {
  assert.equal(exportReview({ getItem() { return null; } }).commentCount, 0);
  assert.throws(() => collect(storage([]), [], '2.0.0', 'https://diag.timkellogg.me'), /version changed/);
});

function writableStorage(comments) {
  const values = new Map([[STORE_KEY, JSON.stringify({comments, unrelatedSetting: 'keep'})], ['another-project', 'untouched']]);
  return { values, getItem(key) { return values.get(key) ?? null; }, setItem(key, value) { values.set(key, value); } };
}
const clearReview = (store, current = [], confirm = () => true, id = 'clear-1') =>
  clearAll(store, current, VERSION, 'https://diag.timkellogg.me', confirm, id);
const restoreReview = (store, current = [], id = 'restore-1') =>
  undoClear(store, current, VERSION, 'https://diag.timkellogg.me', id);

test('clear requires confirmation and cancellation changes nothing', () => {
  const store = writableStorage([record('c1', 'D001'), record('c2', 'S001')]);
  const before = [...store.values];
  assert.equal(clearReview(store, [], message => {
    assert.match(message, /2 comments across 2 pages/);
    return false;
  }), null);
  assert.deepEqual([...store.values], before);
  let asked = false;
  assert.equal(clearReview(writableStorage([]), [], () => { asked = true; }), null);
  assert.equal(asked, false);
});

test('clear saves all ADM comments before removing only this project, including unsaved posted work', () => {
  const foreign = record('other', 'S001', {page:'other-project:S001'});
  const first = record('c1', 'D001', {resolved:true, status:'resolved'});
  const second = record('c2', 'S001');
  const unsaved = record('c3', 'S003');
  const store = writableStorage([first, second, foreign]);
  clearReview(store, [unsaved]);
  assert.equal(exportReview(store).commentCount, 0);
  assert.deepEqual(JSON.parse(store.getItem(STORE_KEY)).comments, [foreign]);
  assert.equal(JSON.parse(store.getItem(STORE_KEY)).unrelatedSetting, 'keep');
  assert.equal(store.getItem('another-project'), 'untouched');
  const backup = lastClear(store);
  assert.equal(backup.review.commentCount, 3);
  assert.deepEqual(backup.review.pages.find(p => p.entryId === 'D001').comments, [first]);
});

test('undo works after navigation, retains new comments and does not replace newer work', () => {
  const old = record('c1', 'D001');
  const store = writableStorage([old, record('c2', 'S001')]);
  clearReview(store);
  const saved = JSON.parse(store.getItem(STORE_KEY));
  const edited = {...old, text:'New text after clearing'};
  const fresh = record('c3', 'S003');
  store.setItem(STORE_KEY, JSON.stringify({...saved, comments:[edited, fresh]}));
  const reloadedStore = {getItem:key => store.getItem(key), setItem:(key, value) => store.setItem(key, value)};
  assert.ok(lastClear(reloadedStore));
  restoreReview(reloadedStore);
  const restored = exportReview(store);
  assert.equal(restored.commentCount, 3);
  assert.equal(restored.pages.find(p => p.entryId === 'D001').comments[0].text, edited.text);
  assert.equal(lastClear(store), null);
  assert.equal(restoreReview(store), null); // An old backup cannot undo twice.
});

test('a second clear replaces the single recoverable round', () => {
  const store = writableStorage([record('old', 'D001')]);
  clearReview(store);
  const saved = JSON.parse(store.getItem(STORE_KEY));
  store.setItem(STORE_KEY, JSON.stringify({...saved, comments:[record('new', 'S001')]}));
  clearReview(store, [], () => true, 'clear-2');
  restoreReview(store);
  assert.deepEqual(exportReview(store).pages.flatMap(p => p.comments.map(c => c.id)), ['new']);
});

test('backup failure or damaged data prevents a clear', () => {
  const store = writableStorage([record('c1', 'D001')]);
  const before = store.getItem(STORE_KEY);
  const limited = {...store, setItem(key, value) {
    if (key === BACKUP_KEY) throw new Error('Quota');
    store.setItem(key, value);
  }};
  assert.throws(() => clearReview(limited), /Quota/);
  assert.equal(store.getItem(STORE_KEY), before);
  store.setItem(STORE_KEY, '{');
  assert.throws(() => clearReview(store), /Nothing was changed/);
  assert.equal(store.getItem(STORE_KEY), '{');
});

test('failed store writes leave the active review and recovery copy intact', () => {
  const store = writableStorage([record('c1', 'D001')]);
  const limited = {...store, setItem(key, value) {
    if (key === STORE_KEY) throw new Error('Denied');
    store.setItem(key, value);
  }};
  assert.throws(() => clearReview(limited), /Denied/);
  assert.equal(exportReview(store).commentCount, 1);
  assert.equal(lastClear(store), null);
  assert.ok(store.getItem(BACKUP_KEY));
  clearReview(store);
  assert.throws(() => restoreReview(limited), /Denied/);
  assert.equal(exportReview(store).commentCount, 0);
  assert.ok(lastClear(store));
});

test('comments saved by another tab during confirmation are included in the recovery copy', () => {
  const store = writableStorage([record('c1', 'D001')]);
  clearReview(store, [], () => {
    const saved = JSON.parse(store.getItem(STORE_KEY));
    saved.comments.push(record('c2', 'S001'));
    store.setItem(STORE_KEY, JSON.stringify(saved));
    return true;
  });
  assert.equal(lastClear(store).review.commentCount, 2);
});
