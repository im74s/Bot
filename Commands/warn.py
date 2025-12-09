from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

# In-memory warns
_WARNS = {}

COMMAND_INFO = {"name": "/warn", "desc": "Warn a user (in-memory).", "usage": "/warn <reply or @username> [reason]", "scope": "Group admins only", "example": "/warn (reply) Spamming"}

async def handler(client, message):
    if not await utils.is_group_admin(client, message):
        await message.reply_text("Admins only.")
        return
    target = message.reply_to_message.from_user if message.reply_to_message else None
    if not target:
        await message.reply_text("Reply to the user you want to warn.")
        return
    _WARNS.setdefault(message.chat.id, {})
    _WARNS[message.chat.id].setdefault(target.id, 0)
    _WARNS[message.chat.id][target.id] += 1
    await message.reply_text(f"User warned. Total warns: {_WARNS[message.chat.id][target.id]}")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["warn"]) & filters.group))
