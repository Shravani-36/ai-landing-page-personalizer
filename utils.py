import requests
from bs4 import BeautifulSoup


# -----------------------------------
# 1. Extract Landing Page Content
# -----------------------------------
def get_page_content(url):
    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")

        # Extract headings
        headings = [h.get_text().strip() for h in soup.find_all(["h1", "h2"])]

        # Extract paragraphs
        paragraphs = [p.get_text().strip() for p in soup.find_all("p")]

        # Combine limited content
        content = " ".join(headings[:5] + paragraphs[:10])

        if not content:
            return "No meaningful content found on the page."

        return content

    except Exception as e:
        return f"Error fetching page: {str(e)}"


# -----------------------------------
# 2. Personalization Logic (NO API)
# -----------------------------------
def personalize_content(ad_text, page_content):

    ad_lower = ad_text.lower()

    # Default values
    headline = "🚀 Upgrade Your Experience Today!"
    cta = "Explore Now"

    # Rule-based personalization
    if "discount" in ad_lower or "off" in ad_lower or "%" in ad_lower:
        headline = "💸 Exclusive Discount Just for You!"
        cta = "Grab the Deal"

    if "student" in ad_lower:
        headline = "🎓 Special Student Offer!"
        cta = "Unlock Your Discount"

    if "limited" in ad_lower or "today" in ad_lower:
        headline = "⏳ Limited Time Offer – Act Fast!"
        cta = "Shop Now"

    if "premium" in ad_lower or "luxury" in ad_lower:
        headline = "✨ Experience Premium Quality!"
        cta = "Upgrade Now"

    if "free" in ad_lower:
        headline = "🎁 Enjoy Free Benefits Today!"
        cta = "Claim Now"

    # Improved content (keeping structure similar)
    improved_copy = f"""
{headline}

{page_content[:300]}...

👉 This page is personalized based on your interest from the ad.

Don’t miss out on this opportunity!

{cta}
"""

    # Final structured output
    return f"""
Headline: {headline}

CTA: {cta}

Improved Copy:
{improved_copy}
"""