Plan (phased; concrete and minimal lift)
Phase 0 (start now; 1–2 days)
Canonical choices: default coherence = log model evidence; alternatives (KLD, cosine) moved to Appendix B.
Neutral naming: “cumulative coherence (FREQ)” with alias “FREQ Coin” in Appendix C; “affective coherence index (Emotional Guidance Scale; EGS)” on first use.
Notation preamble and Option‑Availability metric recipe (affordance count + decision entropy).
Replace figure placeholders with final diagram specs; unify transitions and section lead‑ins.
Phase 1 (code + tiny demo; 3–5 days)
Repo scaffold:
code/: env/, agents/, coherence/, logging/, plots/, configs/
env/: small Gym‑like task with episodic distributional shifts.
agents/: flat baseline vs hierarchical Echo/Super/Meta, Resonance Engine, FREQ gating, EGS proxy.
logging/: selection traces, coherence scores, FREQ, ablation configs.
Ablations to run locally (MacBook Pro M3 Pro via PyTorch MPS or CPU):
β/α sweeps (coherence vs utility weight), FREQ on/off, EGS shaping on/off, hierarchical vs flat.
Outputs: plots for hold_time vs policy entropy, adaptation latency, option‑availability proxy vs FREQ, selection‑trace visuals.
Compute notes:
Your Mac is fine for the toy env and small nets (minutes to a couple of hours per sweep).
Optional cloud GPU (only if we scale): 1× mid‑tier GPU instance to speed sweeps; not required for the initial package.
Phase 2 (citations & polish; 2–3 days)
Web fetch DOIs for VSM, predictive processing/active inference, HRL/meta‑RL, affect/interoception, affect‑driven RL, RLHF, and any construct‑level sources.
Insert IEEE‑style inline numbers + References. No hallucinations; all entries link to DOIs/official sources.
Phase 3 (Seismic Initiative Whitepaper; 2–3 days)
Audience: technologists and community.
Content: vision, ecosystem (community/launchpad/fund), operating model, safety/governance, adoption playbook, on‑ramp for “hard‑to‑nail techies,” linkages to ConsciOS and example projects.
Align language with your draft site framing and pillars; reinforce open invitation and movement ethos.
I’ll incorporate the site narrative and positioning from the Seismic draft page you shared: Seismic (draft landing).
Phase 4 (release kit; 1–2 days)
arXiv preprint PDF + workshop‑length version.
Repo README with quickstart, configs, and reproducibility checklist.
Figure assets and a brief FAQ for skeptics (coherence choice, EGS validity, safety).
