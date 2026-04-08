from flask import Flask
from env.waste_env import WasteEnv

app = Flask(__name__)

env = WasteEnv()

@app.route("/")
def home():
    return {"message": "Smart Waste Env Running"}

@app.route("/reset", methods=["POST"])
def reset():
    state = env.reset()
    return state

@app.route("/step", methods=["POST"])
def step():
    import random
    actions = [random.randint(0, env.num_bins) for _ in range(env.num_trucks)]
    state, reward = env.step(actions)
    return {"state": state, "reward": reward}

@app.route("/state", methods=["GET"])
def state():
    return env.state