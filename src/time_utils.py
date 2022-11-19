import datetime

from src.cache_utils import TIMESTAMP_FNAME
from src.json_utils import safe_load_json, safe_save_json

RATE_LIMIT_COOLDOWN_IN_SECONDS = 3600


def get_timestamp():
    return datetime.datetime.now().timestamp()


def is_rate_limited(last_updated_timestamp=None):
    if last_updated_timestamp is None:
        last_updated_timestamp = load_last_updated_timestamp()
    return bool(get_wait_time(last_updated_timestamp) > 0)


def get_wait_time(last_updated_timestamp=None):
    if last_updated_timestamp is None:
        last_updated_timestamp = load_last_updated_timestamp()
    return int(
        last_updated_timestamp + RATE_LIMIT_COOLDOWN_IN_SECONDS - get_timestamp(),
    )


def load_last_updated_timestamp(fname=TIMESTAMP_FNAME):
    timestamp_list = safe_load_json(fname)

    if len(timestamp_list) > 0:
        timestamp = float(timestamp_list[0])
    else:
        timestamp = 0

    return timestamp


def save_last_updated_timestamp(timestamp=None, fname=TIMESTAMP_FNAME):
    if timestamp is None:
        timestamp = get_timestamp()

    timestamp_list = [str(timestamp)]

    return safe_save_json(timestamp_list, fname)
