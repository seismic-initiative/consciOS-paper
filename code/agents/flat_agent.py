import argparse
from ..env.shifty_grid import ShiftyGrid


def run(episodes: int, seed: int):
	env = ShiftyGrid(seed=seed)
	s = env.reset()
	for ep in range(episodes):
		# naive policy: always move toward right
		a = 1
		s, r, done, info = env.step(a)
		if done:
			env.reset()


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--episodes", type=int, default=200)
	parser.add_argument("--seed", type=int, default=1)
	args = parser.parse_args()
	run(args.episodes, args.seed)


if __name__ == "__main__":
	main()


