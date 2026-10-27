// Bootstrap supplies navigation and scroll tracking; Pagefind supplies search.
const admBaseUrl = document.currentScript.dataset.baseUrl;
document.addEventListener('DOMContentLoaded', () => {
  new bootstrap.ScrollSpy(document.body, { target: '.bs-sidebar' });
  document.querySelectorAll('article table').forEach(table => {
    table.classList.add('table', 'table-striped', 'table-hover');
  });
  if (window.PagefindUI) {
    new PagefindUI({ element: '#search', showSubResults: true,
      showImages: false, baseUrl: admBaseUrl });
  }
  document.addEventListener('keydown', event => {
    if (event.ctrlKey || event.metaKey || event.altKey ||
        event.target.closest('input, textarea, select, [contenteditable="true"]')) return;
    if (event.key === '/') {
      event.preventDefault();
      document.querySelector('.adm-search').open = true;
      document.querySelector('#search input')?.focus();
    }
  });
});
