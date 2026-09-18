const toggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('#site-nav');
if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const open = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', String(!open));
    toggle.textContent = open ? 'Menu' : 'Close';
    nav.classList.toggle('open', !open);
  });
  nav.addEventListener('click', () => { toggle.setAttribute('aria-expanded', 'false'); toggle.textContent = 'Menu'; nav.classList.remove('open'); });
}
document.querySelectorAll('[data-year]').forEach(el => { el.textContent = new Date().getFullYear(); });

const form = document.querySelector('[data-enquiry-form]');
if (form) {
  form.addEventListener('submit', event => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const data = new FormData(form);
    const subject = `Stump’d enquiry — ${data.get('enquiry-type')}`;
    const body = [`Name: ${data.get('name')}`, `Email: ${data.get('email')}`, `Organisation: ${data.get('organisation') || 'Not provided'}`, `Enquiry: ${data.get('enquiry-type')}`, '', data.get('message')].join('\n');
    window.location.href = `mailto:hello@stumpd.co.uk?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    const status = form.querySelector('.form-status');
    status.textContent = 'Your email app should now open with your enquiry ready to send.';
  });
}

// The Spark card artwork is portrait. Correct older card-page markup that
// declared it as landscape and ensure the complete artwork remains visible.
document.querySelectorAll('.spark-card-grid img').forEach(card => {
  card.width = 1024;
  card.height = 1536;
  card.style.width = '100%';
  card.style.height = 'auto';
  card.style.maxHeight = 'none';
  card.style.objectFit = 'contain';
});
