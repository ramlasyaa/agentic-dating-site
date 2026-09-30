import React, { useState } from 'react';
import { Award, Heart, Sparkles, Linkedin, Instagram, ExternalLink, Flame } from 'lucide-react';

export default function RankingsView({ profiles, rankings, onSelectPersonForDate }) {
  const [selectedPersonId, setSelectedPersonId] = useState(profiles[0]?.id || '');

  const person = profiles.find((p) => p.id === selectedPersonId) || profiles[0];
  const personRankings = rankings[selectedPersonId] || [];

  return (
    <div className="max-w-6xl mx-auto space-y-8">
      
      {/* Selection Banner */}
      <div className="glass-panel p-6 rounded-3xl border border-slate-800">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
          
          <div>
            <div className="flex items-center gap-2 text-amber-400 font-bold text-xs uppercase tracking-wider mb-1">
              <Award className="w-4 h-4" />
              <span>Agent Compatibility Leaderboard</span>
            </div>
            <h2 className="text-2xl font-extrabold text-white">Who Fits Each Person Best</h2>
            <p className="text-xs text-slate-400 mt-1">
              Select any person to view their complete compatibility rankings based on agent analysis & dating harness results.
            </p>
          </div>

          {/* Select Person Dropdown */}
          <div className="flex items-center gap-3">
            <span className="text-xs font-semibold text-slate-300">Viewing Rankings For:</span>
            <select
              value={selectedPersonId}
              onChange={(e) => setSelectedPersonId(e.target.value)}
              className="bg-slate-900 border border-slate-700 text-slate-100 text-sm font-bold rounded-xl px-4 py-2.5 focus:ring-2 focus:ring-pink-500 focus:outline-none"
            >
              {profiles.map((p) => (
                <option key={p.id} value={p.id}>
                  {p.name} ({p.title.split(',')[0]})
                </option>
              ))}
            </select>
          </div>

        </div>
      </div>

      {/* Selected Person Summary Card */}
      {person && (
        <div className="glass-card p-6 rounded-3xl border border-pink-500/20 flex flex-col md:flex-row items-center justify-between gap-6">
          <div className="flex items-center gap-4">
            <img
              src={person.avatar}
              alt={person.name}
              className="w-20 h-20 rounded-2xl object-cover ring-4 ring-pink-500/40"
            />
            <div>
              <div className="flex items-center gap-2 mb-1">
                <h3 className="text-xl font-extrabold text-white">{person.name}</h3>
                <span className="px-2.5 py-0.5 rounded-full bg-pink-500/10 text-pink-400 text-xs font-bold border border-pink-500/20">
                  Target Person
                </span>
              </div>
              <p className="text-xs text-slate-400 mb-2">{person.title}</p>
              
              <div className="flex items-center gap-2">
                <a href={person.linkedin_url} target="_blank" rel="noreferrer" className="text-xs text-blue-400 flex items-center gap-1 hover:underline">
                  <Linkedin className="w-3.5 h-3.5" /> LinkedIn
                </a>
                <span className="text-slate-600">•</span>
                <a href={person.instagram_url} target="_blank" rel="noreferrer" className="text-xs text-pink-400 flex items-center gap-1 hover:underline">
                  <Instagram className="w-3.5 h-3.5" /> Instagram
                </a>
              </div>
            </div>
          </div>

          <div className="bg-slate-900/80 p-4 rounded-2xl border border-slate-800 max-w-md w-full">
            <span className="text-xs font-bold text-slate-400 uppercase tracking-wider block mb-1">Extracted Needs Summary</span>
            <p className="text-xs text-slate-300 italic">
              "{person.analysis.needs[0]}"
            </p>
          </div>
        </div>
      )}

      {/* Rankings Grid */}
      <div className="space-y-4">
        <h3 className="text-lg font-bold text-white flex items-center gap-2">
          <span>Ranked Matches for {person?.name}</span>
          <span className="text-xs text-slate-400 font-normal">({personRankings.length} Candidates Evaluated)</span>
        </h3>

        <div className="grid grid-cols-1 gap-4">
          {personRankings.map((match) => {
            const isTop3 = match.rank <= 3;
            return (
              <div
                key={match.match_person_id}
                className={`glass-card p-5 rounded-2xl border transition-all ${
                  match.rank === 1
                    ? 'border-amber-500/40 bg-gradient-to-r from-amber-500/10 via-slate-900 to-slate-900 shadow-lg shadow-amber-500/10'
                    : isTop3
                    ? 'border-pink-500/30'
                    : 'border-slate-800/80'
                }`}
              >
                <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
                  
                  {/* Left: Rank Badge + Profile Info */}
                  <div className="flex items-center gap-4">
                    <div className={`w-12 h-12 rounded-xl flex items-center justify-center font-extrabold text-base ${
                      match.rank === 1
                        ? 'bg-amber-500 text-slate-950 shadow-md shadow-amber-500/30 ring-2 ring-amber-300'
                        : match.rank === 2
                        ? 'bg-slate-300 text-slate-950'
                        : match.rank === 3
                        ? 'bg-amber-700 text-white'
                        : 'bg-slate-800 text-slate-400'
                    }`}>
                      #{match.rank}
                    </div>

                    <img src={match.avatar} alt={match.name} className="w-14 h-14 rounded-xl object-cover" />

                    <div>
                      <h4 className="text-base font-bold text-white flex items-center gap-2">
                        <span>{match.name}</span>
                        {match.rank === 1 && (
                          <span className="text-[10px] uppercase font-extrabold px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">
                            ★ Best Fit Match
                          </span>
                        )}
                      </h4>
                      <p className="text-xs text-slate-400">{match.title}</p>
                      
                      <div className="flex flex-wrap gap-1.5 mt-2">
                        {match.hobbies.map((h, i) => (
                          <span key={i} className="text-[10px] px-2 py-0.5 rounded bg-slate-800 text-slate-300">
                            {h}
                          </span>
                        ))}
                      </div>
                    </div>
                  </div>

                  {/* Middle: Shared Needs & Rationale */}
                  <div className="flex-1 max-w-md bg-slate-950/60 p-3 rounded-xl border border-slate-800/60 text-xs text-slate-300">
                    <span className="text-pink-400 font-bold block mb-1">Why They Fit Best:</span>
                    <p className="line-clamp-2">{match.shared_needs[0]}</p>
                  </div>

                  {/* Right: Compatibility Score & Action Button */}
                  <div className="flex items-center gap-4 justify-between md:justify-end">
                    <div className="text-right">
                      <div className="text-2xl font-black text-pink-400 flex items-center gap-1">
                        <Flame className="w-5 h-5 fill-pink-500 text-pink-500" />
                        <span>{match.score}%</span>
                      </div>
                      <span className="text-[10px] text-slate-400 uppercase font-semibold">Match Score</span>
                    </div>

                    <button
                      onClick={() => onSelectPersonForDate(person.id, match.match_person_id)}
                      className="px-4 py-2 rounded-xl bg-pink-600/20 text-pink-300 border border-pink-500/30 text-xs font-bold hover:bg-pink-600 hover:text-white transition-all flex items-center gap-1.5"
                    >
                      <Heart className="w-3.5 h-3.5 fill-pink-400" />
                      <span>Watch Date</span>
                    </button>
                  </div>

                </div>
              </div>
            );
          })}
        </div>

      </div>

    </div>
  );
}
