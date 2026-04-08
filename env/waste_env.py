import random

class WasteEnv:

    def __init__(self, num_bins=3, num_trucks=2):
        self.num_bins = num_bins
        self.num_trucks = num_trucks
        self.reset()

    def reset(self):
        self.bins = [random.randint(20, 60) for _ in range(self.num_bins)]
        self.trucks = [0 for _ in range(self.num_trucks)]
        self.steps = 0
        return self.state()

    def state(self):
        return {
            "bins": self.bins,
            "trucks": self.trucks
        }

    def step(self, actions):
        reward = 0
        self.steps += 1

        for i, action in enumerate(actions):

            # Move truck to bin
            if action < self.num_bins:
                self.trucks[i] = action
                reward += 2

            # Empty bin
            elif action == self.num_bins:
                pos = self.trucks[i]

                if self.bins[pos] >= 50:
                    self.bins[pos] = 0
                    reward += 20
                else:
                    reward -= 10

        # Bins fill over time
        for i in range(self.num_bins):
            self.bins[i] += random.randint(5, 15)

            if self.bins[i] > 100:
                reward -= 50

        # Time penalty (efficiency)
        reward -= 1

        return self.state(), reward