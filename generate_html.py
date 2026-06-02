import os

def generate_page(filename, title, active_nav, body_content):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>{title} — Majestic Cedar Cleaning</title>
  <link rel="stylesheet" href="styles.css">
  <script src="shared.js"></script>
</head>
<body>
  <div id="header-placeholder"></div>

{body_content}

  <div id="footer-placeholder"></div>
  <script>
    document.getElementById('header-placeholder').outerHTML = renderTopBar() + renderNav('{active_nav}');
    document.getElementById('footer-placeholder').outerHTML = renderFooter();
    initShared();
  </script>
</body>
</html>"""
    with open(filename, 'w') as f:
        f.write(html)

index_body = """<section class="hero">
  <div class="hero__image"></div>
  <div class="container">
    <div class="hero__content">
      <div class="hero__badge">Premium Cleaning Services</div>
      <h1 class="hero__title">Your Space, <em>Perfectly</em><br>Cleaned.</h1>
      <p class="hero__subtitle">Majestic Cedar Cleaning delivers exceptional residential and commercial cleaning services with unmatched attention to detail. Trusted by thousands across the UK.</p>
      <div class="hero__actions">
        <a href="tel:08001234567" class="btn btn--gold">Call Us</a>
        <a href="contact.html" class="btn btn--outline">Get a Quote</a>
      </div>
    </div>
  </div>
</section>
<section class="trust">
  <div class="container">
    <div class="trust__inner">
      <div class="trust__item"><div class="trust__icon">✓</div><div><div class="trust__title">100% Satisfaction</div><div class="trust__desc">Guaranteed on every clean</div></div></div>
      <div class="trust__item"><div class="trust__icon">🛡</div><div><div class="trust__title">Trusted Experts</div><div class="trust__desc">Fully vetted & insured staff</div></div></div>
      <div class="trust__item"><div class="trust__icon">📋</div><div><div class="trust__title">Transparent Booking</div><div class="trust__desc">No hidden fees, ever</div></div></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="text-center" style="margin-bottom:56px;">
      <span class="section-label">What We Offer</span>
      <h2 class="section-title">Our Cleaning Services</h2>
      <div class="gold-divider gold-divider--center"></div>
      <p class="section-subtitle">From routine home cleans to specialist commercial services, we have the expertise and equipment to handle it all.</p>
    </div>
    <div class="services-grid">
      <div class="service-card">
        <img src="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=600&q=80" alt="Residential Cleaning" class="service-card__img">
        <span class="service-card__icon">🏠</span>
        <h3 class="service-card__title">Residential Cleaning</h3>
        <p class="service-card__desc">Regular and one-off home cleaning tailored to your schedule and specific needs.</p>
        <a href="residential.html" class="service-card__link">Learn More →</a>
      </div>
      <div class="service-card">
        <img src="https://images.unsplash.com/photo-1497366216548-37526070297c?w=600&q=80" alt="Commercial Cleaning" class="service-card__img">
        <span class="service-card__icon">🏢</span>
        <h3 class="service-card__title">Commercial Cleaning</h3>
        <p class="service-card__desc">Professional office and business cleaning to maintain a pristine working environment.</p>
        <a href="commercial.html" class="service-card__link">Learn More →</a>
      </div>
      <div class="service-card">
        <img src="https://images.unsplash.com/photo-1527515637462-cff94eecc1ac?w=600&q=80" alt="Deep Cleaning" class="service-card__img">
        <span class="service-card__icon">✨</span>
        <h3 class="service-card__title">Deep Cleaning</h3>
        <p class="service-card__desc">A thorough, top-to-bottom clean reaching every corner and surface of your property.</p>
        <a href="deep-cleaning.html" class="service-card__link">Learn More →</a>
      </div>
      <div class="service-card">
        <img src="https://images.unsplash.com/photo-1600585152220-90363fe7e115?w=600&q=80" alt="End of Tenancy" class="service-card__img">
        <span class="service-card__icon">🔑</span>
        <h3 class="service-card__title">End of Tenancy</h3>
        <p class="service-card__desc">Comprehensive cleaning to secure your deposit return and meet landlord requirements.</p>
        <a href="end-of-tenancy.html" class="service-card__link">Learn More →</a>
      </div>
    </div>
    <div class="text-center" style="margin-top:40px;">
      <a href="services.html" class="btn btn--outline">View All Services</a>
    </div>
  </div>
</section>
<section class="section section--grey">
  <div class="container">
    <div class="text-center" style="margin-bottom:56px;">
      <span class="section-label">Simple Process</span>
      <h2 class="section-title">How It Works</h2>
      <div class="gold-divider gold-divider--center"></div>
    </div>
    <div class="how-it-works__steps">
      <div class="step">
        <div class="step__number">1</div>
        <h3 class="step__title">Request a Quote</h3>
        <p class="step__desc">Fill in our simple form or call us. We'll provide a transparent, no-obligation quote within 2 hours.</p>
      </div>
      <div class="step">
        <div class="step__number">2</div>
        <h3 class="step__title">We Clean</h3>
        <p class="step__desc">Our expert team arrives on time, fully equipped, and delivers a meticulous, professional clean.</p>
      </div>
      <div class="step">
        <div class="step__number">3</div>
        <h3 class="step__title">Sign Off</h3>
        <p class="step__desc">Inspect the results together. We're not done until you're 100% satisfied with every area cleaned.</p>
      </div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="text-center" style="margin-bottom:56px;">
      <span class="section-label">Client Reviews</span>
      <h2 class="section-title">What Our Clients Say</h2>
      <div class="gold-divider gold-divider--center"></div>
    </div>
    <div class="testimonials-grid">
      <div class="testimonial-card"><div class="testimonial-card__quote">"</div>
        <div class="testimonial-card__stars">★★★★★</div>
        <p class="testimonial-card__text">Absolutely brilliant service. The team was punctual, thorough and left our home spotless. Will definitely be booking again.</p>
        <div class="testimonial-card__author">Sarah M.</div><div class="testimonial-card__role">Residential Client, London</div>
      </div>
      <div class="testimonial-card"><div class="testimonial-card__quote">"</div>
        <div class="testimonial-card__stars">★★★★★</div>
        <p class="testimonial-card__text">Used Majestic Cedar for our end of tenancy clean. Got our full deposit back thanks to the incredible job they did.</p>
        <div class="testimonial-card__author">James T.</div><div class="testimonial-card__role">Tenant, Manchester</div>
      </div>
      <div class="testimonial-card"><div class="testimonial-card__quote">"</div>
        <div class="testimonial-card__stars">★★★★★</div>
        <p class="testimonial-card__text">Our office has never looked better. The commercial team is professional, discreet and incredibly detail-oriented.</p>
        <div class="testimonial-card__author">Rebecca L.</div><div class="testimonial-card__role">Office Manager, Birmingham</div>
      </div>
    </div>
  </div>
</section>
<section class="coverage">
  <div class="container">
    <div class="coverage__inner">
      <div class="coverage__text">
        <span class="section-label">Coverage Area</span>
        <h2 class="section-title section-title--white">We Serve Across the UK</h2>
        <div class="gold-divider"></div>
        <p class="section-subtitle section-subtitle--white">Our professional cleaning teams operate throughout London and surrounding counties, bringing our premium service directly to you.</p>
        <div class="coverage__areas">
          <span class="coverage__tag">London</span><span class="coverage__tag">Surrey</span>
          <span class="coverage__tag">Kent</span><span class="coverage__tag">Essex</span>
          <span class="coverage__tag">Hertfordshire</span><span class="coverage__tag">Berkshire</span>
          <span class="coverage__tag">Middlesex</span><span class="coverage__tag">Sussex</span>
        </div>
      </div>
      <div class="coverage__cta">
        <a href="contact.html" class="btn btn--gold">Check Your Area</a>
      </div>
    </div>
  </div>
</section>
<div id="quote-form-container"></div>
<script>
  document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("quote-form-container").innerHTML = renderQuoteForm('Request a Free Quote');
  });
</script>"""

about_body = """<div id="page-hero-container"></div>
<script>
  document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("page-hero-container").innerHTML = renderPageHero('About Majestic Cedar Cleaning', 'Learn about our story, values, and the dedicated team behind every exceptional clean.', 'About Us');
  });
</script>
<section class="section">
  <div class="container">
    <div class="about-intro">
      <div class="about-intro__img-wrap">
        <img src="https://images.unsplash.com/photo-1521791136064-7986c2920216?w=800&q=80" alt="Our Team" class="about-intro__img">
        <div class="about-intro__img-accent"></div>
      </div>
      <div>
        <span class="section-label">Who We Are</span>
        <h2 class="section-title">A Legacy of Clean, Built on Trust</h2>
        <div class="gold-divider"></div>
        <p style="color:var(--text-grey);line-height:1.8;margin-bottom:20px;">Majestic Cedar Cleaning was founded on a simple belief: every home and business deserves a pristine, healthy environment. Since our founding, we have grown from a small local team into one of the UK's most trusted professional cleaning services.</p>
        <p style="color:var(--text-grey);line-height:1.8;margin-bottom:32px;">We combine traditional values of hard work and integrity with modern techniques and eco-friendly products. Our staff are fully vetted, trained to the highest standards, and genuinely passionate about what they do.</p>
        <a href="contact.html" class="btn btn--gold">Get in Touch</a>
      </div>
    </div>
  </div>
</section>
<section class="section section--grey">
  <div class="container">
    <div class="text-center" style="margin-bottom:56px;">
      <span class="section-label">Our Advantages</span>
      <h2 class="section-title">Why Choose Majestic Cedar?</h2>
      <div class="gold-divider gold-divider--center"></div>
    </div>
    <div class="why-choose__grid">
      <div class="why-card"><span class="why-card__icon">🏅</span><h3 class="why-card__title">Fully Insured</h3><p class="why-card__desc">Complete public liability insurance on every job. Your property is in safe hands at all times.</p></div>
      <div class="why-card"><span class="why-card__icon">🌿</span><h3 class="why-card__title">Eco-Friendly</h3><p class="why-card__desc">We use environmentally responsible products that are safe for your family, pets, and the planet.</p></div>
      <div class="why-card"><span class="why-card__icon">⏰</span><h3 class="why-card__title">Always Punctual</h3><p class="why-card__desc">We respect your time. Our teams arrive when promised and complete work within agreed timeframes.</p></div>
      <div class="why-card"><span class="why-card__icon">🔒</span><h3 class="why-card__title">DBS Checked</h3><p class="why-card__desc">Every team member is thoroughly background-checked for your complete peace of mind.</p></div>
    </div>
  </div>
</section>
<div class="stats-grid">
  <div class="stat-item"><div class="stat-item__number" data-count="12" data-suffix="+">0+</div><div class="stat-item__label">Years in Business</div></div>
  <div class="stat-item"><div class="stat-item__number" data-count="5000" data-suffix="+">0+</div><div class="stat-item__label">Clients Served</div></div>
  <div class="stat-item"><div class="stat-item__number" data-count="25000" data-suffix="+">0+</div><div class="stat-item__label">Jobs Completed</div></div>
  <div class="stat-item"><div class="stat-item__number" data-count="99" data-suffix="%">0%</div><div class="stat-item__label">Satisfaction Rate</div></div>
</div>
<section class="section">
  <div class="container">
    <div class="text-center" style="margin-bottom:48px;">
      <span class="section-label">Accreditations</span>
      <h2 class="section-title">Certified & Accredited</h2>
      <div class="gold-divider gold-divider--center"></div>
    </div>
    <div class="cert-grid">
      <div class="cert-badge" title="ISO Certified">🏆</div>
      <div class="cert-badge" title="NCCA Member">🌟</div>
      <div class="cert-badge" title="BICSc Accredited">✅</div>
      <div class="cert-badge" title="Safe Contractor">🛡</div>
      <div class="cert-badge" title="Which? Trusted">👍</div>
    </div>
  </div>
</section>
<section class="cta-banner">
  <div class="container">
    <span class="section-label">Ready to Start?</span>
    <h2 class="section-title">Experience the Majestic Difference</h2>
    <p class="section-subtitle" style="margin:0 auto;">Join thousands of satisfied clients who trust us to keep their spaces immaculate.</p>
    <div class="cta-banner__actions">
      <a href="contact.html" class="btn btn--gold">Get a Free Quote</a>
      <a href="services.html" class="btn btn--outline">View Services</a>
    </div>
  </div>
</section>"""

services_body = """<div id="page-hero-container"></div>
<script>
  document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("page-hero-container").innerHTML = renderPageHero('Our Cleaning Services', 'Professional, reliable cleaning solutions for homes and businesses across the UK.', 'Services');
  });
</script>
<section class="section">
  <div class="container">
    <div class="services-main-grid">
      <div class="service-main-card">
        <img src="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=700&q=80" alt="Residential Cleaning" class="service-main-card__img">
        <div class="service-main-card__body">
          <span class="service-main-card__icon">🏠</span>
          <h3 class="service-main-card__title">Residential Cleaning</h3>
          <p class="service-main-card__desc">Tailored home cleaning services for a spotless living space, whenever you need it.</p>
          <div class="service-main-card__actions">
            <a href="residential.html" class="btn btn--outline" style="padding:10px 20px;font-size:12px;">Read More</a>
            <a href="contact.html" class="btn btn--gold" style="padding:10px 20px;font-size:12px;">Get a Quote</a>
          </div>
        </div>
      </div>
      <div class="service-main-card">
        <img src="https://images.unsplash.com/photo-1497366216548-37526070297c?w=700&q=80" alt="Commercial Cleaning" class="service-main-card__img">
        <div class="service-main-card__body">
          <span class="service-main-card__icon">🏢</span>
          <h3 class="service-main-card__title">Commercial Cleaning</h3>
          <p class="service-main-card__desc">Professional office and commercial premises cleaning for a productive, hygienic workspace.</p>
          <div class="service-main-card__actions">
            <a href="commercial.html" class="btn btn--outline" style="padding:10px 20px;font-size:12px;">Read More</a>
            <a href="contact.html" class="btn btn--gold" style="padding:10px 20px;font-size:12px;">Get a Quote</a>
          </div>
        </div>
      </div>
      <div class="service-main-card">
        <img src="https://images.unsplash.com/photo-1527515637462-cff94eecc1ac?w=700&q=80" alt="Deep Cleaning" class="service-main-card__img">
        <div class="service-main-card__body">
          <span class="service-main-card__icon">✨</span>
          <h3 class="service-main-card__title">Deep Cleaning</h3>
          <p class="service-main-card__desc">An intensive, comprehensive clean targeting every nook and cranny of your property.</p>
          <div class="service-main-card__actions">
            <a href="deep-cleaning.html" class="btn btn--outline" style="padding:10px 20px;font-size:12px;">Read More</a>
            <a href="contact.html" class="btn btn--gold" style="padding:10px 20px;font-size:12px;">Get a Quote</a>
          </div>
        </div>
      </div>
      <div class="service-main-card">
        <img src="https://images.unsplash.com/photo-1600585152220-90363fe7e115?w=700&q=80" alt="End of Tenancy" class="service-main-card__img">
        <div class="service-main-card__body">
          <span class="service-main-card__icon">🔑</span>
          <h3 class="service-main-card__title">End of Tenancy</h3>
          <p class="service-main-card__desc">Comprehensive cleaning to secure your deposit return and meet landlord requirements.</p>
          <div class="service-main-card__actions">
            <a href="end-of-tenancy.html" class="btn btn--outline" style="padding:10px 20px;font-size:12px;">Read More</a>
            <a href="contact.html" class="btn btn--gold" style="padding:10px 20px;font-size:12px;">Get a Quote</a>
          </div>
        </div>
      </div>
      <div class="service-main-card">
        <img src="https://images.unsplash.com/photo-1503387762-592deb58ef4e?w=700&q=80" alt="After Builders Cleaning" class="service-main-card__img">
        <div class="service-main-card__body">
          <span class="service-main-card__icon">🏗️</span>
          <h3 class="service-main-card__title">After Builders</h3>
          <p class="service-main-card__desc">Specialized post-construction cleaning to remove dust, debris, and reveal your new space.</p>
          <div class="service-main-card__actions">
            <a href="after-builders.html" class="btn btn--outline" style="padding:10px 20px;font-size:12px;">Read More</a>
            <a href="contact.html" class="btn btn--gold" style="padding:10px 20px;font-size:12px;">Get a Quote</a>
          </div>
        </div>
      </div>
      <div class="service-main-card">
        <img src="https://images.unsplash.com/photo-1527018601619-a508a2be00cd?w=700&q=80" alt="Window Cleaning" class="service-main-card__img">
        <div class="service-main-card__body">
          <span class="service-main-card__icon">🪟</span>
          <h3 class="service-main-card__title">Window Cleaning</h3>
          <p class="service-main-card__desc">Crystal clear, streak-free window cleaning for residential and commercial properties.</p>
          <div class="service-main-card__actions">
            <a href="window-cleaning.html" class="btn btn--outline" style="padding:10px 20px;font-size:12px;">Read More</a>
            <a href="contact.html" class="btn btn--gold" style="padding:10px 20px;font-size:12px;">Get a Quote</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
<div id="quote-form-container"></div>
<script>
  document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("quote-form-container").innerHTML = renderQuoteForm('Ready for a Clean Space?');
  });
</script>"""

contact_body = """<div id="page-hero-container"></div>
<script>
  document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("page-hero-container").innerHTML = renderPageHero('Contact Us', 'Get in touch for a free quote or to discuss your cleaning requirements.', 'Contact');
  });
</script>
<section class="section">
  <div class="container">
    <div class="contact-grid">
      <div class="quote-form" style="box-shadow:none; border:none; padding:0; max-width:100%;">
        <span class="section-label">Send a Message</span>
        <h2 class="section-title">Request a Free Quote</h2>
        <div class="gold-divider"></div>
        <div class="form-grid" style="margin-top:32px;">
          <div class="form-group"><label>First Name</label><input type="text" placeholder="John"></div>
          <div class="form-group"><label>Last Name</label><input type="text" placeholder="Smith"></div>
          <div class="form-group"><label>Email Address</label><input type="email" placeholder="john@example.com"></div>
          <div class="form-group"><label>Phone Number</label><input type="tel" placeholder="07700 000000"></div>
          <div class="form-group form-grid--full"><label>Service Required</label>
            <select><option value="">Select a service...</option><option>Residential Cleaning</option><option>Commercial Cleaning</option><option>Deep Cleaning</option><option>End of Tenancy</option><option>After Builders</option><option>Window Cleaning</option></select>
          </div>
          <div class="form-group form-grid--full"><label>Message</label><textarea placeholder="Tell us more about your requirements..."></textarea></div>
        </div>
        <div style="margin-top:24px;">
          <button class="btn btn--gold" style="width:100%;justify-content:center;padding:16px;">Send Message <svg width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2"><path d="M13 7l5 5m0 0l-5 5m5-5H6"/></svg></button>
        </div>
      </div>
      <div>
        <div class="contact-info__item">
          <div class="contact-info__icon">📞</div>
          <div>
            <div class="contact-info__label">Phone</div>
            <div class="contact-info__value">0800 123 4567</div>
          </div>
        </div>
        <div class="contact-info__item">
          <div class="contact-info__icon">✉️</div>
          <div>
            <div class="contact-info__label">Email</div>
            <div class="contact-info__value">info@majesticcedarcleaning.co.uk</div>
          </div>
        </div>
        <div class="contact-info__item" style="border-bottom:none;">
          <div class="contact-info__icon">📍</div>
          <div>
            <div class="contact-info__label">Headquarters</div>
            <div class="contact-info__value">London, United Kingdom</div>
            <div style="font-size:14px;color:var(--text-grey);margin-top:8px;">Serving London, Surrey, Kent, Essex, and surrounding areas.</div>
          </div>
        </div>
        <div style="margin-top:24px; padding-top:24px; border-top:1px solid var(--mid-grey);">
            <div class="contact-info__label">Business Hours</div>
            <div class="hours-grid" style="margin-top:12px;">
                <div class="hours-row"><span class="hours-row__day">Monday - Friday</span><span class="hours-row__time">8:00 AM - 6:00 PM</span></div>
                <div class="hours-row"><span class="hours-row__day">Saturday</span><span class="hours-row__time">9:00 AM - 4:00 PM</span></div>
                <div class="hours-row"><span class="hours-row__day">Sunday</span><span class="hours-row__time">Closed</span></div>
            </div>
        </div>
        <div class="map-placeholder">
          <span style="font-size:24px;">🗺️</span>
          <div>Google Map Embed Placeholder</div>
        </div>
      </div>
    </div>
  </div>
</section>"""

def gen_service_page(title, short_title, desc, icon, img_url, benefits_arr, faq_arr, extra_section_html=""):
    benefits_html = "".join([f'<div class="benefit-card"><span class="benefit-card__icon">{b[0]}</span><h3 class="benefit-card__title">{b[1]}</h3><p class="benefit-card__desc">{b[2]}</p></div>' for b in benefits_arr])
    faq_html = "".join([f'<div class="faq__item"><div class="faq__question">{f[0]}<div class="faq__toggle">+</div></div><div class="faq__answer">{f[1]}</div></div>' for f in faq_arr])
    return f"""<div id="page-hero-container"></div>
<script>
  document.addEventListener("DOMContentLoaded", () => {{
    document.getElementById("page-hero-container").innerHTML = renderPageHero('{title}', '{desc}', 'Services', 'Services › {short_title}');
  }});
</script>
<section class="section">
  <div class="container">
    <div class="service-detail">
      <div>
        <span class="section-label">What We Do</span>
        <h2 class="section-title">What is {short_title}?</h2>
        <div class="gold-divider"></div>
        <p style="color:var(--text-grey);line-height:1.8;margin-bottom:24px;">Our {short_title.lower()} service is designed to provide you with the highest standard of cleanliness. We understand that every property is different, which is why we offer tailored solutions to meet your specific requirements.</p>
        <h3 style="font-family:var(--font-display);font-size:1.4rem;font-weight:600;margin-bottom:16px;">What's Included:</h3>
        <div class="checklist">
          <div class="checklist__item"><div class="checklist__icon">✓</div><div>Comprehensive dusting and wiping of all surfaces</div></div>
          <div class="checklist__item"><div class="checklist__icon">✓</div><div>Thorough vacuuming and mopping of floors</div></div>
          <div class="checklist__item"><div class="checklist__icon">✓</div><div>Detailed cleaning of bathrooms and kitchens</div></div>
          <div class="checklist__item"><div class="checklist__icon">✓</div><div>Emptying bins and general tidying</div></div>
        </div>
      </div>
      <img src="{img_url}" alt="{short_title}" class="service-detail__img">
    </div>
  </div>
</section>

{extra_section_html}

<section class="section section--grey">
  <div class="container">
    <div class="text-center" style="margin-bottom:48px;">
      <span class="section-label">Why Choose Us</span>
      <h2 class="section-title">Benefits of Our Service</h2>
      <div class="gold-divider gold-divider--center"></div>
    </div>
    <div class="benefits-grid">
      {benefits_html}
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="text-center" style="margin-bottom:48px;">
      <span class="section-label">Common Questions</span>
      <h2 class="section-title">Frequently Asked Questions</h2>
      <div class="gold-divider gold-divider--center"></div>
    </div>
    <div class="faq">
      {faq_html}
    </div>
  </div>
</section>
<section class="section section--gold-pale" style="padding:40px 0;">
    <div class="container">
        <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:20px;">
            <div style="font-weight:600;">Explore Related Services:</div>
            <div class="related-services">
                <a href="residential.html" class="related-tag">Residential</a>
                <a href="commercial.html" class="related-tag">Commercial</a>
                <a href="deep-cleaning.html" class="related-tag">Deep Cleaning</a>
                <a href="end-of-tenancy.html" class="related-tag">End of Tenancy</a>
                <a href="after-builders.html" class="related-tag">After Builders</a>
            </div>
        </div>
    </div>
</section>
<div id="quote-form-container"></div>
<script>
  document.addEventListener("DOMContentLoaded", () => {{
    document.getElementById("quote-form-container").innerHTML = renderQuoteForm('Get a Quote for {short_title}');
  }});
</script>"""

# Individual Services Generation
residential_html = gen_service_page(
    'Professional Residential Cleaning', 'Residential Cleaning', 'Keep your home spotless and comfortable with our trusted residential cleaning team.', '🏠',
    'https://images.unsplash.com/photo-1581578731548-c64695cc6952?w=800&q=80',
    [('⏰', 'Time Saving', 'Reclaim your weekends and let us handle the chores.'), ('🛡', 'Trusted Staff', 'Fully vetted professionals treating your home with care.'), ('✨', 'Spotless Results', 'Meticulous attention to detail on every visit.')],
    [('Do I need to be home?', 'No, many of our clients provide a spare key. Our staff are fully vetted and insured for your peace of mind.'), ('Do you bring your own supplies?', 'Yes, we provide all necessary professional cleaning equipment and eco-friendly products.')]
)

commercial_html = gen_service_page(
    'Expert Commercial Cleaning', 'Commercial Cleaning', 'Maintain a pristine and productive workspace with our tailored commercial cleaning.', '🏢',
    'https://images.unsplash.com/photo-1497366216548-37526070297c?w=800&q=80',
    [('💼', 'Professional Image', 'Make a great impression on clients and visitors.'), ('📈', 'Productivity', 'A clean office boosts employee morale and focus.'), ('🌙', 'Flexible Hours', 'We clean out of hours to minimize disruption.')],
    [('Can you clean out of business hours?', 'Yes, we offer early morning, evening, and weekend cleaning to suit your business hours.'), ('Are you fully insured?', 'Absolutely, we carry comprehensive public and employer liability insurance.')],
    """<section class="section" style="padding-top:0;"><div class="container"><h3 style="font-family:var(--font-display);font-size:1.8rem;font-weight:600;margin-bottom:24px;text-align:center;">Industries We Serve</h3><div style="display:flex;justify-content:center;gap:16px;flex-wrap:wrap;"><span class="related-tag" style="border-color:var(--text-dark);color:var(--text-dark);">Corporate Offices</span><span class="related-tag" style="border-color:var(--text-dark);color:var(--text-dark);">Retail Stores</span><span class="related-tag" style="border-color:var(--text-dark);color:var(--text-dark);">Medical Facilities</span><span class="related-tag" style="border-color:var(--text-dark);color:var(--text-dark);">Schools & Nurseries</span><span class="related-tag" style="border-color:var(--text-dark);color:var(--text-dark);">Warehouses</span></div></div></section>"""
)

deep_cleaning_html = gen_service_page(
    'Intensive Deep Cleaning', 'Deep Cleaning', 'A top-to-bottom clean reaching every corner of your property.', '✨',
    'https://images.unsplash.com/photo-1527515637462-cff94eecc1ac?w=800&q=80',
    [('🔍', 'Detail Oriented', 'We clean areas often missed in regular cleans.'), ('🦠', 'Hygienic', 'Eliminates hidden dust, bacteria, and allergens.'), ('🏠', 'Refresh', 'Breathes new life into older or neglected properties.')],
    [('How long does a deep clean take?', 'It depends on the size and condition of the property, but typically ranges from 4 to 8 hours.'), ('When should I get a deep clean?', 'We recommend deep cleaning every 6 months, or before special events and holidays.')],
    """<section class="section" style="padding-top:0;"><div class="container"><div style="background:var(--black);color:var(--white);padding:40px;border-radius:var(--radius);text-align:center;"><h3 style="font-family:var(--font-display);font-size:1.8rem;font-weight:600;margin-bottom:16px;color:var(--gold);">When Do You Need a Deep Clean?</h3><p style="color:rgba(255,255,255,0.7);max-width:600px;margin:0 auto;">Deep cleans are perfect for spring cleaning, preparing for a new baby, pre- or post-party cleanups, or simply resetting your home to a pristine baseline.</p></div></div></section>"""
)

eot_html = gen_service_page(
    'End of Tenancy Cleaning', 'End of Tenancy', 'Secure your deposit with our comprehensive moving-out cleaning service.', '🔑',
    'https://images.unsplash.com/photo-1600585152220-90363fe7e115?w=800&q=80',
    [('💰', 'Deposit Return', 'Meets strict landlord and agency inventory standards.'), ('📋', 'Checklist Based', 'We follow an agency-approved detailed checklist.'), ('⏱', 'Guaranteed', 'Free re-clean if the agency flags any issues within 48h.')],
    [('Do you guarantee I will get my deposit back?', 'While we cannot guarantee your landlord\'s actions, our service is designed to pass checkout inventory checks, and we offer a free re-clean guarantee if cleaning issues are flagged within 48 hours.'), ('Do you clean ovens and carpets?', 'Oven cleaning is standard. Professional carpet cleaning can be added for an additional fee.')],
    """<section class="section" style="padding-top:0;"><div class="container"><h3 style="font-family:var(--font-display);font-size:1.8rem;font-weight:600;margin-bottom:24px;text-align:center;">Who Is This For?</h3><div class="benefits-grid"><div class="benefit-card"><span class="benefit-card__icon">👤</span><h3 class="benefit-card__title">Tenants</h3><p class="benefit-card__desc">Moving out and need to secure your deposit.</p></div><div class="benefit-card"><span class="benefit-card__icon">🏠</span><h3 class="benefit-card__title">Landlords</h3><p class="benefit-card__desc">Preparing a property for new occupants.</p></div><div class="benefit-card"><span class="benefit-card__icon">🏢</span><h3 class="benefit-card__title">Letting Agents</h3><p class="benefit-card__desc">Reliable turnaround for managed portfolios.</p></div></div></div></section>"""
)

after_builders_html = gen_service_page(
    'After Builders Cleaning', 'After Builders', 'Remove construction dust and reveal the beauty of your newly built or renovated space.', '🏗️',
    'https://images.unsplash.com/photo-1503387762-592deb58ef4e?w=800&q=80',
    [('🧹', 'Dust Removal', 'Specialist vacuums to eliminate fine plaster dust.'), ('🧽', 'Paint Splatters', 'Careful removal of paint, grout, and sticker residue.'), ('✅', 'Move-in Ready', 'Transforms a site from a construction zone into a home.')],
    [('When should you come in?', 'We recommend waiting until all tradesmen have fully completed their work before we begin the final clean.'), ('Do you remove rubble?', 'No, we are a cleaning company. Heavy building waste and rubble must be removed by contractors beforehand.')],
    """<section class="section" style="padding-top:0;"><div class="container"><div style="max-width:800px;margin:0 auto;text-align:center;"><h3 style="font-family:var(--font-display);font-size:1.8rem;font-weight:600;margin-bottom:16px;">Stages of a Builders Clean</h3><p style="color:var(--text-grey);line-height:1.7;">A proper builders clean usually requires two phases: a rough initial clean to remove the bulk of the dust and debris, followed by a final sparkle clean to ensure every surface is polished and ready for handover.</p></div></div></section>"""
)

window_cleaning_html = gen_service_page(
    'Professional Window Cleaning', 'Window Cleaning', 'Crystal clear, streak-free windows for your home or business.', '🪟',
    'https://images.unsplash.com/photo-1527018601619-a508a2be00cd?w=800&q=80',
    [('✨', 'Streak Free', 'We use pure water systems for a flawless finish.'), ('🪜', 'Safe & Secure', 'Reach and wash systems allow cleaning up to several stories safely.'), ('☀️', 'More Light', 'Instantly brightens your interior spaces.')],
    [('How often should I have windows cleaned?', 'For residential, every 4-8 weeks is typical. For commercial, bi-weekly or monthly is recommended.'), ('Do you clean the frames?', 'Yes, we clean the glass, frames, and sills as standard.')]
)

generate_page('index.html', 'Home', 'Home', index_body)
generate_page('about.html', 'About Us', 'About', about_body)
generate_page('services.html', 'Services', 'Services', services_body)
generate_page('contact.html', 'Contact Us', 'Contact', contact_body)
generate_page('residential.html', 'Residential Cleaning', 'Services', residential_html)
generate_page('commercial.html', 'Commercial Cleaning', 'Services', commercial_html)
generate_page('deep-cleaning.html', 'Deep Cleaning', 'Services', deep_cleaning_html)
generate_page('end-of-tenancy.html', 'End of Tenancy Cleaning', 'Services', eot_html)
generate_page('after-builders.html', 'After Builders Cleaning', 'Services', after_builders_html)
generate_page('window-cleaning.html', 'Window Cleaning', 'Services', window_cleaning_html)

print("All HTML pages restored!")
