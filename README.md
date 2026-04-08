# Smart City Waste Management System (Multi-Agent RL Environment)

## Overview
This project simulates a smart city waste management system using a multi-agent reinforcement learning environment. Multiple garbage trucks coordinate intelligently to collect waste, prevent bin overflow, and optimize collection efficiency.


## Key Highlights
- Multi-agent system (multiple garbage trucks)
- Intelligent decision-making (smart agent vs random agent)
- Real-time simulation with performance graphs
- Reward-based optimization system
- Scalable difficulty levels (easy, medium, hard)


## Objective
To design an environment where agents learn to:
- Prioritize high-fill garbage bins
- Minimize overflow situations
- Optimize movement and collection efficiency


## Environment Design

### State
- Bin fill levels
- Truck positions

### Actions
- Move to any bin
- Empty current bin

### Reward System
- +20 → Empty full bin  
- +2 → Efficient movement  
- -10 → Wrong empty action  
- -50 → Bin overflow  
- -1 → Time penalty  


## Agents Implemented

### 🔹 Smart Agent
- Moves to the fullest bin
- Empties bins when necessary
- Optimizes reward over time

### 🔹 Random Agent
- Takes random actions
- Used as baseline for comparison


## Performance Analysis
- Comparison between smart and random agents
- Efficiency score calculation
- Graph visualization of bin levels over time


## Project Structure
- env/ → Environment logic
- tasks/ → Difficulty levels
- run.py → Simulation runner
- openenv.yaml→ Environment config
- Dockerfile → Container setup
- requirements.txt → Dependencies
- README.md → Documentation


## How to Run
- pip install -r requirements.txt
- python run.py

## Docker Support
- docker build -t waste-env .
- docker run waste-env

## Tagline
Building intelligent systems where AI-driven agents learn to act smart, not random.
