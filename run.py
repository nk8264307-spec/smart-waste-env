import random
import matplotlib.pyplot as plt
from env.waste_env import WasteEnv


def get_status(bins):
    if max(bins) > 100:
        return "🔴 CRITICAL"
    elif max(bins) > 70:
        return "🟠 WARNING"
    else:
        return "🟢 GOOD"


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
    env = WasteEnv()
    state = env.reset()

    total_reward = 0
    history = []

    print("\n" + "="*60)
    print(f"🚀 RUNNING {agent_type.upper()} AGENT SIMULATION")
    print("="*60)

    for step in range(20):

        if agent_type == "smart":
            actions = smart_agent(state, env)
        else:
            actions = random_agent(env)

        state, reward = env.step(actions)
        total_reward += reward

        history.append(state["bins"].copy())

        print(f"\n🔹 STEP {step}")
        print(f"👉 Actions        : {actions}")
        print(f"🗑️ Bins         : {state['bins']}")
        print(f"🚛 Trucks       : {state['trucks']}")
        print(f"📌 Status       : {get_status(state['bins'])}")
        print(f"⭐ Reward       : {reward}")

    return total_reward, history


# RUN BOTH AGENTS
smart_reward, smart_history = run_simulation("smart")
random_reward, random_history = run_simulation("random")


# 📊 GRAPH PLOTTING
def plot_graph(history, title):
    history = list(zip(*history))  # transpose

    for i, bin_data in enumerate(history):
        plt.plot(bin_data, label=f"Bin {i}")

    plt.title(title)
    plt.xlabel("Steps")
    plt.ylabel("Fill Level")
    plt.legend()
    plt.show()


plot_graph(smart_history, "Smart Agent Performance")
plot_graph(random_history, "Random Agent Performance")


# 📈 FINAL COMPARISON
print("\n" + "="*60)
print("📊 FINAL COMPARISON")
print("="*60)

print(f"🤖 Smart Agent Reward  : {smart_reward}")
print(f"🎲 Random Agent Reward : {random_reward}")

if smart_reward > random_reward:
    print("🏆 Smart Agent Performs Better!")
else:
    print("⚠️ Random Agent Performs Better (unexpected!)")


# 🎯 EFFICIENCY SCORE
efficiency = smart_reward - random_reward

print(f"\n🎯 Efficiency Score: {efficiency}")

if efficiency > 100:
    print("🔥 Excellent Optimization")
elif efficiency > 0:
    print("👍 Good Performance")
else:
    print("⚠️ Needs Improvement")

print("\n✅ Simulation Complete!")
print("="*60)