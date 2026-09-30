import os
from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, HttpUrl

from data.seed_profiles import SEED_PROFILES
from scraper import analyze_new_person
from dating_harness import simulate_agent_date, calculate_compatibility
from ranking import generate_global_rankings, get_rankings_for_profile

app = FastAPI(
    title="Agentic Dating Site API",
    description="Backend API serving 25 real profile analyses, agent date simulations, rankings, and live URL scraping.",
    version="1.0.0"
)

# Enable CORS for local dev and frontend interaction
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory database initialized with 25 real seed profiles
PROFILES_DB = list(SEED_PROFILES)

class IngestRequest(BaseModel):
    linkedin_url: str
    instagram_url: str

class DateRequest(BaseModel):
    person1_id: str
    person2_id: str
    venue_name: Optional[str] = None

@app.get("/")
def root():
    return {
        "status": "online",
        "service": "Agentic Dating Platform API",
        "total_profiles": len(PROFILES_DB)
    }

@app.get("/api/profiles")
def get_all_profiles():
    """Retrieve all active profiles in the dating pool."""
    return PROFILES_DB

@app.get("/api/profiles/{profile_id}")
def get_profile(profile_id: str):
    """Get single profile detail & agent analysis."""
    p = next((item for item in PROFILES_DB if item["id"] == profile_id), None)
    if not p:
        raise HTTPException(status_code=404, detail="Profile not found")
    return p

@app.get("/api/rankings/{profile_id}")
def get_rankings(profile_id: str):
    """Get candidate rankings for a specific person."""
    p = next((item for item in PROFILES_DB if item["id"] == profile_id), None)
    if not p:
        raise HTTPException(status_code=404, detail="Profile not found")
    return get_rankings_for_profile(profile_id, PROFILES_DB)

@app.post("/api/date")
def start_agent_date(req: DateRequest):
    """Run interactive simulated date between two agents."""
    p1 = next((item for item in PROFILES_DB if item["id"] == req.person1_id), None)
    p2 = next((item for item in PROFILES_DB if item["id"] == req.person2_id), None)
    if not p1 or not p2:
        raise HTTPException(status_code=404, detail="One or both profiles not found")
    if p1["id"] == p2["id"]:
        raise HTTPException(status_code=400, detail="Cannot simulate a date with oneself")
        
    date_result = simulate_agent_date(p1, p2, req.venue_name)
    return date_result

@app.post("/api/ingest")
async def ingest_links(req: IngestRequest):
    """Scrape public LinkedIn + Instagram links and instantiate a new agent profile."""
    if not req.linkedin_url or not req.instagram_url:
        raise HTTPException(status_code=400, detail="Both LinkedIn and Instagram links are required")
        
    new_profile = await analyze_new_person(req.linkedin_url, req.instagram_url)
    
    # Check if already exists in DB, update or append
    existing_idx = next((i for i, p in enumerate(PROFILES_DB) if p["id"] == new_profile["id"]), None)
    if existing_idx is not None:
        PROFILES_DB[existing_idx] = new_profile
    else:
        PROFILES_DB.insert(0, new_profile)
        
    rankings = get_rankings_for_profile(new_profile["id"], PROFILES_DB)
    
    return {
        "message": "Profile ingested & agent created successfully",
        "profile": new_profile,
        "rankings": rankings
    }

@app.get("/api/demo")
def get_demo_package():
    """Get pre-configured demo package with 25 profiles, sample dates, and rankings."""
    p1 = PROFILES_DB[0] # Mark Zuckerberg
    p2 = PROFILES_DB[1] # Sara Blakely
    p3 = PROFILES_DB[2] # Marques Brownlee
    p4 = PROFILES_DB[3] # Alexis Ohanian
    
    sample_date_1 = simulate_agent_date(p1, p2, "Dimly Lit Speakeasy Cocktail Lounge")
    sample_date_2 = simulate_agent_date(p3, p4, "Architectural Espresso & Matcha Bar")
    
    global_rankings = generate_global_rankings(PROFILES_DB)
    
    return {
        "profiles_count": len(PROFILES_DB),
        "profiles": PROFILES_DB,
        "sample_dates": [sample_date_1, sample_date_2],
        "rankings": global_rankings
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
