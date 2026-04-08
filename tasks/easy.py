from env.waste_env import WasteEnv

def create_env():
    return WasteEnv(num_bins=2, num_trucks=1)