from ASF import IPC

from src.utils import to_str

ASF_COMMAND = "!addlicense"
ASF_SEPARATOR = ","
BOT_NAME = "ASF"
ID_PREFIX = "a/"


async def send_command(asf, cmd):
    return await asf.Api.Command.post(body={"Command": cmd})


async def send_addlicense_command(asf, ids, bot_name, id_prefix):
    return await send_command(
        asf,
        generate_addlicense_command(ids, bot_name, id_prefix),
    )


def generate_addlicense_command(ids, bot_name, id_prefix):
    return f"{ASF_COMMAND} {bot_name} {id_prefix}" + f"{ASF_SEPARATOR}{id_prefix}".join(
        to_str(ids),
    )


async def addlicense(ids, bot_name=BOT_NAME, id_prefix=ID_PREFIX):
    async with IPC() as asf:
        await send_addlicense_command(asf, ids, bot_name, id_prefix)
