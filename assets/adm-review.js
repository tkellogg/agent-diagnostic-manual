/* Cross-page review controls for the pinned @reviewjs/annotate 1.5.3 store.
 * annotate.js owns annotation and editing. ADM adds export and reversible
 * clearing across its project; native Download/Import/Clear are page-scoped.
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
  const BACKUP_KEY = STORE_KEY + ':last-clear';

  function readStore(storage) {
    const raw = storage.getItem(STORE_KEY);
    const saved = raw === null ? { comments: [] } : JSON.parse(raw);
    if (!saved || !Array.isArray(saved.comments)) throw new Error('Invalid store');
    return saved;
  }

  function collect(storage, currentComments, version, origin, now = new Date().toISOString()) {
    if (version !== VERSION) throw new Error('The review tool version changed. Use this page’s Download to preserve your comments.');
    let saved;
    try {
      saved = readStore(storage);
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

  function clearAll(storage, currentComments, version, origin, confirm, id) {
    let payload = collect(storage, currentComments, version, origin);
    if (!payload.commentCount) return null;
    if (!confirm(`Clear ${payload.commentCount} comments across ${payload.pageCount} pages in this browser?\n\nYou can undo this clear until the next clear. Unposted drafts in open ADM tabs will be discarded. Exported JSON files are unaffected.`)) return null;
    // Re-read after the dialog: another tab may have saved while it was open.
    payload = collect(storage, currentComments, version, origin);
    const saved = readStore(storage);
    const backup = { kind: 'adm-cleared-review', id, review: payload };
    // Never clear unless the recovery copy has been written successfully.
    storage.setItem(BACKUP_KEY, JSON.stringify(backup));
    storage.setItem(STORE_KEY, JSON.stringify({
      ...saved, comments: saved.comments.filter(c => !c.page.startsWith(PROJECT + ':')),
      admReset: id,
    }));
    return payload;
  }

  function lastClear(storage) {
    const raw = storage.getItem(BACKUP_KEY);
    if (raw === null) return null;
    const backup = JSON.parse(raw);
    if (backup.kind !== 'adm-cleared-review' || typeof backup.id !== 'string' ||
        backup.review?.kind !== 'adm-review-export' || backup.review.project !== PROJECT ||
        !Array.isArray(backup.review.pages)) throw new Error('Cannot read the last cleared review.');
    const saved = readStore(storage);
    // A failed clear or an already restored backup must not offer Undo.
    return saved.admReset === backup.id ? backup : null;
  }

  function undoClear(storage, currentComments, version, origin, id) {
    const backup = lastClear(storage);
    if (!backup) return null;
    const payload = collect(storage, currentComments, version, origin);
    const records = new Map(payload.pages.flatMap(p => p.comments).map(c => [c.id, c]));
    for (const comment of backup.review.pages.flatMap(p => p.comments)) {
      if (!comment || typeof comment.id !== 'string' || typeof comment.page !== 'string' ||
          !comment.page.startsWith(PROJECT + ':')) throw new Error('Cannot read the last cleared review.');
      // Work posted after the clear always wins on a conflicting ID.
      if (!records.has(comment.id)) records.set(comment.id, comment);
    }
    const saved = readStore(storage);
    storage.setItem(STORE_KEY, JSON.stringify({
      ...saved, comments: [...saved.comments.filter(c => !c.page.startsWith(PROJECT + ':')), ...records.values()],
      admReset: id,
    }));
    return backup.review;
  }

  function mount(win) {
    const doc = win.document;
    const template = doc.getElementById('adm-review-controls');
    if (!template || !win.Annotate) return;
    const controls = template.content.firstElementChild.cloneNode(true);
    const download = controls.querySelector('#adm-review-export');
    const clear = controls.querySelector('#adm-review-clear');
    const undo = controls.querySelector('#adm-review-undo');
    const status = controls.querySelector('#adm-review-status');
    const attachControls = () => {
      const footer = doc.getElementById('__an_foot');
      if (!footer) return;
      // The pinned annotate.js rebuilds the footer on every comment edit.
      // A sibling stays intact, including its listeners, focus and status.
      footer.before(controls);
      footer.setAttribute('role', 'group');
      footer.setAttribute('aria-label', 'This page');
      footer.classList.add('adm-review-page');
      for (const [oldLabel, label] of [
        ['Download comments as JSON', 'Download comments from this page as JSON'],
        ['Import comments from a JSON file', 'Import comments into this page from JSON'],
      ]) {
        const button = doc.querySelector(`#__an_panel .an-ph button[aria-label="${oldLabel}"]`);
        if (button) { button.setAttribute('aria-label', label); button.title = label; }
      }
    };
    attachControls();
    const updateUndo = () => {
      try { undo.hidden = !lastClear(win.localStorage); }
      catch (error) { undo.hidden = true; }
    };
    const resetLayer = () => {
      const wasOpen = doc.getElementById('__an_panel')?.classList.contains('an-open');
      const hadFocus = controls.contains(doc.activeElement);
      // Destroying also drops unsaved drafts and stale comment-edit forms.
      win.Annotate.destroy();
      win.Annotate.init();
      attachControls();
      updateUndo();
      // Keep the result and Undo in view after clearing from this panel.
      if (wasOpen) win.Annotate.open();
      if (hadFocus) (undo.hidden ? download : undo).focus();
    };
    const resetId = () => win.crypto.randomUUID();
    updateUndo();
    win.addEventListener('storage', event => {
      if (event.key === STORE_KEY) {
        try {
          const before = JSON.parse(event.oldValue || '{}').admReset;
          const after = JSON.parse(event.newValue || '{}').admReset;
          if (before !== after) {
            resetLayer();
            status.textContent = 'Comments were cleared or restored in another ADM tab.';
          }
        } catch (error) {
          status.textContent = 'Reload this page to refresh the review tools.';
        }
      }
      if (event.key === STORE_KEY || event.key === BACKUP_KEY) updateUndo();
    });
    clear.addEventListener('click', () => {
      try {
        const payload = clearAll(win.localStorage, win.Annotate.comments(), win.Annotate.version,
          win.location.origin, message => win.confirm(message), resetId());
        if (!payload) {
          status.textContent = 'No comments were cleared.';
          return;
        }
        resetLayer();
        status.textContent = `Cleared ${payload.commentCount} comments across ${payload.pageCount} pages. Undo clear restores them until the next clear.`;
      } catch (error) {
        updateUndo();
        status.textContent = 'Could not complete the clear. Saved comments or their recovery copy remain in this browser. Export your review before trying again.';
      }
    });
    undo.addEventListener('click', () => {
      try {
        const payload = undoClear(win.localStorage, win.Annotate.comments(), win.Annotate.version,
          win.location.origin, resetId());
        if (!payload) { updateUndo(); return; }
        resetLayer();
        status.textContent = `Restored ${payload.commentCount} comments across ${payload.pageCount} pages. New comments were kept too.`;
      } catch (error) {
        status.textContent = 'Could not restore comments. The recovery copy remains in this browser; free some storage and try again.';
      }
    });
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
  return { collect, clearAll, undoClear, lastClear, mount, PROJECT, VERSION, STORE_KEY, BACKUP_KEY };
});
