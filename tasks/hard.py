from env.waste_env import WasteEnv

def create_env():
    return WasteEnv(num_bins=6, num_trucks=3)