(() => {
  const menu = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#site-nav');
  menu?.addEventListener('click', () => {
    const open = menu.getAttribute('aria-expanded') !== 'true';
    menu.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('is-open', open);
  });
  document.addEventListener('keydown', event => {
    if (event.key !== 'Escape') return;
    document.querySelectorAll('.nav-dropdown[open]').forEach(el => el.open = false);
    if (menu?.getAttribute('aria-expanded') === 'true') {
      menu.setAttribute('aria-expanded', 'false');
      nav.classList.remove('is-open');
      menu.focus();
    }
  });
  document.querySelectorAll('.nav-dropdown').forEach(dropdown => {
    dropdown.addEventListener('toggle', () => {
      if (dropdown.open) document.querySelectorAll('.nav-dropdown').forEach(other => {
        if (other !== dropdown) other.open = false;
      });
    });
  });
  document.addEventListener('click', event => {
    if (!event.target.closest('.site-header')) {
      document.querySelectorAll('.nav-dropdown[open]').forEach(el => el.open = false);
      menu?.setAttribute('aria-expanded', 'false');
      nav?.classList.remove('is-open');
    }
  });
  const video = document.querySelector('#hero-video');
  const toggle = document.querySelector('#video-toggle');
  if (!video || !toggle) return;
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  let loaded = false;
  function load() {
    if (loaded) return;
    video.querySelector('source').src = video.querySelector('source').dataset.src;
    video.load();
    loaded = true;
  }
  function update() {
    const playing = !video.paused;
    toggle.textContent = playing ? 'Pause video' : 'Play video';
    toggle.setAttribute('aria-label', playing ? 'Pause background video' : 'Play background video');
  }
  async function play() {
    load();
    video.muted = true;
    try { await video.play(); } catch { /* Poster remains visible when autoplay is unavailable. */ }
    update();
  }
  video.addEventListener('playing', update);
  video.addEventListener('pause', update);
  toggle.hidden = false;
  toggle.addEventListener('click', () => video.paused ? play() : video.pause());
  reduced.addEventListener('change', () => { if (reduced.matches) video.pause(); });
  if (!reduced.matches && !navigator.connection?.saveData) play();
})();
