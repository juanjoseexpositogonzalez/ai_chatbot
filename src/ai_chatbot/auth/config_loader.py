from pathlib import Path
from typing import Dict

import yaml
from yaml.loader import SafeLoader


def load_config(config_path: str | Path) -> Dict[str, str]:
    """Loads the YAML config file for authentication."""
    with open(config_path, "r", encoding="utf-8") as file:
        return yaml.load(file, Loader=SafeLoader)
