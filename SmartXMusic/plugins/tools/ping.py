from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message
from SmartXMusic import app
from SmartXMusic.core.call import Anony
from SmartXMusic.utils import bot_sys_stats
from SmartXMusic.utils.decorators.language import language
from SmartXMusic.utils.inline import supp_markup
from config import BANNED_USERS, PING_IMG_URL, COMMAND_PREFIXES

# Create a filter for commands with multiple prefixes
multi_prefix_filter = lambda commands: filters.command(commands, prefixes=COMMAND_PREFIXES)

@app.on_message(multi_prefix_filter(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"].format(app.mention),
    )
    pytgping = await Anony.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )
