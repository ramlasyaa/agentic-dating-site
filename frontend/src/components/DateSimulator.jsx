import React, { useState, useEffect } from 'react';
import { Heart, Play, RefreshCw, Sparkles, MapPin, CheckCircle2, MessageSquare, Flame } from 'lucide-react';

const VENUES = [
  { name: 'Dimly Lit Speakeasy Cocktail Lounge', icon: '🍸' },
  { name: 'Architectural Espresso & Matcha Bar', icon: '☕' },
  { name: 'Contemporary Art Gallery & Wine Lounge', icon: '🎨' },
  { name: 'Sunset Coastal Walk & Taco Stand', icon: '🌮' },
];

export default function DateSimulator({ profiles, initialP1, initialP2, onRunDate, dateResult, loading }) {
  const [p1Id, setP1Id] = useState(initialP1?.id || profiles[0]?.id || '');
  const [p2Id, setP2Id] = useState(initialP2?.id || profiles[1]?.id || '');
  const [venue, setVenue] = useState(VENUES[0].name);
  const [activeTurn, setActiveTurn] = useState(0);
  const [autoPlay, setAutoPlay] = useState(false);

  const p1 = profiles.find((p) => p.id === p1Id) || profiles[0];
  const p2 = profiles.find((p) => p.id === p2Id) || profiles[1];

  useEffect(() => {
    if (dateResult?.turns) {
      setActiveTurn(dateResult.turns.length - 1);
    }
  }, [dateResult]);

  const handleStartSim = () => {
    if (p1Id === p2Id) return;
    onRunDate(p1Id, p2Id, venue);
  };

  return (
    <div className="max-w-6xl mx-auto space-y-8">
      
      {/* Top Banner / Selection Bar */}
      <div className="glass-panel p-6 rounded-3xl border border-slate-800">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
          
          <div>
            <div className="flex items-center gap-2 text-pink-400 font-bold text-xs uppercase tracking-wider mb-1">
              <Sparkles className="w-4 h-4" />
              <span>Live Agent Dating Harness</span>
            </div>
            <h2 className="text-2xl font-extrabold text-white">Watch Agents Date Each Other</h2>
            <p className="text-xs text-slate-400 mt-1">
              Select two people. Their autonomous agents will date on their behalf and report back.
            </p>
          </div>

          {/* Selectors */}
          <div className="flex flex-wrap items-center gap-3">
            
            {/* Person 1 Selector */}
            <select
              value={p1Id}
              onChange={(e) => setP1Id(e.target.value)}
              className="bg-slate-900 border border-slate-700 text-slate-200 text-xs font-semibold rounded-xl px-3 py-2.5 focus:ring-2 focus:ring-pink-500 focus:outline-none"
            >
              {profiles.map((p) => (
                <option key={p.id} value={p.id} disabled={p.id === p2Id}>
                  Agent 1: {p.name}
                </option>
              ))}
            </select>

            <span className="text-pink-500 font-extrabold text-sm">⚡</span>

            {/* Person 2 Selector */}
            <select
              value={p2Id}
              onChange={(e) => setP2Id(e.target.value)}
              className="bg-slate-900 border border-slate-700 text-slate-200 text-xs font-semibold rounded-xl px-3 py-2.5 focus:ring-2 focus:ring-pink-500 focus:outline-none"
            >
              {profiles.map((p) => (
                <option key={p.id} value={p.id} disabled={p.id === p1Id}>
                  Agent 2: {p.name}
                </option>
              ))}
            </select>

            {/* Venue Selector */}
            <select
              value={venue}
              onChange={(e) => setVenue(e.target.value)}
              className="bg-slate-900 border border-slate-700 text-slate-200 text-xs font-semibold rounded-xl px-3 py-2.5 focus:ring-2 focus:ring-purple-500 focus:outline-none"
            >
              {VENUES.map((v) => (
                <option key={v.name} value={v.name}>
                  {v.icon} {v.name}
                </option>
              ))}
            </select>

            {/* Run Button */}
            <button
              onClick={handleStartSim}
              disabled={loading || p1Id === p2Id}
              className="flex items-center gap-2 px-5 py-2.5 rounded-xl bg-gradient-to-r from-pink-600 via-rose-600 to-purple-600 text-white font-bold text-sm shadow-lg shadow-pink-600/30 hover:scale-[1.03] active:scale-[0.97] transition-all disabled:opacity-50"
            >
              {loading ? (
                <>
                  <RefreshCw className="w-4 h-4 animate-spin" />
                  <span>Dating in Progress...</span>
                </>
              ) : (
                <>
                  <Play className="w-4 h-4 fill-white" />
                  <span>Start Date Simulation</span>
                </>
              )}
            </button>

          </div>

        </div>
      </div>

      {/* Date Arena Visualizer */}
      {dateResult && (
        <div className="space-y-6">
          
          {/* Couple Stage Bar */}
          <div className="glass-panel p-6 rounded-3xl relative overflow-hidden border border-pink-500/20">
            <div className="flex flex-col md:flex-row items-center justify-between gap-6">
              
              {/* Agent 1 Header */}
              <div className="flex items-center gap-4">
                <img
                  src={dateResult.person_1.avatar}
                  alt={dateResult.person_1.name}
                  className="w-16 h-16 rounded-2xl object-cover ring-4 ring-pink-500/40"
                />
                <div>
                  <span className="text-xs font-bold text-pink-400 uppercase tracking-wider block">Representing</span>
                  <h3 className="text-xl font-extrabold text-white">{dateResult.person_1.name}</h3>
                  <p className="text-xs text-slate-400">{dateResult.person_1.title}</p>
                </div>
              </div>

              {/* Chemistry Central Indicator */}
              <div className="flex flex-col items-center justify-center text-center">
                <div className="flex items-center gap-2 text-amber-400 text-xs font-bold uppercase tracking-wider mb-1">
                  <Flame className="w-4 h-4 fill-amber-400" />
                  <span>Live Date Chemistry</span>
                </div>
                <div className="text-4xl font-black bg-gradient-to-r from-pink-400 via-rose-400 to-purple-400 bg-clip-text text-transparent">
                  {dateResult.compatibility.overall_score}%
                </div>
                <span className="text-xs text-slate-400 font-medium mt-1 flex items-center gap-1">
                  <MapPin className="w-3 h-3 text-pink-400" /> {dateResult.venue.name}
                </span>
              </div>

              {/* Agent 2 Header */}
              <div className="flex items-center gap-4">
                <div className="text-right">
                  <span className="text-xs font-bold text-purple-400 uppercase tracking-wider block">Representing</span>
                  <h3 className="text-xl font-extrabold text-white">{dateResult.person_2.name}</h3>
                  <p className="text-xs text-slate-400">{dateResult.person_2.title}</p>
                </div>
                <img
                  src={dateResult.person_2.avatar}
                  alt={dateResult.person_2.name}
                  className="w-16 h-16 rounded-2xl object-cover ring-4 ring-purple-500/40"
                />
              </div>

            </div>
          </div>

          {/* Turn-by-Turn Conversation Script */}
          <div className="glass-panel p-6 rounded-3xl border border-slate-800 space-y-4">
            <div className="flex items-center justify-between border-b border-slate-800 pb-3">
              <div className="flex items-center gap-2 font-bold text-slate-200 text-sm">
                <MessageSquare className="w-4 h-4 text-pink-400" />
                <span>Live Date Dialogue & Banter</span>
              </div>
              <span className="text-xs text-slate-400">Turn-by-turn Agent Interaction</span>
            </div>

            <div className="space-y-4 pt-2">
              {dateResult.turns.map((turn, index) => {
                const isP1 = turn.speaker === dateResult.person_1.id;
                return (
                  <div
                    key={index}
                    className={`flex items-start gap-3 ${isP1 ? 'flex-row' : 'flex-row-reverse'}`}
                  >
                    <img
                      src={turn.avatar}
                      alt={turn.speaker_name}
                      className="w-10 h-10 rounded-xl object-cover ring-2 ring-slate-700 mt-1"
                    />

                    <div className={`max-w-xl p-4 rounded-2xl ${
                      isP1
                        ? 'bg-slate-900/90 border border-pink-500/30 text-slate-100 rounded-tl-none'
                        : 'bg-purple-950/40 border border-purple-500/30 text-slate-100 rounded-tr-none'
                    }`}>
                      <div className="flex items-center justify-between gap-4 mb-1">
                        <span className="text-xs font-bold text-slate-300">{turn.speaker_name}'s Agent</span>
                        <span className="text-[10px] px-2 py-0.5 rounded-full bg-slate-800 text-pink-300 font-medium">
                          Vibe: {turn.vibe_meter}% • {turn.sentiment}
                        </span>
                      </div>
                      <p className="text-sm leading-relaxed text-slate-200">{turn.text}</p>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>

          {/* Agent Post-Date Debrief Reports */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            
            {/* Debrief 1 */}
            <div className="glass-card p-6 rounded-3xl border border-pink-500/20">
              <div className="flex items-center gap-3 mb-3">
                <img src={dateResult.person_1.avatar} className="w-10 h-10 rounded-xl object-cover" />
                <div>
                  <h4 className="text-sm font-bold text-white">Agent Report to {dateResult.person_1.name}</h4>
                  <span className="text-[11px] text-pink-400 font-medium">Post-Date Confidential Summary</span>
                </div>
              </div>
              <p className="text-xs text-slate-300 leading-relaxed bg-slate-900/80 p-3.5 rounded-2xl border border-slate-800">
                "{dateResult.agent_debriefs[dateResult.person_1.id]}"
              </p>
            </div>

            {/* Debrief 2 */}
            <div className="glass-card p-6 rounded-3xl border border-purple-500/20">
              <div className="flex items-center gap-3 mb-3">
                <img src={dateResult.person_2.avatar} className="w-10 h-10 rounded-xl object-cover" />
                <div>
                  <h4 className="text-sm font-bold text-white">Agent Report to {dateResult.person_2.name}</h4>
                  <span className="text-[11px] text-purple-400 font-medium">Post-Date Confidential Summary</span>
                </div>
              </div>
              <p className="text-xs text-slate-300 leading-relaxed bg-slate-900/80 p-3.5 rounded-2xl border border-slate-800">
                "{dateResult.agent_debriefs[dateResult.person_2.id]}"
              </p>
            </div>

          </div>

        </div>
      )}

    </div>
  );
}
