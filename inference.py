from env.waste_env import WasteEnv
import random

random.seed(42)

env = WasteEnv()
state = env.reset()

print("Initial State:", state)

total_reward = 0

for step in range(20):
    actions = [random.randint(0, env.num_bins) for _ in range(env.num_trucks)]

    state, reward = env.step(actions)
    total_reward += reward

    print(f"Step {step}")
    print("Actions:", actions)
    print("State:", state)
    print("Reward:", reward)
    print("-" * 30)

print("Total Reward:", total_reward)