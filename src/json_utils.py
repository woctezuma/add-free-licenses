import json


def load_json(fname):
    with open(fname, encoding="utf8") as file:
        return json.load(file)


def save_json(data, fname, indent=4, sort_keys=True):
    with open(fname, "w", encoding="utf8") as file:
        json.dump(data, file, indent=indent, sort_keys=sort_keys)
