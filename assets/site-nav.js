/* ============================================================
   Shared site nav: hamburger toggle behaviour.
   Injects a toggle button into .nav-inner and a full-screen
   overlay menu (.nav-mobile) cloned from the existing
   .nav-link items. Pairs with /assets/site-nav.css.
   ============================================================ */

(function () {
  function init() {
    const navInner = document.querySelector('.nav .nav-inner');
    if (!navInner) return;

    // Avoid double-init if loaded twice
    if (navInner.querySelector('.nav-toggle')) return;

    // Build the hamburger button
    const toggle = document.createElement('button');
    toggle.className = 'nav-toggle';
    toggle.type = 'button';
    toggle.setAttribute('aria-label', 'Open menu');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-controls', 'nav-mobile');
    toggle.innerHTML = '<span></span><span></span><span></span>';

    // Place inside .nav-right if present, else append to .nav-inner
    const navRight = navInner.querySelector('.nav-right');
    if (navRight) {
      navRight.appendChild(toggle);
    } else {
      navInner.appendChild(toggle);
    }

    // Build the mobile overlay menu by cloning every .nav-link
    const overlay = document.createElement('div');
    overlay.className = 'nav-mobile';
    overlay.id = 'nav-mobile';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');
    overlay.setAttribute('aria-label', 'Site menu');
    overlay.hidden = false; // controlled by .is-open class

    const links = navInner.querySelectorAll('.nav-link');
    links.forEach((orig) => {
      const a = document.createElement('a');
      a.href = orig.getAttribute('href') || '#';
      a.textContent = orig.textContent;
      if (orig.classList.contains('active')) a.classList.add('active');
      if (orig.target) a.target = orig.target;
      if (orig.rel) a.rel = orig.rel;
      a.addEventListener('click', close);
      overlay.appendChild(a);
    });

    // Optional footer line
    const footer = document.createElement('div');
    footer.className = 'nav-mobile-footer';
    footer.textContent = 'compost.fi · public data, on-chain';
    overlay.appendChild(footer);

    document.body.appendChild(overlay);

    function open() {
      toggle.classList.add('is-open');
      overlay.classList.add('is-open');
      document.body.classList.add('nav-locked');
      toggle.setAttribute('aria-expanded', 'true');
      toggle.setAttribute('aria-label', 'Close menu');
    }

    function close() {
      toggle.classList.remove('is-open');
      overlay.classList.remove('is-open');
      document.body.classList.remove('nav-locked');
      toggle.setAttribute('aria-expanded', 'false');
      toggle.setAttribute('aria-label', 'Open menu');
    }

    function toggleMenu(e) {
      e.preventDefault();
      if (overlay.classList.contains('is-open')) close();
      else open();
    }

    toggle.addEventListener('click', toggleMenu);

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && overlay.classList.contains('is-open')) close();
    });

    // Close overlay if the viewport grows back past the breakpoint
    const mq = window.matchMedia('(min-width: 761px)');
    const onChange = (ev) => { if (ev.matches) close(); };
    if (mq.addEventListener) mq.addEventListener('change', onChange);
    else mq.addListener(onChange);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
