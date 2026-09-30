import React, { useState } from 'react';
import { Linkedin, Instagram, Sparkles, ArrowRight, CheckCircle, RefreshCw, UserCheck } from 'lucide-react';

export default function LinkIngestion({ onIngestSuccess }) {
  const [linkedinUrl, setLinkedinUrl] = useState('');
  const [instagramUrl, setInstagramUrl] = useState('');
  const [loading, setLoading] = useState(false);
  const [step, setStep] = useState(0);
  const [error, setError] = useState('');
  const [ingestedProfile, setIngestedProfile] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!linkedinUrl || !instagramUrl) {
      setError('Please provide both official public LinkedIn and Instagram links.');
      return;
    }
    setError('');
    setLoading(true);
    setStep(1);

    try {
      // Step 1: Scrape LinkedIn
      await new Promise((r) => setTimeout(r, 800));
      setStep(2);

      // Step 2: Scrape Instagram
      await new Promise((r) => setTimeout(r, 800));
      setStep(3);

      // Step 3: Call API
      const res = await fetch('/api/ingest', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ linkedin_url: linkedinUrl, instagram_url: instagramUrl }),
      });

      if (!res.ok) {
        throw new Error('Failed to ingest profile links. Ensure backend server is running.');
      }

      const data = await res.json();
      setIngestedProfile(data.profile);
      setStep(4);

      if (onIngestSuccess) {
        onIngestSuccess(data.profile, data.rankings);
      }
    } catch (err) {
      setError(err.message || 'Scraping error');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto space-y-8">
      
      {/* Header Banner */}
      <div className="glass-panel p-8 rounded-3xl text-center border border-pink-500/20 relative overflow-hidden">
        <div className="w-16 h-16 rounded-2xl bg-gradient-to-tr from-pink-500 to-rose-600 flex items-center justify-center mx-auto mb-4 shadow-lg shadow-pink-500/30">
          <Sparkles className="w-8 h-8 text-white" />
        </div>
        <h2 className="text-3xl font-black text-white">Deploy Your Agent to Date</h2>
        <p className="text-sm text-slate-300 max-w-xl mx-auto mt-2">
          Paste official public LinkedIn and Instagram links for any person. Our engine reads both sources, synthesizes their agent persona, and sends them into the dating pool with the 25 people!
        </p>
      </div>

      {/* Form Card */}
      <div className="glass-card p-8 rounded-3xl border border-slate-800">
        <form onSubmit={handleSubmit} className="space-y-6">
          
          {error && (
            <div className="p-4 rounded-2xl bg-rose-500/10 border border-rose-500/20 text-rose-400 text-xs font-semibold">
              {error}
            </div>
          )}

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            
            {/* LinkedIn Input */}
            <div>
              <label className="block text-xs font-bold text-slate-300 uppercase tracking-wider mb-2 flex items-center gap-1.5">
                <Linkedin className="w-4 h-4 text-blue-400" />
                <span>Official LinkedIn URL</span>
              </label>
              <input
                type="url"
                required
                placeholder="https://www.linkedin.com/in/username"
                value={linkedinUrl}
                onChange={(e) => setLinkedinUrl(e.target.value)}
                className="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-sm text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
              <span className="text-[11px] text-slate-500 mt-1 block">Reads career history, skills, and values</span>
            </div>

            {/* Instagram Input */}
            <div>
              <label className="block text-xs font-bold text-slate-300 uppercase tracking-wider mb-2 flex items-center gap-1.5">
                <Instagram className="w-4 h-4 text-pink-400" />
                <span>Official Public Instagram URL</span>
              </label>
              <input
                type="url"
                required
                placeholder="https://www.instagram.com/username"
                value={instagramUrl}
                onChange={(e) => setInstagramUrl(e.target.value)}
                className="w-full bg-slate-900 border border-slate-700 rounded-xl px-4 py-3 text-sm text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-pink-500"
              />
              <span className="text-[11px] text-slate-500 mt-1 block">Reads hobbies, visual aesthetic, and vibe</span>
            </div>

          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full py-4 rounded-2xl bg-gradient-to-r from-pink-600 via-rose-600 to-purple-600 text-white font-extrabold text-base shadow-xl shadow-pink-600/25 hover:scale-[1.01] active:scale-[0.99] transition-all disabled:opacity-60 flex items-center justify-center gap-2"
          >
            {loading ? (
              <>
                <RefreshCw className="w-5 h-5 animate-spin" />
                <span>Analyzing & Building Agent Persona...</span>
              </>
            ) : (
              <>
                <span>Extract Links & Deploy Dating Agent</span>
                <ArrowRight className="w-5 h-5" />
              </>
            )}
          </button>

        </form>

        {/* Progress Tracker */}
        {loading && (
          <div className="mt-8 pt-6 border-t border-slate-800 space-y-3">
            <h4 className="text-xs font-bold text-pink-400 uppercase tracking-wider">Scraping & Analysis Pipeline</h4>
            <div className="space-y-2 text-xs">
              <div className={`flex items-center gap-2 ${step >= 1 ? 'text-emerald-400 font-semibold' : 'text-slate-500'}`}>
                <CheckCircle className="w-4 h-4" /> 1. Fetching LinkedIn public profile metadata & work history...
              </div>
              <div className={`flex items-center gap-2 ${step >= 2 ? 'text-emerald-400 font-semibold' : 'text-slate-500'}`}>
                <CheckCircle className="w-4 h-4" /> 2. Fetching Instagram public profile metadata, hobbies & vibe...
              </div>
              <div className={`flex items-center gap-2 ${step >= 3 ? 'text-emerald-400 font-semibold' : 'text-slate-500'}`}>
                <CheckCircle className="w-4 h-4" /> 3. Synthesizing Needs, Hobbies, Interests, and Qualities...
              </div>
              <div className={`flex items-center gap-2 ${step >= 4 ? 'text-emerald-400 font-semibold' : 'text-slate-500'}`}>
                <CheckCircle className="w-4 h-4" /> 4. Deploying Agent into Dating Pool with 25 people!
              </div>
            </div>
          </div>
        )}

      </div>

      {/* Ingest Result Banner */}
      {ingestedProfile && (
        <div className="glass-panel p-6 rounded-3xl border border-emerald-500/40 bg-emerald-950/20 text-center space-y-4">
          <div className="w-12 h-12 bg-emerald-500/20 rounded-full flex items-center justify-center mx-auto text-emerald-400">
            <UserCheck className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-xl font-extrabold text-white">Agent Created for {ingestedProfile.name}!</h3>
            <p className="text-xs text-slate-300 mt-1">
              Extracted {ingestedProfile.analysis.hobbies.length} hobbies and {ingestedProfile.analysis.needs.length} core needs. Check the 25 Profiles tab or Date Arena to start dating!
            </p>
          </div>
        </div>
      )}

    </div>
  );
}
