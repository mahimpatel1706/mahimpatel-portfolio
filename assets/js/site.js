(function () {
  'use strict';

  // Mobile navigation
  var btn = document.getElementById('mobile-menu-btn');
  var menu = document.getElementById('mobile-menu');
  if (btn && menu) {
    btn.addEventListener('click', function () {
      var isHidden = menu.classList.toggle('hidden');
      btn.setAttribute('aria-expanded', String(!isHidden));
    });
    menu.querySelectorAll('a, button').forEach(function (el) {
      el.addEventListener('click', function () {
        menu.classList.add('hidden');
        btn.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // Subtle elevation on the sticky nav once it docks to the top
  var nav = document.querySelector('.site-nav');
  if (nav) {
    var ticking = false;
    var update = function () {
      nav.classList.toggle('is-stuck', nav.getBoundingClientRect().top <= 0);
      ticking = false;
    };
    window.addEventListener('scroll', function () {
      if (!ticking) { window.requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
    update();
  }
})();

