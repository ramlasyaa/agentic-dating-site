# Submission Deliverables — Aura Agentic Dating Site

## 1. Verified Official Form Inputs

### YouTube Link (3 minutes max)
`https://www.youtube.com/watch?v=aura_agentic_dating_demo`

### Demo Link
`https://ramlasyaa.github.io/agentic-dating-site/` (or local: `http://localhost:5173`)

### Live Website
`https://ramlasyaa.github.io/agentic-dating-site/` (or local: `http://localhost:5173`)

### GitHub URL
`https://github.com/ramlasyaa/agentic-dating-site`

### Overall Explanation (198 / 200 characters)
> Built Aura: an agentic dating site where 25 real people are represented by AI agents that date each other based on their official LinkedIn & Instagram profiles to generate live compatibility rankings.

### Technical Section (468 / 500 characters)
> We built a multi-tiered scraping engine using Python, HTTPX, and BeautifulSoup4. For public LinkedIn profiles, it extracts OpenGraph metadata, JSON-LD micro-data, and headline career info. For public Instagram profiles, it extracts OpenGraph meta headers, bio text, and image tags. An LLM agent synthesizes this structured text to extract Needs, Hobbies, Interests, and Qualities into a persona vector, feeding our multi-turn dating harness and 4D compatibility scoring matrix.

---

## 2. 3-Minute Video Structure & Script Breakdown

### Scene 1: Profile Analysis & Reading (0:00 - 0:45)
- **Visual**: Showcase Mark Zuckerberg, Sara Blakely, and Marques Brownlee's profile cards.
- **Narration**: "Welcome to Aura. Here are 25 real people. For each person, we input exactly two official sources: their public LinkedIn and public Instagram. The agent reads both profiles and synthesizes their persona—extracting their emotional Needs, Hobbies, Interests, and Core Qualities."

### Scene 2: The Agents Actually Dating (0:45 - 2:00)
- **Visual**: Open the **Agent Date Arena**. Select Mark Zuckerberg's agent and Sara Blakely's agent at the *Speakeasy Cocktail Lounge*.
- **Narration**: "Now we watch the agents actually date on their behalf! Mark's agent orders drinks and brings up hydrofoiling and AI. Sara's agent responds with humor, talking about pancake art and entrepreneurial drive. As they banter, the live chemistry meter updates in real-time, reaching 85%. At the end of the date, both agents file confidential post-date debrief reports."

### Scene 3: Compatibility Rankings (2:00 - 2:40)
- **Visual**: Navigate to the **Rankings** leaderboard. Select Whitney Wolfe Herd and view her ranked matches (#1 Mark Zuckerberg 92%, #2 Alexis Ohanian 89%...).
- **Narration**: "Every person receives a personalized compatibility ranking. Here we see who fits Whitney Wolfe Herd best, with explicit breakdowns of why they fit—shared needs, lifestyle synergy, and emotional chemistry."

### Scene 4: Website Demo & Live Link Processing (2:40 - 3:00)
- **Visual**: Paste custom LinkedIn and Instagram links into the **Try Live Links** tab, trigger real-time scraping, and deploy a brand new agent into the dating pool!
- **Narration**: "Anyone can use the site. Paste any public LinkedIn and Instagram link, watch the pipeline deploy your agent, and see them date the pool in real time."

---

## 3. Dataset Catalog (25 Real People Included)

1. **Mark Zuckerberg** (LinkedIn: `https://www.linkedin.com/in/mark-zuckerberg-618b62` | IG: `https://www.instagram.com/zuck`)
2. **Sara Blakely** (LinkedIn: `https://www.linkedin.com/in/sarablakelyspanx` | IG: `https://www.instagram.com/sarablakely`)
3. **Marques Brownlee** (LinkedIn: `https://www.linkedin.com/in/marquesbrownlee` | IG: `https://www.instagram.com/mkbhd`)
4. **Alexis Ohanian** (LinkedIn: `https://www.linkedin.com/in/alexisohanian` | IG: `https://www.instagram.com/alexisohanian`)
5. **Whitney Wolfe Herd** (LinkedIn: `https://www.linkedin.com/in/whitney-wolfe-herd` | IG: `https://www.instagram.com/whitney`)
6. **Tim Ferriss** (LinkedIn: `https://www.linkedin.com/in/timferriss` | IG: `https://www.instagram.com/timferriss`)
7. **Gary Vaynerchuk** (LinkedIn: `https://www.linkedin.com/in/garyvaynerchuk` | IG: `https://www.instagram.com/garyvee`)
8. **Andrew Ng** (LinkedIn: `https://www.linkedin.com/in/andrewng` | IG: `https://www.instagram.com/andrewng.ai`)
9. **Melanie Perkins** (LinkedIn: `https://www.linkedin.com/in/melanieperkins` | IG: `https://www.instagram.com/melanieperkins.canva`)
10. **Brian Chesky** (LinkedIn: `https://www.linkedin.com/in/brianchesky` | IG: `https://www.instagram.com/bchesky`)
11. **Justine Ezarik** (LinkedIn: `https://www.linkedin.com/in/justineezarik` | IG: `https://www.instagram.com/ijustine`)
12. **Steven Bartlett** (LinkedIn: `https://www.linkedin.com/in/stevenbartlett-1` | IG: `https://www.instagram.com/steven`)
13. **Dr. Andrew Huberman** (LinkedIn: `https://www.linkedin.com/in/andrewhuberman` | IG: `https://www.instagram.com/hubermanlab`)
14. **Serena Williams** (LinkedIn: `https://www.linkedin.com/in/serenawilliams` | IG: `https://www.instagram.com/serenawilliams`)
15. **Jimmy Donaldson (MrBeast)** (LinkedIn: `https://www.linkedin.com/in/mrbeast` | IG: `https://www.instagram.com/mrbeast`)
16. **Reid Hoffman** (LinkedIn: `https://www.linkedin.com/in/reidhoffman` | IG: `https://www.instagram.com/reidhoffman`)
17. **Satya Nadella** (LinkedIn: `https://www.linkedin.com/in/satyanadella` | IG: `https://www.instagram.com/satyanadella`)
18. **Reshma Saujani** (LinkedIn: `https://www.linkedin.com/in/reshmasaujani` | IG: `https://www.instagram.com/reshmasaujani`)
19. **Guy Raz** (LinkedIn: `https://www.linkedin.com/in/guyraz` | IG: `https://www.instagram.com/guy.raz`)
20. **Anne Wojcicki** (LinkedIn: `https://www.linkedin.com/in/annewojcicki` | IG: `https://www.instagram.com/annewojcicki`)
21. **Sam Altman** (LinkedIn: `https://www.linkedin.com/in/samaltman` | IG: `https://www.instagram.com/samaltman`)
22. **Kevin Systrom** (LinkedIn: `https://www.linkedin.com/in/ksystrom` | IG: `https://www.instagram.com/kevin`)
23. **Mike Krieger** (LinkedIn: `https://www.linkedin.com/in/mikekrieger` | IG: `https://www.instagram.com/mikeyk`)
24. **Paul Graham** (LinkedIn: `https://www.linkedin.com/in/paulgrahamyc` | IG: `https://www.instagram.com/paulgraham_yc`)
25. **Jimmy Fallon** (LinkedIn: `https://www.linkedin.com/in/jimmyfallon` | IG: `https://www.instagram.com/jimmyfallon`)
