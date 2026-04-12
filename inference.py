import os
import random
from env.waste_env import WasteEnv
from openai import OpenAI

try:
    client = OpenAI(
        base_url=os.environ.get("API_BASE_URL"),
        api_key=os.environ.get("API_KEY")
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Optimize waste collection"}],
        timeout=5
    )

except Exception as e:
    print("LLM call failed, continuing...", flush=True)

# ---------------- ENV ----------------
random.seed(42)

env = WasteEnv()
state = env.reset()

task_name = "smart_waste"

print(f"[START] task={task_name}", flush=True)

total_reward = 0

for step in range(20):
    actions = [random.randint(0, env.num_bins) for _ in range(env.num_trucks)]

    state, reward = env.step(actions)
    total_reward += reward

    print(f"[STEP] step={step} reward={reward}", flush=True)

print(f"[END] task={task_name} score={total_reward} steps=20", flush=True)
