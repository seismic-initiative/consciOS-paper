# ConsciOS Demo: Hierarchical Controller Benchmark

Minimal ablations for the ConsciOS architecture:
- Flat agent vs Hierarchical (Echo/Super/Meta)
- Resonance Engine selection (β/α sweeps)
- Cumulative coherence gating (FREQ on/off)
- EGS‑like intrinsic shaping on/off

## Setup
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

## Run
# Flat baseline
python -m agents.flat_agent --episodes 200 --seed 1
# Hierarchical
python -m agents.hier_agent --episodes 200 --seed 1 --beta 1.0 --alpha 0.5 --freq_on true --egs_on true

## Outputs
- logs/: selection traces, coherence scores, FREQ timeline
- plots/: hold_time vs policy_entropy, adaptation_latency, OA vs FREQ

## Notes
Default coherence: log‑evidence proxy; KLD/cosine alternatives available in coherence/.


