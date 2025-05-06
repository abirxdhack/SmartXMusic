from pyrogram import filters
from pyrogram.types import Message
from SmartXMusic import app
from SmartXMusic.utils import extract_user, int_to_alpha
from SmartXMusic.utils.database import (
    delete_authuser,
    get_authuser,
    get_authuser_names,
    save_authuser,
)
from SmartXMusic.utils.decorators import AdminActual, language
from SmartXMusic.utils.inline import close_markup
from config import BANNED_USERS, adminlist, COMMAND_PREFIXES

# Define command filters with multiple prefixes
command_filters = filters.command(["auth", "unauth", "authlist", "authusers"], prefixes=COMMAND_PREFIXES)

@app.on_message(command_filters & filters.group & ~BANNED_USERS)
@language
async def handle_commands(client, message: Message, _):
    command = message.command[0].lower()

    if command == "auth":
        return await auth(client, message, _)
    elif command == "unauth":
        return await unauthusers(client, message, _)
    elif command in ["authlist", "authusers"]:
        return await authusers(client, message, _)

async def auth(client, message: Message, _):
    if not message.reply_to_message and len(message.command) != 2:
        return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    token = await int_to_alpha(user.id)
    _check = await get_authuser_names(message.chat.id)
    count = len(_check)
    if int(count) == 25:
        return await message.reply_text(_["auth_1"])
    if token not in _check:
        assis = {
            "auth_user_id": user.id,
            "auth_name": user.first_name,
            "admin_id": message.from_user.id,
            "admin_name": message.from_user.first_name,
        }
        get = adminlist.get(message.chat.id)
        if get:
            if user.id not in get:
                get.append(user.id)
        await save_authuser(message.chat.id, token, assis)
        return await message.reply_text(_["auth_2"].format(user.mention))
    else:
        return await message.reply_text(_["auth_3"].format(user.mention))

async def unauthusers(client, message: Message, _):
    if not message.reply_to_message and len(message.command) != 2:
        return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    token = await int_to_alpha(user.id)
    deleted = await delete_authuser(message.chat.id, token)
    get = adminlist.get(message.chat.id)
    if get:
        if user.id in get:
            get.remove(user.id)
    if deleted:
        return await message.reply_text(_["auth_4"].format(user.mention))
    else:
        return await message.reply_text(_["auth_5"].format(user.mention))

async def authusers(client, message: Message, _):
    _wtf = await get_authuser_names(message.chat.id)
    if not _wtf:
        return await message.reply_text(_["setting_4"])
    else:
        j = 0
        mystic = await message.reply_text(_["auth_6"])
        text = _["auth_7"].format(message.chat.title)
        for umm in _wtf:
            _umm = await get_authuser(message.chat.id, umm)
            user_id = _umm["auth_user_id"]
            admin_id = _umm["admin_id"]
            admin_name = _umm["admin_name"]
            try:
                user = (await app.get_users(user_id)).first_name
                j += 1
            except:
                continue
            text += f"{j}➤ {user}[<code>{user_id}</code>]\n"
            text += f"   {_['auth_8']} {admin_name}[<code>{admin_id}</code>]\n\n"
        await mystic.edit_text(text, reply_markup=close_markup(_))
