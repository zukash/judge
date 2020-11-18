import pickle

from . import settings


def config(name, value):
    try:
        with open(settings.CONFIG_FILE, "rb") as f:
            configs = pickle.load(f)
    except Exception:
        configs = {}

    configs[name.upper()] = value

    with open(settings.CONFIG_FILE, "wb") as f:
        pickle.dump(configs, f)
