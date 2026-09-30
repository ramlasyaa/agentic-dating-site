import React from 'react';
import { X, Linkedin, Instagram, ExternalLink, Sparkles, Heart, Compass, ShieldCheck } from 'lucide-react';

export default function ProfileModal({ profile, onClose, onStartDate }) {
  if (!profile) return null;
  const { analysis } = profile;
  const vibe = analysis.vibe_vector || { ambition: 90, social_energy: 80, intellectual_depth: 88, emotional_openness: 85, adventurousness: 82 };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md animate-fade-in">
      <div className="glass-panel w-full max-w-2xl rounded-3xl overflow-hidden border border-pink-500/30 shadow-2xl relative max-h-[90vh] flex flex-col">
        
        {/* Close Button */}
        <button
          onClick={onClose}
          className="absolute top-4 right-4 z-10 w-9 h-9 rounded-full bg-slate-900/80 text-slate-400 hover:text-white flex items-center justify-center border border-slate-700 transition-colors"
        >
          <X className="w-5 h-5" />
        </button>

        {/* Modal Header */}
        <div className="p-6 md:p-8 bg-gradient-to-b from-pink-950/30 via-slate-900 to-slate-900 border-b border-slate-800 flex items-start gap-5">
          <img
            src={profile.avatar}
            alt={profile.name}
            className="w-20 h-20 md:w-24 md:h-24 rounded-3xl object-cover ring-4 ring-pink-500/40 shadow-xl"
          />
          <div className="flex-1 min-w-0 pr-6">
            <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full bg-pink-500/10 text-pink-400 text-xs font-bold border border-pink-500/20 mb-1">
              <ShieldCheck className="w-3.5 h-3.5" /> Agent Profile Active
            </span>
            <h2 className="text-2xl md:text-3xl font-black text-white">{profile.name}</h2>
            <p className="text-xs md:text-sm text-slate-400 font-medium mb-3">{profile.title}</p>
            
            <div className="flex items-center gap-3">
              <a
                href={profile.linkedin_url}
                target="_blank"
                rel="noreferrer"
                className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-blue-500/10 text-blue-400 border border-blue-500/20 text-xs font-bold hover:bg-blue-500/20 transition-colors"
              >
                <Linkedin className="w-3.5 h-3.5" />
                <span>LinkedIn</span>
                <ExternalLink className="w-2.5 h-2.5 opacity-60" />
              </a>

              <a
                href={profile.instagram_url}
                target="_blank"
                rel="noreferrer"
                className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-gradient-to-r from-pink-500/10 to-rose-500/10 text-pink-400 border border-pink-500/20 text-xs font-bold hover:bg-pink-500/20 transition-colors"
              >
                <Instagram className="w-3.5 h-3.5" />
                <span>Instagram</span>
                <ExternalLink className="w-2.5 h-2.5 opacity-60" />
              </a>
            </div>
          </div>
        </div>

        {/* Modal Scrollable Content */}
        <div className="p-6 md:p-8 space-y-6 overflow-y-auto flex-1">
          
          {/* Ideal Date Quote */}
          <div className="bg-slate-900/90 p-4 rounded-2xl border border-pink-500/20">
            <div className="flex items-center gap-1.5 text-xs font-bold text-pink-400 uppercase tracking-wider mb-1">
              <Compass className="w-4 h-4" />
              <span>Agent's Ideal Date Concept</span>
            </div>
            <p className="text-xs md:text-sm text-slate-200 italic leading-relaxed">
              "{analysis.ideal_date}"
            </p>
          </div>

          {/* Dual Source Summaries */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="bg-slate-900/60 p-4 rounded-2xl border border-slate-800">
              <span className="text-xs font-bold text-blue-400 uppercase tracking-wider block mb-1">LinkedIn Summary</span>
              <p className="text-xs text-slate-300 leading-relaxed">{profile.linkedin_summary}</p>
            </div>

            <div className="bg-slate-900/60 p-4 rounded-2xl border border-slate-800">
              <span className="text-xs font-bold text-pink-400 uppercase tracking-wider block mb-1">Instagram Vibe Summary</span>
              <p className="text-xs text-slate-300 leading-relaxed">{profile.instagram_summary}</p>
            </div>
          </div>

          {/* Extracted Needs */}
          <div className="bg-slate-900/60 p-4 rounded-2xl border border-slate-800">
            <span className="text-xs font-bold text-slate-300 uppercase tracking-wider block mb-2">Agent Extracted Needs</span>
            <ul className="space-y-2">
              {analysis.needs.map((n, i) => (
                <li key={i} className="text-xs text-slate-300 flex items-start gap-2">
                  <span className="text-pink-400 font-bold">•</span>
                  <span>{n}</span>
                </li>
              ))}
            </ul>
          </div>

          {/* Hobbies & Qualities */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <span className="text-xs font-bold text-slate-400 uppercase tracking-wider block mb-2">Hobbies & Interests</span>
              <div className="flex flex-wrap gap-1.5">
                {analysis.hobbies.map((h, i) => (
                  <span key={i} className="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-200 text-xs font-medium border border-slate-700">
                    {h}
                  </span>
                ))}
              </div>
            </div>

            <div>
              <span className="text-xs font-bold text-slate-400 uppercase tracking-wider block mb-2">Core Qualities</span>
              <div className="flex flex-wrap gap-1.5">
                {analysis.qualities.map((q, i) => (
                  <span key={i} className="px-2.5 py-1 rounded-lg bg-rose-950/40 text-rose-300 text-xs font-medium border border-rose-800/40">
                    ✨ {q}
                  </span>
                ))}
              </div>
            </div>
          </div>

        </div>

        {/* Modal Footer Action */}
        <div className="p-6 bg-slate-900/90 border-t border-slate-800 flex items-center justify-between gap-4">
          <button
            onClick={onClose}
            className="px-5 py-2.5 rounded-xl bg-slate-800 text-slate-300 text-xs font-bold hover:bg-slate-700 transition-colors"
          >
            Close Profile
          </button>

          <button
            onClick={() => {
              onClose();
              onStartDate(profile);
            }}
            className="flex-1 py-3 rounded-xl bg-gradient-to-r from-pink-600 to-rose-600 text-white text-xs font-bold shadow-lg shadow-pink-600/30 hover:scale-[1.02] active:scale-[0.98] transition-all flex items-center justify-center gap-2"
          >
            <Heart className="w-4 h-4 fill-white" />
            <span>Simulate Date With {profile.name}'s Agent</span>
          </button>
        </div>

      </div>
    </div>
  );
}
