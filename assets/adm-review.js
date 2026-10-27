/* Cross-page export adapter for the pinned @reviewjs/annotate 1.5.3 store.
 * annotate.js owns annotation, persistence, and editing. We only read its
 * project store; native Download and Import remain single-page operations.
 */
(function (root, factory) {
  const api = factory();
  if (typeof module === 'object' && module.exports) module.exports = api;
  else {
    const start = () => api.mount(root);
    if (root.document.readyState === 'loading') root.document.addEventListener('DOMContentLoaded', start);
    else start();
  }
})(typeof window === 'undefined' ? null : window, function () {
  'use strict';
  const PROJECT = 'agent-diagnostic-manual';
  const VERSION = '1.5.3';
  const STORE_KEY = 'annotate:' + PROJECT;

  function collect(storage, currentComments, version, origin, now = new Date().toISOString()) {
    if (version !== VERSION) throw new Error('The review tool version changed. Use this page’s Download to preserve your comments.');
    let saved;
    try {
      const raw = storage.getItem(STORE_KEY);
      saved = raw === null ? { comments: [] } : JSON.parse(raw);
      if (!saved || !Array.isArray(saved.comments)) throw new Error('Invalid store');
    } catch (error) {
      throw new Error('Cannot read the saved site review. Nothing was changed. Use this page’s Download to preserve its comments.');
    }
    const comments = new Map();
    // The public API includes current-page comments whose storage write failed.
    // Keep newer persisted edits if another tab has updated the same comment.
    for (const comment of [...saved.comments, ...currentComments]) {
      if (!comment || typeof comment.id !== 'string' || typeof comment.page !== 'string') {
        throw new Error('Stored review data is damaged. Nothing was changed; export this page with its Download button.');
      }
      if (!comment.page.startsWith(PROJECT + ':')) continue;
      const previous = comments.get(comment.id);
      if (!previous || (comment.updatedAt || '') >= (previous.updatedAt || '')) comments.set(comment.id, comment);
    }
    const grouped = new Map();
    for (const comment of comments.values()) {
      if (!grouped.has(comment.page)) grouped.set(comment.page, []);
      grouped.get(comment.page).push(comment);
    }
    const pages = [...grouped].sort(([a], [b]) => a.localeCompare(b)).map(([page, items]) => {
      const key = page.slice(PROJECT.length + 1);
      return {
        annotate: VERSION, schema: 2, kind: 'annotate-export', exportedAt: now,
        project: PROJECT, page, url: items[0].url || '',
        entryId: /^[SDI]\d{3,}$/.test(key) ? key : null,
        document: /^[SDI]\d{3,}$/.test(key) ? null : key,
        comments: items,
      };
    });
    // Match upstream serialization: runtime-only keys never leave the browser.
    return JSON.parse(JSON.stringify({
      kind: 'adm-review-export', version: 1, project: PROJECT, annotate: VERSION,
      exportedAt: now, origin, pageCount: pages.length, commentCount: comments.size, pages,
    }, (key, value) => key.startsWith('__') ? undefined : value));
  }

  function mount(win) {
    const doc = win.document;
    const open = doc.getElementById('adm-review-open');
    const download = doc.getElementById('adm-review-export');
    const status = doc.getElementById('adm-review-status');
    if (!open || !download || !status) return;
    if (!win.Annotate) {
      status.textContent = 'Review tools could not load. Reload to try again.';
      return;
    }
    open.disabled = false;
    download.disabled = false;
    open.addEventListener('click', () => win.Annotate.open());
    download.addEventListener('click', () => {
      try {
        const payload = collect(win.localStorage, win.Annotate.comments(), win.Annotate.version, win.location.origin);
        if (!payload.commentCount) {
          status.textContent = 'No posted comments yet. Review a page and post a comment first.';
          return;
        }
        const blob = new win.Blob([JSON.stringify(payload, null, 2) + '\n'], { type: 'application/json' });
        const url = win.URL.createObjectURL(blob);
        const link = doc.createElement('a');
        link.href = url;
        link.download = 'adm-review-' + payload.exportedAt.slice(0, 10) + '.json';
        doc.body.appendChild(link);
        link.click();
        link.remove();
        win.setTimeout(() => win.URL.revokeObjectURL(url), 10000);
        status.textContent = `Exported ${payload.commentCount} comment${payload.commentCount === 1 ? '' : 's'} across ${payload.pageCount} page${payload.pageCount === 1 ? '' : 's'}. Send that JSON file when you’re ready. Comments remain saved here.`;
      } catch (error) {
        status.textContent = error.message || 'Export failed. Your saved comments have not been changed.';
      }
    });
  }
  return { collect, mount, PROJECT, VERSION, STORE_KEY };
});
