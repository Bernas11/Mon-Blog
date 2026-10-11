document.addEventListener('DOMContentLoaded', () => {
  const faders = document.querySelectorAll('.fade-in');
  if ('IntersectionObserver' in window && window.matchMedia('(prefers-reduced-motion: no-preference)').matches) {
    const observer = new IntersectionObserver((entries, currentObserver) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          currentObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });
    faders.forEach((element) => observer.observe(element));
  } else {
    faders.forEach((element) => element.classList.add('visible'));
  }

  const slides = document.getElementById('slides');
  const previousButton = document.getElementById('prevBtn');
  const nextButton = document.getElementById('nextBtn');
  if (slides && previousButton && nextButton) {
    const images = slides.querySelectorAll('img');
    let index = 0;
    const showSlide = (nextIndex) => {
      if (!images.length) return;
      index = (nextIndex + images.length) % images.length;
      slides.style.transform = `translateX(${-index * 100}%)`;
    };
    previousButton.addEventListener('click', () => showSlide(index - 1));
    nextButton.addEventListener('click', () => showSlide(index + 1));
    // Sem avanço automático: o visitante controla o ritmo e a leitura das imagens.
    showSlide(0);
  }

  const sections = document.querySelectorAll('main section[id]');
  const navLinks = document.querySelectorAll('.nav-link');
  const updateActiveLink = () => {
    let current = '';
    sections.forEach((section) => {
      if (section.getBoundingClientRect().top <= 150) current = section.id;
    });
    navLinks.forEach((link) => {
      const active = link.getAttribute('href') === `#${current}`;
      if (active) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
  };
  window.addEventListener('scroll', updateActiveLink, { passive: true });
  updateActiveLink();
});
