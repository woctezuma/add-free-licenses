from src.cache_utils import (
    load_activated_licenses,
    load_free_licenses,
    save_activated_licenses,
    save_free_licenses,
)
from src.cookie_utils import is_dummy_cookie
from src.fetch_utils import (
    fetch_activated_licenses_via_game_library,
    fetch_activated_licenses_via_userdata,
    fetch_free_licenses,
    load_activated_licenses_via_steamctl,
)


def get_free_ids(force_update=False):
    free_ids = load_free_licenses()
    if len(free_ids) == 0 or force_update:
        free_ids = fetch_free_licenses()
        if len(free_ids) > 0:
            save_free_licenses(free_ids)
    return free_ids


def get_owned_ids(steam_id, cookies=None, force_update=False):
    if cookies is None:
        cookies = {}
    owned_ids = load_activated_licenses()
    if len(owned_ids) == 0:
        owned_ids = load_activated_licenses_via_steamctl()
        if len(owned_ids) > 0:
            save_activated_licenses(owned_ids)
    if (len(owned_ids) == 0 or force_update) and not is_dummy_cookie(cookies):
        owned_ids = fetch_activated_licenses_via_userdata(cookies)
        if len(owned_ids) > 0:
            save_activated_licenses(owned_ids)
    if len(owned_ids) == 0:
        # NB: there is NO `force_update` variable in the if-statement,
        # because this should be run AT BEST ONCE: the first time.
        # Even then, it is NOT RECOMMENDED. You should use `steamctl`!
        # cf. https://github.com/Luois45/claim-free-steam-packages/issues/166
        owned_ids = fetch_activated_licenses_via_game_library(steam_id)
        if len(owned_ids) > 0:
            save_activated_licenses(owned_ids)

    return owned_ids
