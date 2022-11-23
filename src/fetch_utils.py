import re

import requests

from src.cache_utils import STEAMCTL_OUTPUT_FNAME
from src.cookie_utils import warn_if_missing_fields
from src.utils import to_int

GITHUB_URL = "https://raw.githubusercontent.com/Luois45/claim-free-steam-packages"
BRANCH_PATH = "/auto-update/package_list.txt"
INPUT_URL = f"{GITHUB_URL}{BRANCH_PATH}"
INPUT_SEPARATOR = ","
STEAM_URL = "https://steamcommunity.com/id/"
STEAM_ENDPOINT = "/games/?tab=all"
USERDATA_URL = "https://store.steampowered.com/dynamicstore/userdata"
USERDATA_APP_FIELD = "rgOwnedApps"


def fetch_free_licenses(url=INPUT_URL, separator=INPUT_SEPARATOR):
    response = requests.get(url)
    if response.ok:
        app_ids = response.text.split(separator)
    else:
        app_ids = []

    return to_int(app_ids)


def fetch_activated_licenses_via_game_library(steam_id):
    response = requests.get(url=f"{STEAM_URL}{steam_id}{STEAM_ENDPOINT}")
    if response.ok:
        html = response.text
        regex = re.compile(r'"appid":(\d+),')
        app_ids = regex.findall(html)

    else:
        app_ids = []

    warning = "[WARN] fetched licenses are not exhaustive, e.g. demos are missing!"
    print(warning)

    return to_int(app_ids)


def fetch_activated_licenses_via_userdata(cookies):
    warn_if_missing_fields(cookies)

    response = requests.get(url=USERDATA_URL, cookies=cookies)
    if response.ok:
        data = response.json()
        app_ids = data[USERDATA_APP_FIELD]
    else:
        app_ids = []

    return to_int(app_ids)


def load_activated_licenses_via_steamctl(fname=STEAMCTL_OUTPUT_FNAME):
    try:
        with open(fname, encoding="utf8") as file:
            app_ids = [line.split()[0] for line in file.readlines()]
    except FileNotFoundError:
        app_ids = []

    return to_int(app_ids)
