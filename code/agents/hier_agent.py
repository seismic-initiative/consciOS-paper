import argparse
from ..env.shifty_grid import ShiftyGrid
from ..selection.resonance import resonance_score


def run(episodes: int, seed: int, beta: float, alpha: float, freq_on: bool, egs_on: bool):
	env = ShiftyGrid(seed=seed)
	s = env.reset()
	# toy: two candidate frames (left vs right) with dummy utilities; select via resonance_score
	for ep in range(episodes):
		# placeholder coherence/util estimates
		eu_left, eu_right = 0.1, 0.1
		c_left, c_right = 0.4, 0.6
		cost_left, cost_right = 0.05, 0.05
		score_left = resonance_score(eu_left, c_left, cost_left, alpha, beta, 0.0)
		score_right = resonance_score(eu_right, c_right, cost_right, alpha, beta, 0.0)
		a = 1 if score_right >= score_left else -1
		s, r, done, info = env.step(a)
		if done:
			env.reset()


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--episodes", type=int, default=200)
	parser.add_argument("--seed", type=int, default=1)
	parser.add_argument("--beta", type=float, default=1.0)
	parser.add_argument("--alpha", type=float, default=0.5)
	parser.add_argument("--freq_on", type=str, default="true")
	parser.add_argument("--egs_on", type=str, default="true")
	args = parser.parse_args()
	run(args.episodes, args.seed, args.beta, args.alpha, args.freq_on.lower()=="true", args.egs_on.lower()=="true")


