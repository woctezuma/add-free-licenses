from src.cache_utils import COOKIE_FNAME
from src.json_utils import safe_load_json

REQUIRED_COOKIE_FIELD = "steamLoginSecure"


def load_cookies(fname=COOKIE_FNAME):
    return dict(safe_load_json(fname))


def warn_if_missing_fields(cookies):
    if REQUIRED_COOKIE_FIELD not in cookies:
        warning = f"[WARN] cookies are missing the {REQUIRED_COOKIE_FIELD} field!"
        print(warning)


def is_dummy_cookie(cookies):
    return cookies is None or len(cookies) == 0
