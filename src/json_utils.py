import json
from pathlib import Path


def load_json(fname):
    with open(fname, encoding="utf8") as file:
        return json.load(file)


def safe_load_json(fname):
    try:
        license_ids = load_json(fname)
    except FileNotFoundError:
        license_ids = []
    return license_ids


def save_json(data, fname, indent=4, sort_keys=True):
    with open(fname, "w", encoding="utf8") as file:
        json.dump(data, file, indent=indent, sort_keys=sort_keys)


def safe_save_json(data, fname, indent=4, sort_keys=True):
    Path(fname).parent.mkdir(parents=False, exist_ok=True)
    save_json(data, fname, indent, sort_keys)
