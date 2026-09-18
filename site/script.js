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

const teamMembers = {
  'Rob Osman': { src: '/assets/team/rob-osman.png', width: 1024, height: 1536 },
  'Jack Henderson': { src: '/assets/team/jack-henderson.png', width: 1024, height: 1024 },
};
const teamCards = document.querySelectorAll('.team-grid .person');
if (teamCards.length) {
  const teamStyles = document.createElement('link');
  teamStyles.rel = 'stylesheet';
  teamStyles.href = '/team/team-images.css';
  document.head.append(teamStyles);

  teamCards.forEach(card => {
    const name = card.querySelector('h2')?.textContent.trim();
    const member = teamMembers[name];
    const currentVisual = card.querySelector('.avatar, .team-photo');
    if (!member || !currentVisual) return;

    const photo = document.createElement('img');
    photo.className = 'team-photo';
    photo.src = member.src;
    photo.alt = name;
    photo.width = member.width;
    photo.height = member.height;
    photo.loading = 'lazy';
    photo.decoding = 'async';
    currentVisual.replaceWith(photo);
  });
}
