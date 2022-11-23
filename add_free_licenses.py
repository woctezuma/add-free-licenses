from src.batch_utils import batch_process
from src.cache_utils import save_activated_licenses
from src.cookie_utils import load_cookies
from src.get_utils import get_free_ids, get_owned_ids
from src.time_utils import get_wait_time, is_rate_limited

STEAM_ID = "wokuma"


def main():
    free_ids = get_free_ids(force_update=False)

    owned_ids = get_owned_ids(
        steam_id=STEAM_ID,
        cookies=load_cookies(),
        force_update=False,
    )

    new_free_ids = set(free_ids).difference(owned_ids)
    print(f"There are {len(new_free_ids)} license IDs to add to your account.")

    if is_rate_limited():
        print(f"You are rate-limited. Wait for {get_wait_time()} seconds.")
    else:
        newly_activated_ids = batch_process(new_free_ids)
        print(f"Activated ids: {newly_activated_ids}")
        if len(newly_activated_ids) > 0:
            save_activated_licenses(owned_ids + newly_activated_ids)


if __name__ == "__main__":
    main()
