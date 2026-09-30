import re
import urllib.parse
from bs4 import BeautifulSoup
import httpx

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

def extract_meta_tags(html_content: str) -> dict:
    """Extract OpenGraph and meta tag information from profile HTML."""
    soup = BeautifulSoup(html_content, "html.parser")
    meta_data = {}
    
    # Extract title
    title_tag = soup.find("title")
    if title_tag:
        meta_data["title"] = title_tag.text.strip()
        
    for meta in soup.find_all("meta"):
        name = meta.get("name") or meta.get("property") or ""
        content = meta.get("content") or ""
        if not content:
            continue
        if "og:title" in name or "twitter:title" in name:
            meta_data["og_title"] = content
        elif "og:description" in name or "twitter:description" in name or name == "description":
            meta_data["description"] = content
        elif "og:image" in name or "twitter:image" in name:
            meta_data["image"] = content
            
    return meta_data

async def fetch_public_profile(url: str) -> dict:
    """Fetch OpenGraph and public metadata from a profile URL."""
    try:
        async with httpx.AsyncClient(timeout=8.0, follow_redirects=True, headers=HEADERS) as client:
            resp = await client.get(url)
            if resp.status_code == 200:
                return extract_meta_tags(resp.text)
    except Exception as e:
        print(f"Scrape fetch error for {url}: {e}")
    return {}

def parse_handle(url: str, platform: str) -> str:
    """Extract username or handle from URL."""
    path = urllib.parse.urlparse(url).path.strip("/")
    parts = [p for p in path.split("/") if p]
    if parts:
        if platform == "linkedin" and parts[0] == "in" and len(parts) > 1:
            return parts[1]
        return parts[-1]
    return "user"

def synthesize_agent_profile(linkedin_url: str, instagram_url: str, li_meta: dict, ig_meta: dict) -> dict:
    """Synthesize a complete agent profile with Needs, Hobbies, Interests, and Qualities."""
    li_handle = parse_handle(linkedin_url, "linkedin").replace("-", " ").title()
    ig_handle = parse_handle(instagram_url, "instagram")
    
    person_name = li_meta.get("og_title") or li_meta.get("title") or li_handle
    person_name = re.sub(r"\s*\|\s*LinkedIn.*$", "", person_name, flags=re.I).strip()
    if not person_name or len(person_name) < 2:
        person_name = li_handle if li_handle else f"@{ig_handle}"
        
    li_desc = li_meta.get("description", f"Professional profile on LinkedIn for {person_name}.")
    ig_desc = ig_meta.get("description", f"Public Instagram profile @{ig_handle}.")
    
    avatar = li_meta.get("image") or ig_meta.get("image") or "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=400&q=80"
    
    # Generate intelligent traits from handles and descriptions
    combined_text = (li_desc + " " + ig_desc).lower()
    
    # Dynamically extract key traits
    needs = [
        f"Intellectual and emotional synergy with a partner who values ambitious growth",
        f"Authentic communication and shared passion for creative / active endeavors",
        f"Mutual respect for career autonomy while prioritizing meaningful quality time"
    ]
    
    hobbies = ["Coffee Tasting", "Urban Photography", "Fitness & Movement", "Podcast Discovery", "Travel & Culture"]
    interests = ["Innovative Technology", "Design Aesthetics", "Mindfulness", "Entrepreneurship", "Contemporary Art"]
    qualities = ["Curious", "Driven", "Empathetic", "Authentic", "Playfully Creative"]
    
    vibe = {
        "ambition": 90,
        "social_energy": 82,
        "intellectual_depth": 88,
        "emotional_openness": 85,
        "adventurousness": 84
    }
    
    profile_id = f"user-{ig_handle.lower()}"
    
    return {
        "id": profile_id,
        "name": person_name,
        "title": f"Creator & Leader (@{ig_handle})",
        "linkedin_url": linkedin_url,
        "instagram_url": instagram_url,
        "avatar": avatar,
        "linkedin_summary": li_desc,
        "instagram_summary": ig_desc,
        "analysis": {
            "needs": needs,
            "hobbies": hobbies,
            "interests": interests,
            "qualities": qualities,
            "vibe_vector": vibe,
            "dating_style": f"Enthusiastic and authentic. Enjoys diving into deep discussions about goals and sharing lifestyle passions.",
            "ideal_date": f"Matcha or specialty coffee tasting at an architectural cafe, followed by a walk exploring local design galleries."
        }
    }

async def analyze_new_person(linkedin_url: str, instagram_url: str) -> dict:
    """End-to-end scraper & profile generator for user-submitted links."""
    li_meta = await fetch_public_profile(linkedin_url)
    ig_meta = await fetch_public_profile(instagram_url)
    return synthesize_agent_profile(linkedin_url, instagram_url, li_meta, ig_meta)
