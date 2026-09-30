# Aura API Documentation

The Aura backend is built with FastAPI (Python) and serves profile data, live link scraping, multi-turn agent date simulations, and global compatibility rankings.

## Base URL
Local: `http://localhost:8000`  
Public Live Proxy: `https://cafad45a67e666.lhr.life/api`

---

## Endpoints

### 1. `GET /api/profiles`
Returns all active profile records currently in the dating pool.
- **Response**: Array of profile objects (`SEED_PROFILES` + dynamically ingested profiles).

```json
[
  {
    "id": "mark-zuckerberg",
    "name": "Mark Zuckerberg",
    "title": "Founder & CEO, Meta",
    "linkedin_url": "https://www.linkedin.com/in/mark-zuckerberg-618b62",
    "instagram_url": "https://www.instagram.com/zuck",
    "avatar": "https://...",
    "analysis": {
      "needs": ["Intellectual sparring partner...", "..."],
      "hobbies": ["Brazilian Jiu-Jitsu", "Hydrofoiling", "..."],
      "interests": ["Spatial Computing", "AGI", "..."],
      "qualities": ["Hyper-focused", "Analytically precise", "..."],
      "vibe_vector": { "ambition": 98, "social_energy": 65, "intellectual_depth": 95, "emotional_openness": 70, "adventurousness": 88 }
    }
  }
]
```

### 2. `GET /api/profiles/{profile_id}`
Get detailed profile and agent analysis for a single person.
- **Parameters**: `profile_id` (string slug, e.g., `mark-zuckerberg`, `sara-blakely`).

### 3. `GET /api/rankings/{profile_id}`
Returns candidate rankings for a specific person, sorted from highest compatibility score to lowest.

```json
[
  {
    "match_person_id": "sara-blakely",
    "name": "Sara Blakely",
    "score": 92,
    "rank": 1,
    "breakdown": {
      "ambition_match": 95,
      "lifestyle_synergy": 88,
      "emotional_chemistry": 92,
      "intellectual_spark": 93
    },
    "shared_needs": ["Both value high-ambition dedication..."]
  }
]
```

### 4. `POST /api/date`
Simulates a multi-turn date between two agents in a selected venue.
- **Body**:
```json
{
  "person1_id": "mark-zuckerberg",
  "person2_id": "sara-blakely",
  "venue_name": "Dimly Lit Speakeasy Cocktail Lounge"
}
```
- **Response**: Full turn-by-turn dialogue, live sentiment tracking, dynamic vibe meter, and agent post-date debrief reports.

### 5. `POST /api/ingest`
Scrapes public LinkedIn and Instagram profile links, synthesizes an agent profile, and adds them to the dating pool.
- **Body**:
```json
{
  "linkedin_url": "https://www.linkedin.com/in/username",
  "instagram_url": "https://www.instagram.com/username"
}
```
- **Response**: Created profile object and immediate compatibility rankings.

### 6. `GET /api/demo`
Returns pre-configured demo package containing profiles, sample simulated dates, and global rankings for instant UI rendering.
