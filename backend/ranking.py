"""
Ranking Module for Agentic Dating Platform
Ranks all candidates for every person based on agent date evaluation and multi-dimensional analysis.
"""

from typing import List, Dict
from dating_harness import calculate_compatibility

def generate_global_rankings(profiles: List[Dict]) -> Dict[str, List[Dict]]:
    """
    Generate ranked compatibility lists for all profiles in the pool.
    Returns a dictionary mapping profile_id to an ordered list of ranked matches.
    """
    rankings_by_person = {}
    
    for i, p1 in enumerate(profiles):
        p1_rankings = []
        for j, p2 in enumerate(profiles):
            if p1["id"] == p2["id"]:
                continue
                
            compat = calculate_compatibility(p1, p2)
            p1_rankings.append({
                "match_person_id": p2["id"],
                "name": p2["name"],
                "title": p2["title"],
                "avatar": p2["avatar"],
                "linkedin_url": p2["linkedin_url"],
                "instagram_url": p2["instagram_url"],
                "score": compat["overall_score"],
                "breakdown": compat["breakdown"],
                "shared_needs": compat["shared_needs"],
                "hobbies": p2["analysis"]["hobbies"][:3],
                "qualities": p2["analysis"]["qualities"][:3]
            })
            
        # Sort descending by score
        p1_rankings.sort(key=lambda x: x["score"], reverse=True)
        
        # Add rank position
        for idx, item in enumerate(p1_rankings):
            item["rank"] = idx + 1
            
        rankings_by_person[p1["id"]] = p1_rankings
        
    return rankings_by_person

def get_rankings_for_profile(profile_id: str, profiles: List[Dict]) -> List[Dict]:
    """Get sorted match rankings for a specific profile ID."""
    all_rankings = generate_global_rankings(profiles)
    return all_rankings.get(profile_id, [])
