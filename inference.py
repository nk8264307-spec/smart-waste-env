from env.waste_env import WasteEnv
import random
import sys

random.seed(42)

env = WasteEnv()
state = env.reset()

task_name = "smart_waste"

# START BLOCK
print(f"[START] task={task_name}", flush=True)

total_reward = 0

for step in range(20):
    actions = [random.randint(0, env.num_bins) for _ in range(env.num_trucks)]

    state, reward = env.step(actions)
    total_reward += reward

    # STEP BLOCK
    print(f"[STEP] step={step} reward={reward}", flush=True)

# END BLOCK
print(f"[END] task={task_name} score={total_reward} steps=20", flush=True)
