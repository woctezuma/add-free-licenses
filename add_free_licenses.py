from src.batch_utils import batch_process
from src.get_utils import get_free_ids, get_owned_ids
from src.time_utils import get_wait_time, is_rate_limited

STEAM_ID = "wokuma"


def main():
    free_ids = get_free_ids(force_update=False)

    # TODO initialize the JSON file with steamctl
    owned_ids = get_owned_ids(steam_id=STEAM_ID)

    new_free_ids = set(free_ids).difference(owned_ids)
    print(f"There are {len(new_free_ids)} license IDs to add to your account.")

    if is_rate_limited():
        print(f"You are rate-limited. Wait for {get_wait_time()} seconds.")
    else:
        # TODO check if ASF is running
        # TODO parse ASF output to check if the activation was OK.
        newly_activated_ids = batch_process(new_free_ids)
        print(f"Activated ids: {newly_activated_ids}")


if __name__ == "__main__":
    main()
