from flask import Flask, send_file, request, jsonify
import random
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from env.waste_env import WasteEnv

app = Flask(__name__)

random.seed(42)

env = WasteEnv()
current_state = env.reset()

def get_status(bins):
    if max(bins) > 100:
        return "CRITICAL"
    elif max(bins) > 70:
        return "WARNING"
    else:
        return "GOOD"

def smart_agent(state, env):
    actions = []
    for i in range(env.num_trucks):
        truck_pos = state["trucks"][i]

        if state["bins"][truck_pos] >= 50:
            actions.append(env.num_bins)  # empty
        else:
            max_bin = state["bins"].index(max(state["bins"]))
            actions.append(max_bin)

    return actions

def random_agent(env):
    return [random.randint(0, env.num_bins) for _ in range(env.num_trucks)]

def run_simulation(agent_type="smart"):
    env_local = WasteEnv()
    state = env_local.reset()

    total_reward = 0
    history = []
    output = ""

    for step in range(20):
        if agent_type == "smart":
            actions = smart_agent(state, env_local)
        else:
            actions = random_agent(env_local)

        state, reward = env_local.step(actions)
        total_reward += reward

        history.append(state["bins"].copy())

        output += f"Step {step}\n"
        output += f"Bins: {state['bins']} | Reward: {reward}\n"

    return total_reward, history, output

def plot_graph(history, filename, title):
    history = list(zip(*history))

    plt.figure(figsize=(8, 5))

    for i, bin_data in enumerate(history):
        plt.plot(bin_data, label=f"Bin {i}")

    plt.title(title)
    plt.xlabel("Steps")
    plt.ylabel("Fill Level")
    plt.legend()
    plt.tight_layout()

    plt.savefig(filename)
    plt.close()

print("Generating graphs...")

smart_reward, smart_history, smart_output = run_simulation("smart")
random_reward, random_history, random_output = run_simulation("random")

plot_graph(smart_history, "smart.png", "Smart Agent Performance")
plot_graph(random_history, "random.png", "Random Agent Performance")

final = f"""
FINAL RESULTS
Smart Reward  : {smart_reward}
Random Reward : {random_reward}
Efficiency    : {smart_reward - random_reward}
"""

@app.route("/")
def home():
    return f"""
    <h1>🚀 Smart Waste Management</h1>

    <h2>🧠 Smart Agent</h2>
    <pre>{smart_output}</pre>

    <h2>🎲 Random Agent</h2>
    <pre>{random_output}</pre>

    <h2>📊 Results</h2>
    <pre>{final}</pre>

    <h2>📈 Smart Graph</h2>
    <img src="/smart_graph" width="600">

    <h2>📉 Random Graph</h2>
    <img src="/random_graph" width="600">
    """

@app.route("/smart_graph")
def smart_graph():
    return send_file("smart.png", mimetype='image/png')

@app.route("/random_graph")
def random_graph():
    return send_file("random.png", mimetype='image/png')

@app.route("/reset", methods=["POST"])
def reset():
    global current_state
    current_state = env.reset()
    return jsonify(current_state)

@app.route("/step", methods=["POST"])
def step():
    global current_state
    data = request.get_json()

    actions = data.get("actions", [])

    current_state, reward = env.step(actions)

    return jsonify({
        "state": current_state,
        "reward": reward
    })

@app.route("/state", methods=["GET"])
def state():
    return jsonify(current_state)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
