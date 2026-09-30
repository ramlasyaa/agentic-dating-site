"""
Seed dataset containing 25 real people with official public LinkedIn and Instagram links,
along with agent-derived needs, hobbies, interests, qualities, and dating personas.
"""

SEED_PROFILES = [
    {
        "id": "mark-zuckerberg",
        "name": "Mark Zuckerberg",
        "title": "Founder & CEO, Meta",
        "linkedin_url": "https://www.linkedin.com/in/mark-zuckerberg-618b62",
        "instagram_url": "https://www.instagram.com/zuck",
        "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=400&q=80",
        "linkedin_summary": "Founder and CEO of Meta. Leading the build of the metaverse, AI, and social connection platforms. Background in computer science & psychology at Harvard.",
        "instagram_summary": "Hydrofoiling, Brazilian Jiu-Jitsu tournaments, outdoor family hikes, building AI smart home assistants, wearing custom streetwear, smoking meats in the backyard.",
        "analysis": {
            "needs": [
                "Intellectual sparring partner who values extreme focus and long-term vision",
                "Someone who enjoys physical outdoor challenges (Jiu-Jitsu, surfing, hydrofoiling)",
                "Grounded emotional stability amidst high-intensity public pressure"
            ],
            "hobbies": ["Brazilian Jiu-Jitsu", "Hydrofoiling", "Smoking Meats", "AI Tinkering", "Hiking"],
            "interests": ["Spatial Computing", "Artificial General Intelligence", "Open Source AI", "Renaissance History", "Macroeconomics"],
            "qualities": ["Hyper-focused", "Analytically precise", "Disciplined", "Family-oriented", "Playfully competitive"],
            "vibe_vector": {"ambition": 98, "social_energy": 65, "intellectual_depth": 95, "emotional_openness": 70, "adventurousness": 88},
            "dating_style": "Brings intense curiosity to the conversation, loves discussing future visions while sharing good food.",
            "ideal_date": "Sunset hydrofoiling session followed by outdoor wood-fired BBQ and conversation on the future of humanity."
        }
    },
    {
        "id": "sara-blakely",
        "name": "Sara Blakely",
        "title": "Founder, Spanx & Investor",
        "linkedin_url": "https://www.linkedin.com/in/sarablakelyspanx",
        "instagram_url": "https://www.instagram.com/sarablakely",
        "avatar": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=400&q=80",
        "linkedin_summary": "Self-made billionaire entrepreneur, founder of Spanx, guest shark on Shark Tank. Advocate for female entrepreneurship and creative problem solving.",
        "instagram_summary": "Doodle notebooks, goofy viral dances, empowering women entrepreneurs, red backpack travel moments, family pancake art mornings, high-energy humor.",
        "analysis": {
            "needs": [
                "Unapologetic humor and readiness to laugh at life's mishaps",
                "Mutual support for big entrepreneurial dreams without ego clash",
                "Spontaneity and high-energy joy in everyday moments"
            ],
            "hobbies": ["Pancake Art", "Journaling & Mind-Mapping", "Dancing", "Mentoring Female Founders", "Collecting Vintage Fashion"],
            "interests": ["Invention & Product Design", "Female Empowerment", "Creative Thinking", "Comedy", "Philanthropy"],
            "qualities": ["Resilient", "Humble & Hilarious", "Optimistic", "Vibrant", "Deeply Caring"],
            "vibe_vector": {"ambition": 94, "social_energy": 95, "intellectual_depth": 85, "emotional_openness": 92, "adventurousness": 85},
            "dating_style": "Disarms you immediately with self-deprecating humor and infectiously enthusiastic brainstorming.",
            "ideal_date": "Creative art studio date followed by street tacos and spontaneous karaoke."
        }
    },
    {
        "id": "marques-brownlee",
        "name": "Marques Brownlee",
        "title": "Tech Creator & Ultimate Frisbee Athlete",
        "linkedin_url": "https://www.linkedin.com/in/marquesbrownlee",
        "instagram_url": "https://www.instagram.com/mkbhd",
        "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=400&q=80",
        "linkedin_summary": "Leading technology reviewer, producer, host of Waveform Podcast, competitive professional ultimate frisbee player (AUDL). Stevens Institute of Technology graduate.",
        "instagram_summary": "Matte black aesthetics, RED camera rigs, professional frisbee highlights, electric supercar test drives, crisp studio setups, behind-the-scenes production clips.",
        "analysis": {
            "needs": [
                "Appreciation for craftsmanship, design minimalism, and technical detail",
                "Active, sports-oriented lifestyle balance",
                "Calm, composed, and authentic communication style"
            ],
            "hobbies": ["Professional Ultimate Frisbee", "EV Supercar Testing", "Cinematography", "Podcasting", "Tech Unboxing"],
            "interests": ["Industrial Design", "Camera Sensor Tech", "Automotive Innovation", "Consumer Electronics", "Sports Science"],
            "qualities": ["Meticulous", "Composed", "Authentic", "Athletic", "Visually Attuned"],
            "vibe_vector": {"ambition": 90, "social_energy": 75, "intellectual_depth": 90, "emotional_openness": 78, "adventurousness": 82},
            "dating_style": "Thoughtful, articulate listener who notices subtle design details and loves sharing peak aesthetic experiences.",
            "ideal_date": "Test driving an electric vehicle to a minimalist espresso bar, followed by an ultimate frisbee scrimmage."
        }
    },
    {
        "id": "alexis-ohanian",
        "name": "Alexis Ohanian",
        "title": "Co-founder Reddit & Seven Seven Six",
        "linkedin_url": "https://www.linkedin.com/in/alexisohanian",
        "instagram_url": "https://www.instagram.com/alexisohanian",
        "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=400&q=80",
        "linkedin_summary": "Co-founder of Reddit, founder of VC firm Seven Seven Six. Lead investor in women's sports (Angel City FC, Athlos), internet pioneer, University of Virginia alum.",
        "instagram_summary": "Pancake sculptures for his daughters, women's sports court-side fandom, trading cards collection, tech startup investing tips, dad life pride.",
        "analysis": {
            "needs": [
                "Partner who champions equality and invests deeply in family life",
                "Shared passion for sports, culture, and building legacy projects",
                "Willingness to indulge in geeky pop culture & trading card hobbies"
            ],
            "hobbies": ["Pancake Art", "Sports Card Collecting", "Attending Women's Tennis/Soccer Matches", "Gaming", "Venture Investing"],
            "interests": ["Women's Sports Empowerment", "Web3 & Tech Infrastructure", "Waffle/Pancake Culinary Art", "Fatherhood", "Pop Culture"],
            "qualities": ["Supportive", "Visionary", "Family-First", "Enthusiastic", "Engaged"],
            "vibe_vector": {"ambition": 92, "social_energy": 88, "intellectual_depth": 88, "emotional_openness": 90, "adventurousness": 80},
            "dating_style": "Wears his heart on his sleeve, hypes up your achievements, and loves making gourmet breakfast items.",
            "ideal_date": "VIP tickets to a women's championship soccer match followed by late-night dessert and board games."
        }
    },
    {
        "id": "whitney-wolfe-herd",
        "name": "Whitney Wolfe Herd",
        "title": "Founder & Executive Chair, Bumble",
        "linkedin_url": "https://www.linkedin.com/in/whitney-wolfe-herd",
        "instagram_url": "https://www.instagram.com/whitney",
        "avatar": "https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&w=400&q=80",
        "linkedin_summary": "Founder and Executive Chair of Bumble, youngest female founder to take a company public. Pioneer in female-first social networks and online safety legislation.",
        "instagram_summary": "Texas ranch sunsets, yellow floral decor, mother-son moments, female empowerment keynote speeches, cozy interior aesthetics, wellness routines.",
        "analysis": {
            "needs": [
                "Kindness and respectful, modern relationship dynamics",
                "Quiet sanctuary and nature-filled downtime away from corporate noise",
                "Emotional intelligence and proactive empathy"
            ],
            "hobbies": ["Interior Decorating", "Ranch Life & Horseback Riding", "Wellness & Meditation", "Garden Design", "Hosting Dinner Parties"],
            "interests": ["Relationship Psychology", "Female Founder Support", "Digital Safety", "Organic Architecture", "Mindfulness"],
            "qualities": ["Empathetic", "Graceful", "Trailblazing", "Warm", "Intentionally Kind"],
            "vibe_vector": {"ambition": 93, "social_energy": 80, "intellectual_depth": 87, "emotional_openness": 95, "adventurousness": 76},
            "dating_style": "Focuses on deep emotional connection, active listening, and creating a safe, comfortable ambiance.",
            "ideal_date": "Golden hour walk on a scenic Texas ranch followed by an intimate farm-to-table candlelit dinner."
        }
    },
    {
        "id": "tim-ferriss",
        "name": "Tim Ferriss",
        "title": "Author & Podcaster (The Tim Ferriss Show)",
        "linkedin_url": "https://www.linkedin.com/in/timferriss",
        "instagram_url": "https://www.instagram.com/timferriss",
        "avatar": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?auto=format&fit=crop&w=400&q=80",
        "linkedin_summary": "Author of 5 #1 NYT bestsellers (The 4-Hour Workweek, Tools of Titans). Early investor in Uber, Twitter, Facebook. Host of podcast with 900M+ downloads.",
        "instagram_summary": "Dog training with Molly, Japanese tea ceremonies, archery practice, psychedelic medicine science research, stoic quotes, ice baths, book recommendations.",
        "analysis": {
            "needs": [
                "Curious explorer who loves deep questioning and mental frameworks",
                "Adherence to health optimization, biohacking, and mental resilience",
                "Love for dogs, nature retreats, and tranquil silence"
            ],
            "hobbies": ["Archery", "Dog Training", "Cold Plunges & Sauna", "Japanese Tea Rituals", "Book Collecting"],
            "interests": ["Psychedelic Science", "Stoic Philosophy", "Meta-Learning", "Longitudinal Health", "Japanese Craftsmanship"],
            "qualities": ["Analytical", "Philosophical", "Experimental", "Disciplined", "Introspective"],
            "vibe_vector": {"ambition": 89, "social_energy": 60, "intellectual_depth": 98, "emotional_openness": 82, "adventurousness": 92},
            "dating_style": "Asks fascinating, non-standard questions, shares biohacking tips, and values deep presence.",
            "ideal_date": "Matcha tea ceremony in a Japanese garden followed by an archery lesson and deep philosophical talk."
        }
    },
    {
        "id": "gary-vaynerchuk",
        "name": "Gary Vaynerchuk",
        "title": "Chairman VaynerX & CEO VaynerMedia",
        "linkedin_url": "https://www.linkedin.com/in/garyvaynerchuk",
        "instagram_url": "https://www.instagram.com/garyvee",
        "avatar": "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&w=400&q=80",
        "linkedin_summary": "Serial entrepreneur, chairman of VaynerX, CEO of VaynerMedia, creator of VeeFriends. NYT bestselling author, NY Jets fanatic, garage sale hunter.",
        "instagram_summary": "High-octane motivational rants, garage sale flips on weekends, NY Jets game reactions, VeeFriends art, wine tasting throwback clips, hustle mindset quotes.",
        "analysis": {
            "needs": [
                "Partner with thick skin who thrives under high energy and rapid movement",
                "Authentic empathy and zero tolerance for pretense or complaining",
                "Someone who finds joy in the daily hustle and flea market treasure hunting"
            ],
            "hobbies": ["Garage Sale Treasure Hunting", "NY Jets Tailgating", "Wine Tasting", "Trading Cards", "Keynote Speaking"],
            "interests": ["Consumer Attention Trends", "VeeFriends & Intellectual Property", "Kindness in Business", "Vintage Toys", "Social Commerce"],
            "qualities": ["Relentless", "Hyper-energetic", "Radically Honest", "Empathetic", "Street-smart"],
            "vibe_vector": {"ambition": 99, "social_energy": 100, "intellectual_depth": 82, "emotional_openness": 85, "adventurousness": 88},
            "dating_style": "High-octane energy, direct expression, constant passion, and unexpected bursts of warm encouragement.",
            "ideal_date": "Early morning flea market hunt for vintage pop culture items followed by espresso and an impromptu Jets game tailgate."
        }
    },
    {
        "id": "andrew-ng",
        "name": "Andrew Ng",
        "title": "Founder DeepLearning.AI & Coursera",
        "linkedin_url": "https://www.linkedin.com/in/andrewng",
        "instagram_url": "https://www.instagram.com/andrewng.ai",
        "avatar": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&w=400&q=80",
        "linkedin_summary": "Co-founder of Coursera, Founder of DeepLearning.AI, Managing General Partner of AI Fund, Adjunct Professor at Stanford University. Former Chief Scientist at Baidu.",
        "instagram_summary": "AI education workshops, Stanford lecture halls, teaching children to code, reading research papers on flights, blue blazer style, global tech keynote moments.",
        "analysis": {
            "needs": [
                "Intellectual companion passionate about education, science, and human progress",
                "Gentle, patient, and methodical approach to life",
                "Shared dedication to making positive global impact"
            ],
            "hobbies": ["Reading Research Papers", "Teaching & Mentoring", "Puzzles & Chess", "Writing Technical Guides", "Quiet Coffee Visits"],
            "interests": ["Machine Learning & Neural Networks", "Democratizing Education", "AI Ethics & Safety", "Robotics", "EdTech"],
            "qualities": ["Patient", "Brilliant", "Gentle", "Methodical", "Deeply Ethical"],
            "vibe_vector": {"ambition": 95, "social_energy": 62, "intellectual_depth": 100, "emotional_openness": 75, "adventurousness": 68},
            "dating_style": "Warm, encouraging educator who loves explaining complex ideas clearly and listening with absolute patience.",
            "ideal_date": "Quiet afternoon at a university library cafe discussing computational ethics, followed by a classical music concert."
        }
    },
    {
        "id": "melanie-perkins",
        "name": "Melanie Perkins",
        "title": "Co-founder & CEO, Canva",
        "linkedin_url": "https://www.linkedin.com/in/melanieperkins",
        "instagram_url": "https://www.instagram.com/melanieperkins.canva",
        "avatar": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=400&q=80",
        "linkedin_summary": "Co-founder and CEO of Canva, empowering the world to design. One of the youngest female tech CEOs to build a multi-billion dollar global platform.",
        "instagram_summary": "Kitesurfing in Mauritius, Canva team magic celebrations, colorful graphic design art, eco-friendly philanthropy, travel photography, coastal views.",
        "analysis": {
            "needs": [
                "Creativity and appreciation for visual aesthetics & design simplicity",
                "Spirit of adventure (kitesurfing, exploring remote places)",
                "Commitment to doing good in the world"
            ],
            "hobbies": ["Kitesurfing", "Graphic Design & Typography", "Travel Photography", "Environmental Conservation", "Backpacking"],
            "interests": ["Visual Communication", "Democratizing Creativity", "Pledge 1% Philanthropy", "Sustainable Tech", "Product UX"],
            "qualities": ["Imaginative", "Determined", "Adventurous", "Generous", "Visionary"],
            "vibe_vector": {"ambition": 96, "social_energy": 82, "intellectual_depth": 90, "emotional_openness": 88, "adventurousness": 94},
            "dating_style": "Inspirational and visually expressive, loves dreaming up wild creative projects while pursuing thrilling outdoor sports.",
            "ideal_date": "Kitesurfing on a pristine beach followed by mood-boarding creative ideas over fresh coconut water."
        }
    },
    {
        "id": "brian-chesky",
        "name": "Brian Chesky",
        "title": "Co-founder & CEO, Airbnb",
        "linkedin_url": "https://www.linkedin.com/in/brianchesky",
        "instagram_url": "https://www.instagram.com/bchesky",
        "avatar": "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&w=400&q=80",
        "linkedin_summary": "Co-founder and CEO of Airbnb. Industrial designer by background (RISD). Pioneered global hospitality sharing economy and icon experiences.",
        "instagram_summary": "Living in Airbnb listings worldwide, golden retriever Sophie, industrial design sketches, iconic architecture tours, RISD reunion memories, founder retreats.",
        "analysis": {
            "needs": [
                "Passion for travel, hospitality, architecture, and interior design",
                "Love for dogs (Sophie the Golden Retriever)",
                "Openness to living nomadically and exploring unique spaces"
            ],
            "hobbies": ["Industrial Sketching", "Architectural Sightseeing", "Playing with Golden Retriever", "Weightlifting", "Curating Iconic Stays"],
            "interests": ["Hospitality Design", "Experience Economy", "Mid-Century Modern Architecture", "Industrial Design History", "Global Culture"],
            "qualities": ["Creative", "Detail-obsessed", "Hospitable", "Playful", "Bold"],
            "vibe_vector": {"ambition": 95, "social_energy": 85, "intellectual_depth": 92, "emotional_openness": 86, "adventurousness": 95},
            "dating_style": "Generous host who curates magical visual atmospheres and loves sharing stories about world travel and design.",
            "ideal_date": "Private tour of a landmark mid-century modern home followed by a surprise weekend stay in a treehouse architecture Airbnb."
        }
    },
    {
        "id": "justine-ezarik",
        "name": "Justine Ezarik",
        "title": "Creator (iJustine), Host & Author",
        "linkedin_url": "https://www.linkedin.com/in/justineezarik",
        "instagram_url": "https://www.instagram.com/ijustine",
        "avatar": "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=400&q=80",
        "linkedin_summary": "Digital creator pioneer (iJustine), tech video producer, host, best-selling author. Over 1 Billion views across YouTube and digital media platforms.",
        "instagram_summary": "Apple keynote reactions, drone photography, gaming setups, dog adventures, gadget unboxings, fitness ring stats, festival vlogs.",
        "analysis": {
            "needs": [
                "Playful companion who embraces technology, gaming, and content creation",
                "Spontaneity for outdoor video production and tech events",
                "High energy and enthusiasm for pop culture"
            ],
            "hobbies": ["Drone Videography", "Gaming & Streaming", "Tech Unboxing", "Dog Training", "Culinary Baking"],
            "interests": ["Consumer Gadgets", "Virtual Reality", "Digital Media Trends", "Video Editing", "Fitness Tech"],
            "qualities": ["Energetic", "Tech-savvy", "Optimistic", "Creative", "Fun-loving"],
            "vibe_vector": {"ambition": 88, "social_energy": 94, "intellectual_depth": 80, "emotional_openness": 90, "adventurousness": 89},
            "dating_style": "Lively, bubbly, and full of surprise tech gadgets to test together, making every outing feel like a fun vlog adventure.",
            "ideal_date": "Flying FPV drones in a scenic canyon, trying the latest VR multiplayer game, and finishing with dessert."
        }
    },
    {
        "id": "steven-bartlett",
        "name": "Steven Bartlett",
        "title": "Host of The Diary Of A CEO & Entrepreneur",
        "linkedin_url": "https://www.linkedin.com/in/stevenbartlett-1",
        "instagram_url": "https://www.instagram.com/steven",
        "avatar": "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=400&q=80",
        "linkedin_summary": "Founder of Social Chain, Flight Story & Thirdweb. Host of Europe's #1 podcast 'The Diary Of A CEO'. Dragon on BBC's Dragons' Den.",
        "instagram_summary": "Podcast studio deep talks, gym workouts, black turtleneck style, psychological insights, blue ocean strategy quotes, international keynote stages.",
        "analysis": {
            "needs": [
                "Deep psychological curiosity and willingness to discuss vulnerability",
                "High ambition and dedication to health, fitness, and continuous growth",
                "Sophisticated taste and quiet confidence"
            ],
            "hobbies": ["Fitness & Weightlifting", "Podcast Hosting", "Journaling", "Public Speaking", "Investing"],
            "interests": ["Behavioral Psychology", "Health Longevity", "Marketing Strategy", "Biotechnology", "Personal Development"],
            "qualities": ["Introspective", "Articulate", "Ambitious", "Empathetic", "Charismatic"],
            "vibe_vector": {"ambition": 97, "social_energy": 85, "intellectual_depth": 94, "emotional_openness": 92, "adventurousness": 80},
            "dating_style": "Asks probing psychological questions, creates an atmosphere of intimacy and vulnerability over candlelight.",
            "ideal_date": "Late night conversation in a dimly lit speakeasy discussing human behavior and personal evolution."
        }
    },
    {
        "id": "dr-andrew-huberman",
        "name": "Dr. Andrew Huberman",
        "title": "Neuroscientist & Host, Huberman Lab",
        "linkedin_url": "https://www.linkedin.com/in/andrewhuberman",
        "instagram_url": "https://www.instagram.com/hubermanlab",
        "avatar": "https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?auto=format&fit=crop&w=400&q=80",
        "linkedin_summary": "Tenured Professor of Neurobiology at Stanford University School of Medicine. Host of top-ranked health podcast Huberman Lab.",
        "instagram_summary": "Morning sunlight protocol reels, cold exposure tips, neuroscience lecture diagrams, weight training clips, bulldog appreciation, scientific research summaries.",
        "analysis": {
            "needs": [
                "Alignment on circadian biology, healthy sleep, and physical fitness",
                "Intellectual rigor and curiosity about human physiology and mental focus",
                "Grounded, nature-connected lifestyle with clear boundaries"
            ],
            "hobbies": ["Morning Sunlight Hikes", "Cold Plunging & Sauna", "Weight Training", "Skateboarding", "Reading Medical Papers"],
            "interests": ["Neuroplasticity", "Dopamine Optimization", "Sleep Science", "Visual Systems", "Behavioral Neuroscience"],
            "qualities": ["Disciplined", "Science-driven", "Articulate", "Grounded", "Intensely Focused"],
            "vibe_vector": {"ambition": 92, "social_energy": 70, "intellectual_depth": 99, "emotional_openness": 78, "adventurousness": 84},
            "dating_style": "Engaging scientific conversationalist who brings evidence-based wellness insight and deep focus to your interaction.",
            "ideal_date": "Early morning ocean view hike to catch the first light, followed by black coffee and a discussion on neuroplasticity."
        }
    },
    {
        "id": "serena-williams",
        "name": "Serena Williams",
        "title": "Tennis Champion & Managing Partner, Serena Ventures",
        "linkedin_url": "https://www.linkedin.com/in/serenawilliams",
        "instagram_url": "https://www.instagram.com/serenawilliams",
        "avatar": "https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?auto=format&fit=crop&w=400&q=80",
        "linkedin_summary": "23-time Grand Slam champion, founder of Serena Ventures investing in diverse founders, fashion designer (S by Serena), venture capitalist.",
        "instagram_summary": "High-fashion red carpets, family moments with Olympia & Adira, venture capital portfolio highlights, tennis court throwbacks, beauty line SYNCS.",
        "analysis": {
            "needs": [
                "Unwavering confidence and support for a legendary career & venture empire",
                "Deep family focus and joy in parenting",
                "Appreciation for high fashion, elegance, and competitive excellence"
            ],
            "hobbies": ["Fashion Design", "Nail Art", "Karaoke", "Dance", "Venture Capital Investing"],
            "interests": ["Diversity in VC", "High Fashion", "Sports Business", "Beauty Innovation", "Parenting"],
            "qualities": ["Fierce", "Gracious", "Iconic", "Passionate", "Unbeatable Drive"],
            "vibe_vector": {"ambition": 99, "social_energy": 90, "intellectual_depth": 88, "emotional_openness": 88, "adventurousness": 86},
            "dating_style": "Commands the room with warmth, high elegance, and inspiring confidence, while enjoying fun entertainment and family jokes.",
            "ideal_date": "Front row seats at Paris Fashion Week followed by private karaoke and champagne."
        }
    },
    {
        "id": "mrbeast",
        "name": "Jimmy Donaldson (MrBeast)",
        "title": "Founder, Beast Industries & Feastables",
        "linkedin_url": "https://www.linkedin.com/in/mrbeast",
        "instagram_url": "https://www.instagram.com/mrbeast",
        "avatar": "https://images.unsplash.com/photo-1527980965255-d3b416303d12?auto=format&fit=crop&w=400&q=80",
        "linkedin_summary": "Most subscribed creator on YouTube (300M+ subs). CEO of Beast Industries, founder of Feastables, Beast Philanthropy (built wells, homes, clinics globally).",
        "instagram_summary": "Insane video set builds, Feastables chocolate sampling in stores, philanthropic giveaways, team stunts, thumbnail testing marathons.",
        "analysis": {
            "needs": [
                "Partner who can handle extreme scale, non-stop creative work, and bold ideas",
                "Shared dedication to large-scale global philanthropy",
                "Fun-loving, adventurous attitude with zero cynicism"
            ],
            "hobbies": ["Thumbnail & Video Optimization", "Chocolate Recipe Tasting", "Theme Park Stunts", "Philanthropic Expeditions", "Gaming"],
            "interests": ["Viral Psychology", "Global Philanthropy", "Consumer Snack Brands", "Production Engineering", "Media Distribution"],
            "qualities": ["Hyper-ambitious", "Generous", "Obsessive", "Playful", "Direct"],
            "vibe_vector": {"ambition": 100, "social_energy": 95, "intellectual_depth": 85, "emotional_openness": 80, "adventurousness": 98},
            "dating_style": "Unstoppable enthusiasm, loves planning grand surprise activities, and brings genuine joy to helping others.",
            "ideal_date": "Renting out an entire amusement park for the night, followed by late-night Feastables chocolate tasting."
        }
    },
    {
        "id": "reid-hoffman",
        "name": "Reid Hoffman",
        "title": "Co-founder LinkedIn & Partner at Greylock",
        "linkedin_url": "https://www.linkedin.com/in/reidhoffman",
        "instagram_url": "https://www.instagram.com/reidhoffman",
        "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=400&q=80",
        "linkedin_summary": "Co-founder of LinkedIn, Partner at Greylock, board member of OpenAI. Co-author of Blitzscaling and Masters of Scale podcast host.",
        "instagram_summary": "Boardgame nights (Settlers of Catan), AI philosophy debates, podcast interviews with tech icons, book launches, Oxford philosophy memories.",
        "analysis": {
            "needs": [
                "Intellectual depth and enthusiasm for strategic thinking & philosophy",
                "Love for complex tabletop strategy board games",
                "Commitment to positive societal evolution through technology"
            ],
            "hobbies": ["Tabletop Strategy Boardgames", "Writing Books", "Philosophical Debates", "Hosting Salon Dinners", "Podcasting"],
            "interests": ["Blitzscaling", "AI Governance", "Network Effects", "Moral Philosophy", "Venture Capital"],
            "qualities": ["Intellectual Giant", "Warm Networker", "Strategic", "Generous", "Thoughtful"],
            "vibe_vector": {"ambition": 94, "social_energy": 80, "intellectual_depth": 99, "emotional_openness": 85, "adventurousness": 75},
            "dating_style": "Delightful conversationalist who connects disparate ideas across philosophy, tech, and human history over a strategic game.",
            "ideal_date": "Intimate salon dinner with great red wine followed by a competitive game of Settlers of Catan."
        }
    },
    {
        "id": "satya-nadella",
        "name": "Satya Nadella",
        "title": "Chairman & CEO, Microsoft",
        "linkedin_url": "https://www.linkedin.com/in/satyanadella",
        "instagram_url": "https://www.instagram.com/satyanadella",
        "avatar": "https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?auto=format&fit=crop&w=400&q=80",
        "linkedin_summary": "Chairman and CEO of Microsoft. Transformed company culture through empathy and growth mindset. Author of Hit Refresh.",
        "instagram_summary": "Cricket matches, poetry readings, Microsoft AI keynote moments, accessibility tech demos, family memories, leadership quotes.",
        "analysis": {
            "needs": [
                "Empathy, humility, and dedication to growth mindset",
                "Appreciation for poetry, literature, and international sports (Cricket)",
                "Calm, grounded wisdom during complex times"
            ],
            "hobbies": ["Cricket", "Reading Hyderabadi & Russian Poetry", "Family Time", "Tech Accessibility Advocacy", "Coffee Tasting"],
            "interests": ["Growth Mindset", "AI Transformation", "Empathy in Leadership", "Poetry & Literature", "Cricket History"],
            "qualities": ["Empathetic", "Wise", "Humble", "Transformational", "Calm"],
            "vibe_vector": {"ambition": 96, "social_energy": 72, "intellectual_depth": 97, "emotional_openness": 90, "adventurousness": 70},
            "dating_style": "Quietly inspiring, listens with profound empathy, and recites beautiful poetry over espresso.",
            "ideal_date": "Attending a high-stakes international Cricket match followed by a quiet evening sharing favorite classic poems."
        }
    },
    {
        "id": "reshma-saujani",
        "name": "Reshma Saujani",
        "title": "Founder, Girls Who Code & Moms First",
        "linkedin_url": "https://www.linkedin.com/in/reshmasaujani",
        "instagram_url": "https://www.instagram.com/reshmasaujani",
        "avatar": "https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?auto=format&fit=crop&w=400&q=80",
        "linkedin_summary": "Founder of Girls Who Code and Moms First. Author of 'Brave, Not Perfect'. Attorney, political advocate, champion for mothers and women in STEM.",
        "instagram_summary": "Advocacy rallies on Capitol Hill, family moments with sons, speaking on bravery over perfection, book signings, female leadership summits.",
        "analysis": {
            "needs": [
                "Unwavering support for social justice and female equality",
                "Embracing imperfection, vulnerability, and courage",
                "Active partnership in balancing parenting and systemic change"
            ],
            "hobbies": ["Advocacy Rallies", "Writing", "Public Speaking", "Family Board Game Nights", "Yoga"],
            "interests": ["Closing the Gender Gap in Tech", "Pay Equity & Childcare Reform", "Bravery vs Perfection", "Public Policy", "EdTech"],
            "qualities": ["Brave", "Passionate", "Tenacious", "Vulnerable", "Empowering"],
            "vibe_vector": {"ambition": 94, "social_energy": 90, "intellectual_depth": 91, "emotional_openness": 94, "adventurousness": 82},
            "dating_style": "Direct, uplifting, and deeply encouraging, urging you to be brave and pursue your boldest life goals.",
            "ideal_date": "Stroll through a modern art museum discussing systemic change, followed by cozy comfort food in Greenwich Village."
        }
    },
    {
        "id": "guy-raz",
        "name": "Guy Raz",
        "title": "Host of How I Built This & Podcaster",
        "linkedin_url": "https://www.linkedin.com/in/guyraz",
        "instagram_url": "https://www.instagram.com/guy.raz",
        "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=400&q=80",
        "linkedin_summary": "Award-winning reporter, host of NPR's 'How I Built This', 'TED Radio Hour', and 'Wisdom From The Top'. Co-founder of Built It Productions.",
        "instagram_summary": "Interviews with legendary founders, children's science podcast (Wow in the World) behind-the-scenes, acoustic guitar playing, vinyl records.",
        "analysis": {
            "needs": [
                "Curiosity for human origin stories, resilience, and storytelling",
                "Warmth, humor, and appreciation for music & vintage vinyl",
                "Grounded family life and playful curiosity"
            ],
            "hobbies": ["Acoustic Guitar", "Vinyl Record Collecting", "Cycling", "Storytelling", "Listening to Audio Documentaries"],
            "interests": ["Entrepreneurial Resilience", "Journalism & Media", "Children's Science Education", "Music History", "Audio Production"],
            "qualities": ["Curious", "Warm", "Master Storyteller", "Good Listener", "Empathetic"],
            "vibe_vector": {"ambition": 88, "social_energy": 86, "intellectual_depth": 93, "emotional_openness": 92, "adventurousness": 78},
            "dating_style": "Asks the most captivating questions about your origin story, making you feel like the protagonist of a bestseller.",
            "ideal_date": "Browsing an independent record shop for vintage vinyl, followed by wood-fired pizza and acoustic guitar tunes."
        }
    },
    {
        "id": "anne-wojcicki",
        "name": "Anne Wojcicki",
        "title": "Co-founder & CEO, 23andMe",
        "linkedin_url": "https://www.linkedin.com/in/annewojcicki",
        "instagram_url": "https://www.instagram.com/annewojcicki",
        "avatar": "https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&w=400&q=80",
        "linkedin_summary": "Co-founder and CEO of 23andMe, pioneering consumer genetics and preventive healthcare. Yale biology graduate, health tech leader.",
        "instagram_summary": "Rollerblading along Palo Alto trails, preventive health research, outdoor camping with kids, scientific genetics forums, relaxed low-key style.",
        "analysis": {
            "needs": [
                "Intellectual curiosity for human genetics and health autonomy",
                "Down-to-earth, unpretentious lifestyle (rollerblading, camping)",
                "Boldness to challenge conventional healthcare systems"
            ],
            "hobbies": ["Rollerblading", "Outdoor Camping", "Ice Hockey", "Gardening", "Genetic Research"],
            "interests": ["Consumer Genomics", "Preventive Medicine", "Biotech Innovation", "Public Health", "Longevity"],
            "qualities": ["Pioneering", "Down-to-earth", "Direct", "Scientific", "Unpretentious"],
            "vibe_vector": {"ambition": 95, "social_energy": 78, "intellectual_depth": 96, "emotional_openness": 84, "adventurousness": 88},
            "dating_style": "Refreshingly unpretentious, energetic, and scientifically curious about habits, biology, and health.",
            "ideal_date": "Rollerblading session along a coastal path followed by casual fish tacos and a chat on human longevity."
        }
    },
    {
        "id": "sam-altman",
        "name": "Sam Altman",
        "title": "CEO, OpenAI",
        "linkedin_url": "https://www.linkedin.com/in/samaltman",
        "instagram_url": "https://www.instagram.com/samaltman",
        "avatar": "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&w=400&q=80",
        "linkedin_summary": "CEO of OpenAI, former President of Y Combinator. Co-founder of Loopt, Worldcoin, investor in Helion Energy and Retro Biosciences.",
        "instagram_summary": "Napa Valley farm views, rare sports cars, AI policy summits, nuclear fusion reactors, quiet outdoor coffee mornings.",
        "analysis": {
            "needs": [
                "Someone who operates at high speed and thinks in centuries rather than years",
                "Quiet, private sanctuary to unwind from global tech spotlights",
                "Shared fascination with energy, intelligence, and humanity's future"
            ],
            "hobbies": ["Driving Fast Cars", "Farming & Agriculture", "Reading Sci-Fi Classics", "Tinkering with Hardware", "Hiking"],
            "interests": ["Artificial General Intelligence", "Clean Energy & Fusion", "Longevity Biotech", "Startup Acceleration", "Macro-History"],
            "qualities": ["Ultra-visionary", "Calm under pressure", "Decisive", "Intense", "Quietly Warm"],
            "vibe_vector": {"ambition": 100, "social_energy": 60, "intellectual_depth": 99, "emotional_openness": 72, "adventurousness": 90},
            "dating_style": "Unassuming yet intensely thoughtful; discusses universe-altering breakthroughs with calm composure.",
            "ideal_date": "Private drive in a vintage sports car to a serene Napa Valley orchard for espresso and sci-fi literature talks."
        }
    },
    {
        "id": "kevin-systrom",
        "name": "Kevin Systrom",
        "title": "Co-founder Instagram & Artifact",
        "linkedin_url": "https://www.linkedin.com/in/ksystrom",
        "instagram_url": "https://www.instagram.com/kevin",
        "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=400&q=80",
        "linkedin_summary": "Co-founder and former CEO of Instagram, co-founder of Artifact (AI news platform). Stanford Management Science & Engineering graduate.",
        "instagram_summary": "Artisanal espresso roasting, craft sourdough baking, fine wine collecting, vintage Leica photography, cycling through European mountains.",
        "analysis": {
            "needs": [
                "Deep appreciation for artisanal craftsmanship (coffee, wine, baking)",
                "Eye for fine visual aesthetic and photography",
                "Intellectual rigor combined with relaxed European-style leisure"
            ],
            "hobbies": ["Espresso Roasting & Brewing", "Sourdough Baking", "Vintage Leica Photography", "Road Cycling", "Fine Wine Tasting"],
            "interests": ["Visual Culture & Filters", "Machine Learning in News", "Artisanal Food Science", "Stanford Tech Legacy", "Typography"],
            "qualities": ["Artisanal", "Refined", "Meticulous", "Curious", "Aesthetically Driven"],
            "vibe_vector": {"ambition": 91, "social_energy": 70, "intellectual_depth": 94, "emotional_openness": 80, "adventurousness": 82},
            "dating_style": "Sophisticated and warm; delights in sharing perfectly pulled espresso shots and photography tips.",
            "ideal_date": "Morning photography walk with a Leica camera followed by pulling custom espresso shots and tasting fresh sourdough."
        }
    },
    {
        "id": "mike-krieger",
        "name": "Mike Krieger",
        "title": "Co-founder Instagram & Chief Product Officer, Anthropic",
        "linkedin_url": "https://www.linkedin.com/in/mikekrieger",
        "instagram_url": "https://www.instagram.com/mikeyk",
        "avatar": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=400&q=80",
        "linkedin_summary": "Co-founder & former CTO of Instagram, Chief Product Officer at Anthropic. Stanford Symbolic Systems graduate. Philanthropist (Open Research).",
        "instagram_summary": "Sous-vide culinary experiments, acoustic piano pieces, San Francisco parks with family, AI product design sketches, open-source philanthropy.",
        "analysis": {
            "needs": [
                "Cognitive synergy in understanding human-computer interaction",
                "Love for culinary arts, acoustic music, and home hospitality",
                "Gentle, humble, and thoughtful partnership"
            ],
            "hobbies": ["Sous-Vide Cooking", "Piano Playing", "Product Design", "Philanthropy", "Reading Sci-Fi"],
            "interests": ["Symbolic Systems & AI", "Human-Centric Software", "Effective Altruism", "Culinary Science", "Acoustic Music"],
            "qualities": ["Humble", "Brilliant Engineer", "Thoughtful", "Generous", "Musical"],
            "vibe_vector": {"ambition": 92, "social_energy": 68, "intellectual_depth": 97, "emotional_openness": 86, "adventurousness": 76},
            "dating_style": "Generous and detail-oriented host who cooks gourmet meals and plays soft piano while talking software elegance.",
            "ideal_date": "Home-cooked multi-course dinner paired with wine and live acoustic piano improvisations."
        }
    },
    {
        "id": "paul-graham",
        "name": "Paul Graham",
        "title": "Co-founder, Y Combinator & Essayist",
        "linkedin_url": "https://www.linkedin.com/in/paulgrahamyc",
        "instagram_url": "https://www.instagram.com/paulgraham_yc",
        "avatar": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?auto=format&fit=crop&w=400&q=80",
        "linkedin_summary": "Co-founder of Y Combinator, Viaweb. Renowned essayist on startups, programming (Lisp), painting, and intellectual curiosity. Harvard PhD.",
        "instagram_summary": "Oil paintings in progress, countryside walks in England, notebook drafts of essays, classic book stacks, quiet tea time reflections.",
        "analysis": {
            "needs": [
                "Unconventional independent thinker who questions consensus",
                "Appreciation for oil painting, literature, and quiet countryside living",
                "Deep intellectual honesty and clarity of expression"
            ],
            "hobbies": ["Oil Painting", "Writing Essays", "Walking in Countryside", "Lisp Programming", "Reading Classics"],
            "interests": ["Independent Thinking", "Startup Dynamics", "Art History", "Linguistic Clarity", "Intellectual History"],
            "qualities": ["Original Thinker", "Direct", "Artistic", "Insightful", "Unconventional"],
            "vibe_vector": {"ambition": 93, "social_energy": 55, "intellectual_depth": 100, "emotional_openness": 78, "adventurousness": 74},
            "dating_style": "Candid and intellectually refreshing; cuts through fluff to explore original insights about life and art.",
            "ideal_date": "Long afternoon walk in an English countryside village discussing independent thought, ending with tea and painting."
        }
    },
    {
        "id": "jimmy-fallon",
        "name": "Jimmy Fallon",
        "title": "Host of The Tonight Show Starring Jimmy Fallon",
        "linkedin_url": "https://www.linkedin.com/in/jimmyfallon",
        "instagram_url": "https://www.instagram.com/jimmyfallon",
        "avatar": "https://images.unsplash.com/photo-1527980965255-d3b416303d12?auto=format&fit=crop&w=400&q=80",
        "linkedin_summary": "Host of NBC's The Tonight Show. SNL alumnus, comedian, actor, Grammy & Emmy winner, children's book author.",
        "instagram_summary": "Lip sync battles, musical parodies, late night celebrity games, guitar improvisations, children's books (Your Baby's First Word Will Be DADA).",
        "analysis": {
            "needs": [
                "Joyful, play-filled spirit who loves musical humor and party games",
                "Warm emotional support to balance high-pressure daily television",
                "Family-centered warmth and child-like wonder"
            ],
            "hobbies": ["Guitar Parodies", "Party Board Games", "Writing Children's Books", "Cooking Italian Food", "Improv Comedy"],
            "interests": ["Musical Comedy", "Late Night Entertainment", "Pop Culture", "Children's Literature", "Classic Rock"],
            "qualities": ["Hilarious", "Playful", "Infectiously Enthusiastic", "Kind-hearted", "Musically Talented"],
            "vibe_vector": {"ambition": 90, "social_energy": 98, "intellectual_depth": 78, "emotional_openness": 94, "adventurousness": 85},
            "dating_style": "Endlessly funny and engaging; breaks into spontaneous guitar riffs and game shows on dates.",
            "ideal_date": "Making homemade pizza together followed by playing hilarious musical improv games on guitar."
        }
    }
]
