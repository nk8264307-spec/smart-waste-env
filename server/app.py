from flask import Flask, request, jsonify
from env.waste_env import WasteEnv
import random

app = Flask(__name__)

env = WasteEnv()
current_state = env.reset()

# ---------------- ROUTES ----------------

@app.route("/")
def home():
    return {"message": "Smart Waste Env Running"}

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

# ---------------- MAIN FUNCTION ----------------

def main():
    app.run(host="0.0.0.0", port=7860)

# ---------------- ENTRY POINT ----------------

if __name__ == "__main__":
    main()
