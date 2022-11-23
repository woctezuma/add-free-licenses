from src.json_utils import safe_load_json, safe_save_json

DATA_FOLDER = "data/"
FREE_LICENSE_FNAME = f"{DATA_FOLDER}free_licenses.json"
ACTIVATED_LICENSE_FNAME = f"{DATA_FOLDER}activated_licenses.json"
TIMESTAMP_FNAME = f"{DATA_FOLDER}last_updated.json"
COOKIE_FNAME = f"{DATA_FOLDER}cookies.json"
STEAMCTL_OUTPUT_FNAME = f"{DATA_FOLDER}steamctl_output.txt"


def load_activated_licenses(fname=ACTIVATED_LICENSE_FNAME):
    return sorted(safe_load_json(fname), key=int)


def save_activated_licenses(license_ids, fname=ACTIVATED_LICENSE_FNAME):
    return safe_save_json(sorted(license_ids, key=int), fname)


def load_free_licenses(fname=FREE_LICENSE_FNAME):
    return sorted(safe_load_json(fname), key=int)


def save_free_licenses(license_ids, fname=FREE_LICENSE_FNAME):
    return safe_save_json(sorted(license_ids, key=int), fname)
