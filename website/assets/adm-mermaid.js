// Render ordinary fenced Mermaid blocks; leave the Markdown source untouched.
const diagrams = [...document.querySelectorAll('article pre > code.language-mermaid')].map((code, index) => ({
  source: code.textContent,
  pre: code.parentElement,
  id: `adm-mermaid-${index}`,
  figure: null,
  error: null,
}));

function showSource(diagram) {
  diagram.figure?.remove();
  diagram.figure = null;
  diagram.pre.hidden = false;
  if (!diagram.error) {
    diagram.error = document.createElement('p');
    diagram.error.className = 'adm-diagram-error';
    diagram.error.setAttribute('role', 'status');
    diagram.error.textContent = 'The diagram could not be rendered. Its Mermaid source is shown below.';
    diagram.pre.before(diagram.error);
  }
}

if (diagrams.length) {
  try {
    // Load the full v12 bundle only on pages with diagrams. It includes ELK.
    const { default: mermaid } = await import('./vendor/mermaid-12.2.0/mermaid.esm.min.mjs');
    await document.fonts.ready;
    let queue = Promise.resolve();
    let revision = 0;
    function render() {
      const requested = ++revision;
      queue = queue.then(async () => {
        if (requested !== revision) return;
        const styles = getComputedStyle(document.documentElement);
        const color = name => styles.getPropertyValue(`--adm-${name}`).trim();
        mermaid.initialize({
          startOnLoad: false,
          securityLevel: 'strict',
          theme: 'base',
          fontFamily: getComputedStyle(document.body).fontFamily,
          themeVariables: {
            darkMode: document.documentElement.dataset.bsTheme === 'dark',
            background: color('paper'),
            primaryColor: color('surface'),
            primaryTextColor: color('ink'),
            primaryBorderColor: color('accent'),
            secondaryColor: color('hover'),
            tertiaryColor: color('paper'),
            lineColor: color('muted'),
            textColor: color('ink'),
            clusterBkg: color('surface'),
            clusterBorder: color('line'),
            edgeLabelBackground: color('paper'),
          },
        });
        for (const diagram of diagrams) {
          try {
            if (!diagram.figure) {
              diagram.figure = document.createElement('figure');
              diagram.figure.className = 'adm-diagram';
              diagram.pre.before(diagram.figure);
            }
            const { svg, bindFunctions } = await mermaid.render(diagram.id, diagram.source, diagram.figure);
            diagram.figure.innerHTML = svg;
            bindFunctions?.(diagram.figure);
            diagram.pre.hidden = true;
            diagram.error?.remove();
            diagram.error = null;
          } catch (error) {
            showSource(diagram);
            console.error('ADM Mermaid rendering failed:', error);
          }
        }
        window.bootstrap?.ScrollSpy.getInstance(document.body)?.refresh();
      });
      return queue;
    }
    await render();
    new MutationObserver(render).observe(document.documentElement, {
      attributes: true, attributeFilter: ['data-bs-theme'],
    });
  } catch (error) {
    diagrams.forEach(showSource);
    console.error('ADM Mermaid loading failed:', error);
  }
}
