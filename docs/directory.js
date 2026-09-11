(() => {
  'use strict';
  const form = document.querySelector('#filters');
  const search = document.querySelector('#search');
  const market = document.querySelector('#market');
  const mode = document.querySelector('#mode');
  const categorySelect = document.querySelector('#category-select');
  const buttons = [...document.querySelectorAll('.category')];
  const count = document.querySelector('#result-count');
  const reset = document.querySelector('#reset');
  const empty = document.querySelector('#empty');
  const projects = [...document.querySelectorAll('.project')].map(element => ({
    element, category: element.dataset.category,
    markets: JSON.parse(element.dataset.markets), modes: JSON.parse(element.dataset.modes),
    search: element.dataset.search.toLocaleLowerCase()
  }));
  let category = '';
  function update() {
    const words = search.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    let shown = 0;
    for (const project of projects) {
      const match = (!category || project.category === category)
        && (!market.value || project.markets.includes(market.value))
        && (!mode.value || (mode.value === 'unknown' ? !project.modes.length : project.modes.includes(mode.value)))
        && words.every(word => project.search.includes(word));
      project.element.hidden = !match;
      if (match) shown++;
    }
    count.textContent = `${shown} of ${projects.length} tools`;
    empty.hidden = shown !== 0;
    reset.hidden = !(words.length || category || market.value || mode.value);
    categorySelect.value = category;
    for (const button of buttons) {
      const active = button.dataset.category === category;
      button.setAttribute('aria-pressed', String(active));
      button.classList.toggle('active', active);
    }
  }
  function clear() {
    form.reset(); category = ''; update(); search.focus();
  }
  form.addEventListener('submit', event => event.preventDefault());
  search.addEventListener('input', update);
  market.addEventListener('change', update);
  mode.addEventListener('change', update);
  categorySelect.addEventListener('change', () => {category = categorySelect.value; update();});
  for (const button of buttons) button.addEventListener('click', () => {category = button.dataset.category; update();});
  reset.addEventListener('click', clear);
  document.querySelector('#empty-reset').addEventListener('click', clear);
  form.hidden = false;
  update();
})();
