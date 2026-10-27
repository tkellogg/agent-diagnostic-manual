const test = require('node:test');
const assert = require('node:assert/strict');
const { collect, STORE_KEY, VERSION } = require('../website/assets/adm-review.js');
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
