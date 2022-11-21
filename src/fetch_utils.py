import re

import requests

from src.utils import to_int

GITHUB_URL = "https://raw.githubusercontent.com/Luois45/claim-free-steam-packages"
BRANCH_PATH = "/auto-update/package_list.txt"
INPUT_URL = f"{GITHUB_URL}{BRANCH_PATH}"
INPUT_SEPARATOR = ","
STEAM_URL = "https://steamcommunity.com/id/"
STEAM_ENDPOINT = "/games/?tab=all"
USERDATA_URL = "https://store.steampowered.com/dynamicstore/userdata"
USERDATA_APP_FIELD = "rgOwnedApps"
REQUIRED_COOKIE_FIELD = "steamLoginSecure"


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
    if REQUIRED_COOKIE_FIELD not in cookies:
        warning = f"[WARN] cookies are missing the {REQUIRED_COOKIE_FIELD} field!"
        print(warning)

    response = requests.get(url=USERDATA_URL, cookies=cookies)
    if response.ok:
        data = response.json()
        app_ids = data[USERDATA_APP_FIELD]
    else:
        app_ids = []

    return to_int(app_ids)
