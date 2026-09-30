"""
Agentic Dating Harness Engine
Simulates authentic multi-turn dates between two AI agents dating on behalf of real people.
"""

import random

VENUES = [
    {
        "name": "Architectural Espresso & Matcha Bar",
        "setting": "A minimalist, sunlit industrial loft in Soho with specialty pour-overs and Japanese matcha.",
        "icon": "☕"
    },
    {
        "name": "Contemporary Art Gallery & Wine Lounge",
        "setting": "A modern gallery displaying vibrant abstract art with natural organic wines.",
        "icon": "🎨"
    },
    {
        "name": "Sunset Coastal Walk & Taco Stand",
        "setting": "A breezy oceanfront boardwalk watching the golden hour sky with artisanal tacos.",
        "icon": "🌮"
    },
    {
        "name": "Dimly Lit Speakeasy Cocktail Lounge",
        "setting": "A cozy leather booth behind a hidden bookcase with custom craft cocktails and jazz.",
        "icon": "🍸"
    }
]

def calculate_compatibility(p1: dict, p2: dict) -> dict:
    """Calculate deep multi-dimensional compatibility between two agents."""
    v1 = p1["analysis"]["vibe_vector"]
    v2 = p2["analysis"]["vibe_vector"]
    
    # 1. Ambition alignment
    ambition_diff = abs(v1["ambition"] - v2["ambition"])
    ambition_score = max(50, 100 - (ambition_diff * 2.5))
    
    # 2. Hobby overlap
    h1 = set(p1["analysis"]["hobbies"])
    h2 = set(p2["analysis"]["hobbies"])
    common_hobbies = h1.intersection(h2)
    hobby_score = 70 + (len(common_hobbies) * 10) + (len(h1.union(h2)) % 5 * 3)
    hobby_score = min(98, hobby_score)
    
    # 3. Emotional openness & social synergy
    social_avg = (v1["social_energy"] + v2["social_energy"]) / 2
    emotional_avg = (v1["emotional_openness"] + v2["emotional_openness"]) / 2
    eq_score = min(99, (social_avg * 0.4) + (emotional_avg * 0.6) + 10)
    
    # 4. Intellectual depth spark
    intel_avg = (v1["intellectual_depth"] + v2["intellectual_depth"]) / 2
    intel_score = min(99, intel_avg + random.randint(-2, 4))
    
    overall = round((ambition_score * 0.25) + (hobby_score * 0.25) + (eq_score * 0.25) + (intel_score * 0.25))
    
    # Rationales
    shared_needs = [
        f"Both value high-ambition dedication balanced with grounded personal life.",
        f"Shared enthusiasm for {p1['analysis']['hobbies'][0]} & {p2['analysis']['hobbies'][0]}.",
        f"Strong alignment between {p1['name']}'s focus on {p1['analysis']['qualities'][0]} and {p2['name']}'s {p2['analysis']['qualities'][0]} nature."
    ]
    
    return {
        "overall_score": overall,
        "breakdown": {
            "ambition_match": round(ambition_score),
            "lifestyle_synergy": round(hobby_score),
            "emotional_chemistry": round(eq_score),
            "intellectual_spark": round(intel_score)
        },
        "shared_needs": shared_needs
    }

def simulate_agent_date(p1: dict, p2: dict, venue_name: str = None) -> dict:
    """Run an interactive turn-by-turn simulated date between Agent P1 and Agent P2."""
    if not venue_name:
        venue = random.choice(VENUES)
    else:
        venue = next((v for v in VENUES if v["name"] == venue_name), VENUES[0])
        
    compat = calculate_compatibility(p1, p2)
    score = compat["overall_score"]
    
    n1 = p1["name"]
    n2 = p2["name"]
    
    h1_top = p1["analysis"]["hobbies"][0] if p1["analysis"]["hobbies"] else "travel"
    h2_top = p2["analysis"]["hobbies"][0] if p2["analysis"]["hobbies"] else "design"
    
    q1_top = p1["analysis"]["qualities"][0] if p1["analysis"]["qualities"] else "driven"
    q2_top = p2["analysis"]["qualities"][0] if p2["analysis"]["qualities"] else "thoughtful"
    
    turns = [
        {
            "speaker": p1["id"],
            "speaker_name": n1,
            "avatar": p1["avatar"],
            "turn_number": 1,
            "text": f"Hey {n2.split()[0]}! Welcome to {venue['name']}. I was just admiring the atmosphere here. How has your week been?",
            "sentiment": "Warm & Inviting",
            "vibe_meter": 72
        },
        {
            "speaker": p2["id"],
            "speaker_name": n2,
            "avatar": p2["avatar"],
            "turn_number": 2,
            "text": f"Hi {n1.split()[0]}! This spot is incredible. Honestly, week's been busy, but I made sure to save energy for tonight! I read on your profile that you're super passionate about {h1_top}. How did you get into that?",
            "sentiment": "Curious & Engaged",
            "vibe_meter": 78
        },
        {
            "speaker": p1["id"],
            "speaker_name": n1,
            "avatar": p1["avatar"],
            "turn_number": 3,
            "text": f"Ah, {h1_top} is my ultimate reset button! When you're managing big goals, you need something that grounds you. Looking at your Instagram vibe, it seems like you love {h2_top} and living intentionally. Is that what keeps your energy up?",
            "sentiment": "Insightful Connection",
            "vibe_meter": 84
        },
        {
            "speaker": p2["id"],
            "speaker_name": n2,
            "avatar": p2["avatar"],
            "turn_number": 4,
            "text": f"Spot on! What I really look for in life—and in a relationship—is a partner who is {q1_top} yet grounded. On your LinkedIn, your work vision is huge, but sitting here, I really appreciate how present and authentic your agent represents you.",
            "sentiment": "Deep Mutual Respect",
            "vibe_meter": 89
        },
        {
            "speaker": p1["id"],
            "speaker_name": n1,
            "avatar": p1["avatar"],
            "turn_number": 5,
            "text": f"That means a lot, {n2.split()[0]}. I feel like our agents nailed this match. What if we plan our next date around {p1['analysis']['ideal_date']}?",
            "sentiment": "High Chemistry & Spark",
            "vibe_meter": score
        },
        {
            "speaker": p2["id"],
            "speaker_name": n2,
            "avatar": p2["avatar"],
            "turn_number": 6,
            "text": f"Consider it a date! I'm reporting back to {n2.split()[0]} right now that this was a 10/10 connection.",
            "sentiment": "Enthusiastic Agreement",
            "vibe_meter": score
        }
    ]
    
    agent_1_debrief = f"I went on a date with {n2}'s agent at {venue['name']}. We connected deeply on {h1_top}, shared values around {q1_top} ambition, and mutual lifestyle expectations. Chemistry was {score}%. Highly recommended."
    agent_2_debrief = f"Dated {n1}'s agent tonight. Loved their grounding energy, authenticity, and clear vision for life. Overall compatibility score is {score}%. Recommend booking date #2!"
    
    return {
        "person_1": p1,
        "person_2": p2,
        "venue": venue,
        "compatibility": compat,
        "turns": turns,
        "agent_debriefs": {
            p1["id"]: agent_1_debrief,
            p2["id"]: agent_2_debrief
        }
    }
