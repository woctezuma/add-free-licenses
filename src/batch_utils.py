import asyncio

from src.asf_utils import addlicense
from src.time_utils import save_last_updated_timestamp

NUM_BATCHES = 5
HOURLY_RATE_LIMIT = 50


def batch_process(new_free_ids, num_batches=NUM_BATCHES):
    # Due to the truncation, the total number is AT MOST the limit.
    num_ids_per_batch = int(HOURLY_RATE_LIMIT / NUM_BATCHES)

    newly_activated_ids = []
    loop = asyncio.get_event_loop()

    for batch_no in range(num_batches):
        id_batch = []
        for _ in range(num_ids_per_batch):
            try:
                id_batch.append(new_free_ids.pop())
            except KeyError:
                break

        if len(id_batch) > 0:
            print(
                f"Batch n°{batch_no + 1}/{num_batches}: {id_batch}",
            )

            loop.run_until_complete(addlicense(id_batch))

            save_last_updated_timestamp()

            newly_activated_ids += id_batch

    loop.close()

    return newly_activated_ids
