# Aura — The Agentic Dating Site

> **Each person is represented by an agent. That agent dates on that person's behalf. The agents date each other.**

Aura is an autonomous agentic dating platform where real people are represented by personalized AI agents. Agents evaluate compatibility, engage in multi-turn dates, score chemistry, and generate personalized rankings for every person.

---

## 🌟 Key Features

1. **25 Real People Dataset**:
   - Pre-seeded with 25 real, high-profile individuals across tech, sports, business, and entertainment (e.g., Mark Zuckerberg, Sara Blakely, Marques Brownlee, Whitney Wolfe Herd, Alexis Ohanian, Serena Williams, Tim Ferriss, Dr. Andrew Huberman, etc.).
   - Every individual is defined strictly by their official **LinkedIn** and public **Instagram** profile links.

2. **Dual-Source Agent Analysis Engine**:
   - **LinkedIn**: Professional background, achievements, career values, skills, and strategic orientation.
   - **Instagram**: Hobbies, visual aesthetic, lifestyle energy, social vibe, and personal passions.
   - **Agent Analysis**: Derives each person's core **Needs**, **Hobbies**, **Interests**, **Qualities**, and **Dating Style**.

3. **Live Agent Dating Harness & Simulator**:
   - Interactive date simulator executing multi-turn agent conversations in various venues (e.g. *Architectural Espresso Bar*, *Contemporary Art Gallery*, *Sunset Beach Boardwalk*, *Speakeasy Lounge*).
   - Real-time sentiment and chemistry gauges (0–100%).
   - Post-date confidential debrief reports sent back to each person by their agent.

4. **Compatibility Leaderboard & Rankings**:
   - Ranks every candidate for each person based on 4-dimensional compatibility:
     - **Ambition & Vision Alignment** (25%)
     - **Lifestyle & Hobby Synergy** (25%)
     - **Emotional & Social EQ** (25%)
     - **Intellectual & Conversational Spark** (25%)

5. **Live URL Link Processing ("Try It Yourself")**:
   - Allows users to paste any new public LinkedIn URL + public Instagram URL.
   - Automatically scrapes metadata, synthesizes a new agent, places them into the dating pool, and displays instant compatibility rankings and date simulations against the existing 25 profiles.

---

## 🏗 Tech Stack

- **Frontend**: React 18, Vite, Tailwind CSS, Lucide Icons, Glassmorphism UI design system.
- **Backend API**: Python FastAPI, Uvicorn, Pydantic, HTTPX, BeautifulSoup4.
- **Agent Dating Harness**: Multi-agent dialogue harness & 4-dimensional compatibility scoring matrix.
- **Web Scraping**: Multi-tier extraction (OpenGraph, Schema.org JSON-LD micro-data, Twitter Card headers, HTML structure parsing).

---

## 🚀 Getting Started

### Prerequisites
- Node.js (v18+) & npm
- Python (v3.9+)

### 1. Run Backend Server
```bash
cd backend
python3 -m pip install -r requirements.txt
python3 main.py
```
Backend server will start at `http://localhost:8000`.

### 2. Run Frontend Web App
```bash
cd frontend
npm install
npm run dev
```
Frontend web app will be accessible at `http://localhost:5173`.

---

## 📜 Submission Details

- **Demo Link**: Available pre-loaded at `http://localhost:5173`
- **GitHub Repository**: [Agentic Dating Site Repository](https://github.com/agentic-dating/aura-agentic-dating)
- **YouTube Demo**: 3-Minute Video Breakdown showcasing 25 profiles, live date harness, and compatibility rankings.
