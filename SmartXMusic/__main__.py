import asyncio
import importlib
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall
import config
from SmartXMusic import LOGGER, app, userbot
from SmartXMusic.core.call import Anony
from SmartXMusic.misc import sudo
from SmartXMusic.plugins import ALL_MODULES
from SmartXMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

async def init():
    if not config.STRING_SESSION:
        LOGGER(__name__).error("User Client Not Started Stopping SmartMusic")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("SmartXMusic.plugins" + all_module)
    LOGGER("SmartXMusic.plugins").info("Successfully Imported All Of The Modules...")
    await userbot.start()
    await Anony.start()
    try:
        await Anony.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("SmartXMusic").warning(
            "Bot Successfully Running On Pyrogram And Py-TgCalls"
        )
    except:
        pass
    await Anony.decorators()
    LOGGER("SmartXMusic").info(
        "SmartXMusic Bot Started Successfully.\n\nDon't forget to visit @TheSmartDev"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("SmartXMusic").info("SmartMusic Bot Stopping...")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
