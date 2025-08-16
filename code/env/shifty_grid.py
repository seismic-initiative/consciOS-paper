import numpy as np


class ShiftyGrid:
	"""
	Tiny grid-like toy env with episodic distributional shifts.
	State: scalar context + position index.
	Actions: {-1, +1}; reward depends on hidden context.
	"""

	def __init__(self, length=21, shift_every=50, seed=0):
		self.length = length
		self.shift_every = shift_every
		self.rng = np.random.default_rng(seed)
		self.t = 0
		self.ctx = 1  # context flips sign
		self.pos = length // 2

	def reset(self):
		self.t = 0
		self.pos = self.length // 2
		self.ctx = 1
		return self._obs()

	def step(self, a):
		if self.t > 0 and self.t % self.shift_every == 0:
			self.ctx *= -1
		self.pos = int(np.clip(self.pos + (1 if a > 0 else -1), 0, self.length - 1))
		target = self.length - 1 if self.ctx > 0 else 0
		r = 1.0 if self.pos == target else -0.01 * abs(self.pos - target)
		self.t += 1
		done = self.t % self.shift_every == 0
		return self._obs(), r, done, {"ctx": self.ctx}

	def _obs(self):
		return np.array([self.pos / (self.length - 1), (self.ctx + 1) / 2.0], dtype=np.float32)


if __name__ == "__main__":
	env = ShiftyGrid()
	s = env.reset()
	for _ in range(5):
		s, r, d, info = env.step(1)
		print(s, r, d, info)


