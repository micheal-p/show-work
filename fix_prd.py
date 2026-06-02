import os
import glob
import re

def fix_topbar():
    with open('shared.js', 'r') as f:
        content = f.read()

    # The email block in topbar is a span containing info@majesticcedarcleaning.co.uk
    email_regex = r'<span class="topbar__item">\s*<svg[^>]*>.*?info@majesticcedarcleaning\.co\.uk\s*</span>'
    content = re.sub(email_regex, '', content, flags=re.DOTALL)
    
    # Rename CTA
    content = content.replace('Get a Free Quote</a>', 'Get a Quote</a>')

    # Add social icons to footer
    if 'footer__social' not in content:
        social_html = """
        <div>
          <p class="footer__heading">Follow Us</p>
          <div class="footer__social" style="display:flex; gap:16px;">
            <a href="#" style="color:var(--text-grey);"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg></a>
            <a href="#" style="color:var(--text-grey);"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
            <a href="#" style="color:var(--text-grey);"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg></a>
          </div>
        </div>"""
        content = content.replace('</div>\n      </div>\n    </div>\n    <div style="border-top:1px solid rgba(255,255,255,0.07);">', social_html + '\n      </div>\n    </div>\n    <div style="border-top:1px solid rgba(255,255,255,0.07);">')

    with open('shared.js', 'w') as f:
        f.write(content)


def fix_home():
    with open('index.html', 'r') as f:
        content = f.read()
    
    # Rename CTAs
    content = content.replace('📞 Call Us Now', 'Call Us')
    content = content.replace('Get a Free Quote', 'Get a Quote')

    with open('index.html', 'w') as f:
        f.write(content)

def fix_services():
    with open('services.html', 'r') as f:
        content = f.read()

    # Remove "Get a Quote" from cards
    content = re.sub(r'<a href="contact\.html"[^>]*>Get a Quote</a>', '', content)
    with open('services.html', 'w') as f:
        f.write(content)

def fix_individual_services():
    service_pages = ['residential.html', 'commercial.html', 'deep-cleaning.html', 'end-of-tenancy.html', 'after-builders.html', 'window-cleaning.html']
    for page in service_pages:
        with open(page, 'r') as f:
            content = f.read()
        
        # Add "Get a Quote" CTA banner before FAQ
        if 'class="cta-banner"' not in content:
            cta_banner = """
<section class="cta-banner" style="background:var(--black); padding:60px 0; text-align:center;">
  <div class="container">
    <h2 class="section-title" style="color:var(--gold); margin-bottom:16px;">Ready for a Cleaner Space?</h2>
    <p class="section-subtitle" style="color:rgba(255,255,255,0.8); margin:0 auto 32px auto; max-width:600px;">Contact us today to get a custom, no-obligation quote.</p>
    <a href="contact.html" class="btn btn--gold" style="display:inline-flex;">Get a Quote</a>
  </div>
</section>
"""
            # Insert before the FAQ section. FAQ section starts with <section class="section">\n  <div class="container">\n    <div class="text-center" style="margin-bottom:48px;">\n      <span class="section-label">Common Questions</span>
            content = content.replace('<span class="section-label">Common Questions</span>', cta_banner + '\n<span class="section-label">Common Questions</span>')

        with open(page, 'w') as f:
            f.write(content)

def fix_contact():
    with open('contact.html', 'r') as f:
        content = f.read()

    # Add social links
    if 'Social Media' not in content:
        social_links = """
        <div style="margin-top:24px; padding-top:24px; border-top:1px solid var(--mid-grey);">
            <div class="contact-info__label">Social Media Links</div>
            <div style="display:flex; gap:16px; margin-top:12px;">
                <a href="#" style="color:var(--gold);"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg></a>
                <a href="#" style="color:var(--gold);"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
                <a href="#" style="color:var(--gold);"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg></a>
            </div>
        </div>
        """
        # Insert right after Business hours
        content = content.replace('</div>\n        <div style="margin-top:32px; width:100%; height:300px;', social_links + '\n        </div>\n        <div style="margin-top:32px; width:100%; height:300px;')
    
    with open('contact.html', 'w') as f:
        f.write(content)

fix_services()
fix_individual_services()
fix_contact()
fix_home()
fix_topbar()
print("PRD fixes applied successfully!")
