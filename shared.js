// Shared components for Majestic Cedar Cleaning
function renderTopBar() {
  return `
  <div class="topbar">
    <div class="container">
      <div class="topbar__inner">
        <div class="topbar__left">
          
        </div>
        <a href="contact.html" class="topbar__cta">Get a Quote</a>
      </div>
    </div>
  </div>`;
}

function renderNav(activePage) {
  const pages = [
    { href: 'index.html', label: 'Home' },
    { href: 'about.html', label: 'About' },
    { href: 'services.html', label: 'Services' },
    { href: 'sectors.html', label: 'Sectors' },
    { href: 'contact.html', label: 'Contact' },
  ];
  const links = pages.map(p => `
    <a href="${p.href}" class="nav__link${activePage === p.label ? ' active' : ''}">${p.label}</a>
  `).join('');
  return `
  <nav class="nav" id="mainNav">
    <div class="container">
      <div class="nav__inner">
        <a href="index.html" class="nav__logo">
          <img src="logo.webp" alt="Majestic Cedar Logo" style="height:36px;width:auto;border-radius:4px;">
          Majestic <span>Cedar</span>
        </a>
        <div class="nav__links">${links}</div>
        <div class="nav__cta">
          <a href="tel:08001234567" class="nav__phone">
            <svg width="15" height="15" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
            Call Us
          </a>
          <a href="contact.html" class="btn btn--gold">Get a Quote</a>
        </div>
        <button class="nav__hamburger" id="hamburger" aria-label="Menu">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
    <div class="nav__mobile" id="mobileNav" style="display:none;">
      <div class="container">
        ${pages.map(p => `<a href="${p.href}" class="nav__link">${p.label}</a>`).join('')}
        <a href="contact.html" class="btn btn--gold" style="margin-top:16px;width:100%;justify-content:center;">Get a Quote</a>
      </div>
    </div>
  </nav>`;
}

function renderFooter() {
  return `
  <footer class="footer">
    <div class="container">
      <div class="footer__grid">
        <div class="footer__brand">
          <div class="footer__logo">
            <img src="logo.webp" alt="Majestic Cedar Logo" style="height:32px;width:auto;border-radius:4px;">
            Majestic <span>Cedar</span>
          </div>
          <p class="footer__tagline">Professional cleaning services delivered with precision, care, and a commitment to excellence. Serving homes and businesses across the UK.</p>
          <div class="footer__social" style="display:flex; gap:16px; margin-top:24px;">
            <a href="#" style="color:var(--text-grey);"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg></a>
            <a href="#" style="color:var(--text-grey);"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
            <a href="#" style="color:var(--text-grey);"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg></a>
            <a href="#" style="color:var(--text-grey);"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg></a>
          </div>
        </div>
        <div>
          <p class="footer__heading">Services</p>
          <ul class="footer__links">
            <li><a href="residential.html" class="footer__link">Residential Cleaning</a></li>
            <li><a href="commercial.html" class="footer__link">Commercial Cleaning</a></li>
            <li><a href="deep-cleaning.html" class="footer__link">Deep Cleaning</a></li>
            <li><a href="end-of-tenancy.html" class="footer__link">End of Tenancy</a></li>
            <li><a href="after-builders.html" class="footer__link">After Builders</a></li>
            <li><a href="window-cleaning.html" class="footer__link">Window Cleaning</a></li>
          </ul>
        </div>
        <div>
          <p class="footer__heading">Company</p>
          <ul class="footer__links">
            <li><a href="about.html" class="footer__link">About Us</a></li>
            <li><a href="services.html" class="footer__link">Services</a></li>
            <li><a href="sectors.html" class="footer__link">Sectors</a></li>
            <li><a href="contact.html" class="footer__link">Contact</a></li>
            <li><a href="#" class="footer__link">Privacy Policy</a></li>
            <li><a href="#" class="footer__link">Terms of Service</a></li>
          </ul>
        </div>
        <div>
          <p class="footer__heading">Contact</p>
          <div class="footer__contact-item">
            <span class="footer__contact-icon"><svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-phone"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg></span>
            <span>0800 123 4567</span>
          </div>
          <div class="footer__contact-item">
            <span class="footer__contact-icon"><svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-mail"><rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg></span>
            <span>info@majesticcedarcleaning.co.uk</span>
          </div>
          <div class="footer__contact-item">
            <span class="footer__contact-icon"><svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-map-pin"><path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/></svg></span>
            <span>London, United Kingdom</span>
          </div>
        </div>
      </div>
    </div>
    <div style="border-top:1px solid rgba(255,255,255,0.07);">
      <div class="container">
        <div class="footer__bottom">
          <span>© 2024 Majestic Cedar Cleaning. All rights reserved.</span>
          <div class="footer__bottom-links">
            <a href="#" class="footer__bottom-link">Privacy Policy</a>
            <a href="#" class="footer__bottom-link">Terms</a>
            <a href="#" class="footer__bottom-link">Cookies</a>
          </div>
        </div>
      </div>
    </div>
  </footer>`;
}

function renderQuoteForm(title = 'Request a Free Quote') {
  return `
  <section class="section">
    <div class="container">
      <div class="text-center" style="margin-bottom:48px;">
        <span class="section-label">Free Quote</span>
        <h2 class="section-title">${title}</h2>
        <div class="gold-divider gold-divider--center"></div>
        <p class="section-subtitle">Fill in your details and we'll get back to you within 2 hours with a tailored quote.</p>
      </div>
      <div class="quote-form">
        <div class="form-grid">
          <div class="form-group">
            <label>First Name</label>
            <input type="text" placeholder="John">
          </div>
          <div class="form-group">
            <label>Last Name</label>
            <input type="text" placeholder="Smith">
          </div>
          <div class="form-group">
            <label>Email Address</label>
            <input type="email" placeholder="john@example.com">
          </div>
          <div class="form-group">
            <label>Phone Number</label>
            <input type="tel" placeholder="07700 000000">
          </div>
          <div class="form-group form-grid--full">
            <label>Service Required</label>
            <select>
              <option value="">Select a service...</option>
              <option>Residential Cleaning</option>
              <option>Commercial Cleaning</option>
              <option>Deep Cleaning</option>
              <option>End of Tenancy Cleaning</option>
              <option>After Builders Cleaning</option>
              <option>Window Cleaning</option>
            </select>
          </div>
          <div class="form-group form-grid--full">
            <label>Message</label>
            <textarea placeholder="Tell us more about your requirements..."></textarea>
          </div>
        </div>
        <div style="margin-top:24px;">
          <button class="btn btn--gold" style="width:100%;justify-content:center;padding:16px;" onclick="alert('Thank you! We\\'ll be in touch within 2 hours.')">
            Send Quote Request
            <svg width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path d="M13 7l5 5m0 0l-5 5m5-5H6"/></svg>
          </button>
        </div>
      </div>
    </div>
  </section>`;
}

function renderPageHero(title, subtitle, page, breadcrumb) {
  return `
  <section class="page-hero">
    <div class="container">
      <div class="page-hero__breadcrumb">
        <a href="index.html">Home</a> <span>›</span> ${breadcrumb || page}
      </div>
      <div class="section-label">${page}</div>
      <h1 class="page-hero__title">${title}</h1>
      <p class="page-hero__subtitle">${subtitle}</p>
    </div>
  </section>`;
}

function initShared() {
  // Sticky nav shadow
  const nav = document.getElementById('mainNav');
  if (nav) {
    window.addEventListener('scroll', () => {
      nav.classList.toggle('scrolled', window.scrollY > 20);
    });
  }
  // Mobile menu
  const hamburger = document.getElementById('hamburger');
  const mobileNav = document.getElementById('mobileNav');
  if (hamburger && mobileNav) {
    hamburger.addEventListener('click', () => {
      const isOpen = mobileNav.style.display !== 'none';
      mobileNav.style.display = isOpen ? 'none' : 'block';
    });
  }
  // FAQ toggles
  document.querySelectorAll('.faq__question').forEach(q => {
    q.addEventListener('click', () => {
      const item = q.closest('.faq__item');
      item.classList.toggle('open');
    });
  });
}
