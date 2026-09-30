import React from 'react';
import { Linkedin, Instagram, Heart, ExternalLink, Sparkles, Award } from 'lucide-react';

export default function ProfileCard({ profile, onSelectProfile, onStartDate, onViewRankings }) {
  const { analysis } = profile;

  return (
    <div className="glass-card rounded-3xl p-6 flex flex-col justify-between transition-all duration-300 hover:-translate-y-1 relative group overflow-hidden">
      {/* Decorative gradient glow background */}
      <div className="absolute top-0 right-0 w-32 h-32 bg-pink-500/10 rounded-full blur-2xl group-hover:bg-pink-500/20 transition-all pointer-events-none" />

      <div>
        {/* Profile Header */}
        <div className="flex items-start gap-4 mb-4">
          <div className="relative">
            <img
              src={profile.avatar}
              alt={profile.name}
              className="w-16 h-16 rounded-2xl object-cover ring-2 ring-slate-700/60 group-hover:ring-pink-500/50 transition-all"
            />
            <span className="absolute -bottom-1 -right-1 w-5 h-5 bg-emerald-500 border-2 border-slate-900 rounded-full flex items-center justify-center" title="Agent Active">
              <span className="w-1.5 h-1.5 bg-white rounded-full animate-ping" />
            </span>
          </div>
          
          <div className="flex-1 min-w-0">
            <h3 className="text-lg font-bold text-white truncate group-hover:text-pink-300 transition-colors">
              {profile.name}
            </h3>
            <p className="text-xs text-slate-400 font-medium truncate mb-2">{profile.title}</p>
            
            {/* The Two Official Links */}
            <div className="flex items-center gap-2">
              <a
                href={profile.linkedin_url}
                target="_blank"
                rel="noreferrer"
                className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-blue-500/10 text-blue-400 border border-blue-500/20 text-xs font-semibold hover:bg-blue-500/20 transition-colors"
                title="Official LinkedIn Profile"
              >
                <Linkedin className="w-3.5 h-3.5" />
                <span>LinkedIn</span>
                <ExternalLink className="w-2.5 h-2.5 opacity-60" />
              </a>

              <a
                href={profile.instagram_url}
                target="_blank"
                rel="noreferrer"
                className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg bg-gradient-to-r from-pink-500/10 to-rose-500/10 text-pink-400 border border-pink-500/20 text-xs font-semibold hover:bg-pink-500/20 transition-colors"
                title="Official Public Instagram Profile"
              >
                <Instagram className="w-3.5 h-3.5" />
                <span>Instagram</span>
                <ExternalLink className="w-2.5 h-2.5 opacity-60" />
              </a>
            </div>
          </div>
        </div>

        {/* Agent Analysis: Needs */}
        <div className="mb-4 bg-slate-900/60 p-3.5 rounded-2xl border border-slate-800/80">
          <div className="flex items-center gap-1.5 text-xs font-bold text-pink-400 uppercase tracking-wider mb-2">
            <Sparkles className="w-3.5 h-3.5" />
            <span>Agent Extracted Needs</span>
          </div>
          <ul className="space-y-1.5">
            {analysis.needs.slice(0, 2).map((need, idx) => (
              <li key={idx} className="text-xs text-slate-300 flex items-start gap-1.5">
                <span className="text-pink-500 font-bold">•</span>
                <span className="line-clamp-2">{need}</span>
              </li>
            ))}
          </ul>
        </div>

        {/* Hobbies & Qualities Tags */}
        <div className="space-y-2 mb-6">
          <div>
            <span className="text-[11px] font-semibold text-slate-400 block mb-1">Hobbies & Interests</span>
            <div className="flex flex-wrap gap-1.5">
              {analysis.hobbies.slice(0, 3).map((h, i) => (
                <span key={i} className="px-2.5 py-0.5 rounded-md bg-slate-800/80 text-slate-300 text-xs font-medium border border-slate-700/50">
                  {h}
                </span>
              ))}
              {analysis.interests.slice(0, 2).map((interest, i) => (
                <span key={i} className="px-2.5 py-0.5 rounded-md bg-purple-950/40 text-purple-300 text-xs font-medium border border-purple-800/40">
                  {interest}
                </span>
              ))}
            </div>
          </div>

          <div>
            <span className="text-[11px] font-semibold text-slate-400 block mb-1">Core Qualities</span>
            <div className="flex flex-wrap gap-1.5">
              {analysis.qualities.slice(0, 3).map((q, i) => (
                <span key={i} className="px-2 py-0.5 rounded-md bg-rose-950/40 text-rose-300 text-[11px] font-medium border border-rose-800/30">
                  ✨ {q}
                </span>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Card Actions */}
      <div className="pt-4 border-t border-slate-800/80 flex items-center justify-between gap-2">
        <button
          onClick={() => onViewRankings(profile)}
          className="flex-1 flex items-center justify-center gap-1.5 px-3 py-2 rounded-xl bg-slate-800/80 text-slate-200 text-xs font-bold hover:bg-slate-700 transition-colors border border-slate-700/50"
        >
          <Award className="w-3.5 h-3.5 text-amber-400" />
          <span>Rankings</span>
        </button>

        <button
          onClick={() => onStartDate(profile)}
          className="flex-1 flex items-center justify-center gap-1.5 px-3 py-2 rounded-xl bg-gradient-to-r from-pink-600 to-rose-600 text-white text-xs font-bold shadow-md shadow-pink-600/20 hover:shadow-pink-600/40 hover:scale-[1.02] active:scale-[0.98] transition-all"
        >
          <Heart className="w-3.5 h-3.5 fill-white" />
          <span>Date Agent</span>
        </button>
      </div>

    </div>
  );
}
