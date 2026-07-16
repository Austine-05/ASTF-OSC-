"""
config.py

ATSF-OSC Configuration Loader

Loads project configuration from configs/config.yaml.
"""

from pathlib import Path
import yaml


class Config:

    def __init__(self):

        root = Path(__file__).resolve().parents[2]

        config_file = root / "configs" / "config.yaml"

        with open(config_file, "r", encoding="utf-8") as file:
            self.settings = yaml.safe_load(file)

    def get(self, *keys):

        value = self.settings

        for key in keys:
            value = value[key]

        return value


if __name__ == "__main__":

    config = Config()

    print(config.get("project", "name"))
    print(config.get("training", "test_size"))