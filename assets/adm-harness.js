// Filter only implementation notes; the shared intervention remains visible.
(() => {
  const select = document.getElementById('adm-harness-select');
  if (!select) return;
  const notes = [...document.querySelectorAll('.adm-harness-note')];
  const status = document.getElementById('adm-harness-status');
  const key = 'adm:harness';
  const available = value => value === 'all' || notes.some(note => note.dataset.harness === value);
  function apply(value, unavailable = false) {
    select.value = available(value) ? value : 'all';
    notes.forEach(note => { note.hidden = select.value !== 'all' && note.dataset.harness !== select.value; });
    status.textContent = unavailable
      ? 'Your saved harness has no specific notes here. Showing all harnesses.'
      : 'Shared instructions above apply to every harness. Your choice is remembered in this browser.';
    bootstrap.ScrollSpy.getInstance(document.body)?.refresh();
  }
  let saved = 'all';
  try { saved = localStorage.getItem(key) || 'all'; } catch (_) { /* Selection still works without storage. */ }
  apply(saved, !available(saved));
  select.closest('.adm-harness-controls').hidden = false;
  select.addEventListener('change', () => {
    apply(select.value);
    try { localStorage.setItem(key, select.value); } catch (_) {
      status.textContent = 'Showing your selection. This browser could not remember it.';
    }
  });
  function revealLinkedNote() {
    let target;
    try { target = document.getElementById(decodeURIComponent(location.hash.slice(1))); } catch (_) { return; }
    const note = target?.closest('.adm-harness-note');
    if (note) {
      apply(note.dataset.harness);
      target.scrollIntoView();
    }
  }
  window.addEventListener('hashchange', revealLinkedNote);
  revealLinkedNote();
})();
