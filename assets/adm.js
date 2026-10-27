// Bootstrap supplies navigation and scroll tracking; Pagefind supplies search.
const admBaseUrl = document.currentScript.dataset.baseUrl;
document.addEventListener('DOMContentLoaded', () => {
  new bootstrap.ScrollSpy(document.body, { target: '.bs-sidebar' });
  document.querySelectorAll('article table').forEach(table => {
    table.classList.add('table', 'table-striped', 'table-hover');
  });
  const dialog = document.getElementById('adm-search-dialog');
  const searchModal = bootstrap.Modal.getOrCreateInstance(dialog);
  dialog.addEventListener('shown.bs.modal', () => document.querySelector('#search input')?.focus());
  document.addEventListener('keydown', event => {
    if (event.key !== '/' || event.ctrlKey || event.metaKey || event.altKey ||
        event.target.closest('input, textarea, select, [contenteditable]')) return;
    event.preventDefault();
    searchModal.show();
  });
  if (window.PagefindUI) {
    new PagefindUI({ element: '#search', showSubResults: false,
      showImages: false, baseUrl: admBaseUrl, processResult: result => {
        const { kind, entry_id, ...meta } = result.meta;
        const label = document.createElement('span');
        label.className = 'adm-result-meta';
        label.textContent = [entry_id, kind].filter(Boolean).join(' · ');
        return { ...result, meta, excerpt: label.outerHTML + ' ' + result.excerpt };
      },
      translations: { placeholder: 'Search all ADM…', search_label: 'Search all ADM' } });
  }
});
