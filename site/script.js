const toggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('#site-nav');

if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', String(!open));
    toggle.querySelector('span').textContent = open ? 'Menu' : 'Close';
    nav.classList.toggle('is-open', !open);
  });

  nav.addEventListener('click', event => {
    if (event.target.closest('a')) {
      toggle.setAttribute('aria-expanded', 'false');
      toggle.querySelector('span').textContent = 'Menu';
      nav.classList.remove('is-open');
    }
  });
}

document.querySelectorAll('[data-year]').forEach(item => {
  item.textContent = new Date().getFullYear();
});
