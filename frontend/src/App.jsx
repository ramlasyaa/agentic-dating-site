import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import ProfileCard from './components/ProfileCard';
import DateSimulator from './components/DateSimulator';
import RankingsView from './components/RankingsView';
import LinkIngestion from './components/LinkIngestion';
import { Heart, Sparkles, Search, Linkedin, Instagram, Award, MessageCircle, ArrowRight } from 'lucide-react';

export default function App() {
  const [profiles, setProfiles] = useState([]);
  const [rankings, setRankings] = useState({});
  const [activeTab, setActiveTab] = useState('profiles');
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedP1, setSelectedP1] = useState(null);
  const [selectedP2, setSelectedP2] = useState(null);
  const [dateResult, setDateResult] = useState(null);
  const [loading, setLoading] = useState(false);

  // Fetch profiles and initial data on mount
  useEffect(() => {
    fetchInitialData();
  }, []);

  const fetchInitialData = async () => {
    try {
      const res = await fetch('/api/demo');
      if (res.ok) {
        const data = await res.json();
        setProfiles(data.profiles);
        setRankings(data.rankings);
        if (data.sample_dates && data.sample_dates.length > 0) {
          setDateResult(data.sample_dates[0]);
        }
      }
    } catch (e) {
      console.log('Failed to fetch from backend API, using local fallbacks if needed.', e);
    }
  };

  const handleStartDate = async (p1Id, p2Id, venueName) => {
    setLoading(true);
    try {
      const res = await fetch('/api/date', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ person1_id: p1Id, person2_id: p2Id, venue_name: venueName }),
      });
      if (res.ok) {
        const result = await res.json();
        setDateResult(result);
        setActiveTab('date-arena');
      }
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleSelectForDateFromCard = (p1) => {
    setSelectedP1(p1);
    // Find a good match for p2
    const p1Rankings = rankings[p1.id];
    if (p1Rankings && p1Rankings.length > 0) {
      const topMatchId = p1Rankings[0].match_person_id;
      const topMatch = profiles.find((p) => p.id === topMatchId);
      setSelectedP2(topMatch);
      handleStartDate(p1.id, topMatchId);
    } else {
      const other = profiles.find((p) => p.id !== p1.id);
      setSelectedP2(other);
      handleStartDate(p1.id, other.id);
    }
  };

  const handleViewRankingsFromCard = (p) => {
    setSelectedP1(p);
    setActiveTab('rankings');
  };

  const handleSelectPersonForDateFromRankings = (p1Id, p2Id) => {
    const p1 = profiles.find((p) => p.id === p1Id);
    const p2 = profiles.find((p) => p.id === p2Id);
    setSelectedP1(p1);
    setSelectedP2(p2);
    handleStartDate(p1Id, p2Id);
  };

  const handleIngestSuccess = (newProfile, newRankings) => {
    setProfiles((prev) => [newProfile, ...prev]);
    fetchInitialData();
  };

  const handleRunDemo = () => {
    setActiveTab('date-arena');
    if (profiles.length >= 2) {
      handleStartDate(profiles[0].id, profiles[1].id);
    }
  };

  const filteredProfiles = profiles.filter(
    (p) =>
      p.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
      p.title.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <div className="min-h-screen bg-[#090d16] text-slate-100 flex flex-col font-['Plus_Jakarta_Sans',sans-serif]">
      
      {/* Sticky Header */}
      <Navbar
        activeTab={activeTab}
        setActiveTab={setActiveTab}
        profileCount={profiles.length}
        onRunDemo={handleRunDemo}
      />

      {/* Main Container */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-10">
        
        {/* Hero Section */}
        <div className="relative glass-panel p-8 md:p-12 rounded-3xl overflow-hidden border border-slate-800">
          <div className="absolute top-0 right-0 -mt-12 -mr-12 w-96 h-96 bg-gradient-to-br from-pink-500/20 via-purple-500/10 to-transparent rounded-full blur-3xl pointer-events-none" />
          
          <div className="max-w-3xl relative z-10 space-y-4">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-pink-500/10 text-pink-400 border border-pink-500/20 text-xs font-extrabold uppercase tracking-wider">
              <Sparkles className="w-3.5 h-3.5" />
              <span>Two Official Sources: LinkedIn + Public Instagram</span>
            </div>

            <h1 className="text-4xl md:text-5xl font-black tracking-tight text-white leading-tight">
              Agents Date On Their Behalf.{' '}
              <span className="bg-gradient-to-r from-pink-400 via-rose-400 to-purple-400 bg-clip-text text-transparent">
                The Agents Date Each Other.
              </span>
            </h1>

            <p className="text-sm md:text-base text-slate-300 leading-relaxed font-medium">
              We analyze exactly two official public links for every person—their <strong className="text-blue-400 font-bold">LinkedIn</strong> (career, achievements, values) and public <strong className="text-pink-400 font-bold">Instagram</strong> (hobbies, aesthetic, vibe). Their autonomous agents date in realistic scenarios and generate ranking reports.
            </p>

            <div className="flex flex-wrap items-center gap-3 pt-2">
              <button
                onClick={() => setActiveTab('date-arena')}
                className="px-5 py-3 rounded-2xl bg-gradient-to-r from-pink-600 via-rose-600 to-purple-600 text-white font-bold text-sm shadow-xl shadow-pink-600/30 hover:scale-[1.02] active:scale-[0.98] transition-all flex items-center gap-2"
              >
                <Heart className="w-4 h-4 fill-white" />
                <span>Watch Agents Date (Live Arena)</span>
              </button>

              <button
                onClick={() => setActiveTab('add-links')}
                className="px-5 py-3 rounded-2xl bg-slate-900 border border-slate-700 text-slate-200 font-bold text-sm hover:bg-slate-800 transition-all flex items-center gap-2"
              >
                <span>Paste Your Own Links</span>
                <ArrowRight className="w-4 h-4" />
              </button>
            </div>
          </div>
        </div>

        {/* Tab Content Rendering */}

        {/* TAB 1: 25 PROFILES */}
        {activeTab === 'profiles' && (
          <div className="space-y-6">
            
            {/* Filter Bar */}
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
              <div>
                <h2 className="text-2xl font-extrabold text-white flex items-center gap-2">
                  <span>25 Real People Profiles</span>
                  <span className="text-xs font-bold px-2.5 py-0.5 rounded-full bg-pink-500/10 text-pink-400 border border-pink-500/20">
                    Verified LinkedIn + Instagram
                  </span>
                </h2>
                <p className="text-xs text-slate-400">
                  Inspect the agent analysis for each real person: extracted Needs, Hobbies, Interests, and Core Qualities.
                </p>
              </div>

              {/* Search Box */}
              <div className="relative w-full sm:w-72">
                <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2" />
                <input
                  type="text"
                  placeholder="Search by name or role..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="w-full bg-slate-900 border border-slate-800 rounded-xl pl-10 pr-4 py-2 text-xs text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-pink-500"
                />
              </div>
            </div>

            {/* Grid of Profiles */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {filteredProfiles.map((profile) => (
                <ProfileCard
                  key={profile.id}
                  profile={profile}
                  onStartDate={() => handleSelectForDateFromCard(profile)}
                  onViewRankings={() => handleViewRankingsFromCard(profile)}
                />
              ))}
            </div>

          </div>
        )}

        {/* TAB 2: AGENT DATE ARENA */}
        {activeTab === 'date-arena' && (
          <DateSimulator
            profiles={profiles}
            initialP1={selectedP1}
            initialP2={selectedP2}
            onRunDate={handleStartDate}
            dateResult={dateResult}
            loading={loading}
          />
        )}

        {/* TAB 3: COMPATIBILITY RANKINGS */}
        {activeTab === 'rankings' && (
          <RankingsView
            profiles={profiles}
            rankings={rankings}
            onSelectPersonForDate={handleSelectPersonForDateFromRankings}
          />
        )}

        {/* TAB 4: ADD LINKS */}
        {activeTab === 'add-links' && (
          <LinkIngestion onIngestSuccess={handleIngestSuccess} />
        )}

      </main>

      {/* Footer */}
      <footer className="glass-panel border-t border-slate-800/80 mt-16 py-8">
        <div className="max-w-7xl mx-auto px-4 text-center space-y-2">
          <p className="text-xs text-slate-400 font-medium">
            <strong>Aura</strong> — Agentic Dating Site • Dual Sources: Public LinkedIn + Public Instagram
          </p>
          <p className="text-[11px] text-slate-500">
            Agents date on their behalf • Multi-turn Date Harness • Dynamic Compatibility Matrix
          </p>
        </div>
      </footer>

    </div>
  );
}
