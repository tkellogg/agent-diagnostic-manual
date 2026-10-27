// Bootstrap supplies navigation and scroll tracking; Pagefind supplies search.
const admBaseUrl = document.currentScript.dataset.baseUrl;
document.addEventListener('DOMContentLoaded', () => {
  new bootstrap.ScrollSpy(document.body, { target: '.bs-sidebar' });
  document.querySelectorAll('article table').forEach(table => {
    table.classList.add('table', 'table-striped', 'table-hover');
  });
  if (window.PagefindUI) {
    new PagefindUI({ element: '#search', showSubResults: false,
      showImages: false, baseUrl: admBaseUrl, focusOnSlash: true,
      translations: { placeholder: 'Search the manual…', search_label: 'Search the manual' } });
  }
});
