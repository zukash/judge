import pickle
from pathlib import Path

# default settings
CONFIG_DIR = Path().home() / ".config" / "judge"
CONFIG_FILE = Path(CONFIG_DIR) / "config"
COOKIES_FILE = Path(CONFIG_DIR) / "cookies"
PROBLEM_DIR = Path().home() / ".judge"
SOLVER_EXTENSIONS = ["py", "out"]

# overwrite some settings
try:
    with open(CONFIG_FILE, "rb") as f:
        configs = pickle.load(f)
except Exception:
    configs = {}

for name, value in configs.items():
    exec(f"{name} = {value}")
