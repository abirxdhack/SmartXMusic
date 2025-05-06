from pyrogram import filters
from SmartXMusic import app
from SmartXMusic.misc import SUDOERS
from SmartXMusic.utils.database import add_off, add_on
from SmartXMusic.utils.decorators.language import language
from config import COMMAND_PREFIXES

# Create a filter for commands with multiple prefixes
multi_prefix_filter = lambda commands: filters.command(commands, prefixes=COMMAND_PREFIXES)

@app.on_message(multi_prefix_filter(["logger"]) & SUDOERS)
@language
async def logger(client, message, _):
    usage = _["log_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        await add_on(2)
        await message.reply_text(_["log_2"])
    elif state == "disable":
        await add_off(2)
        await message.reply_text(_["log_3"])
    else:
        await message.reply_text(usage)
