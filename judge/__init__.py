import importlib.metadata
from pathlib import Path

from . import settings

__version__ = importlib.metadata.version(__name__)

Path(settings.CONFIG_DIR).mkdir(exist_ok=True)
