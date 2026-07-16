"""
ATSF-OSC Utility Functions

Common helper functions used across the ATSF-OSC framework.
"""

from pathlib import Path
from datetime import datetime
import json


def ensure_directory(path):
    """
    Create a directory if it does not exist.
    """
    Path(path).mkdir(parents=True, exist_ok=True)


def save_json(data, filename):
    """
    Save a dictionary as a JSON file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def load_json(filename):
    """
    Load a JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def timestamp():
    """
    Return the current date and time.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")