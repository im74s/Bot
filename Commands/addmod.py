from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

COMMAND_INFO = {"name": "/addmod", "desc": "Add a moderator (placeholder).", "usage": "/addmod <reply>", "scope": "Group admins only", "example": "/addmod (reply)"}

async def handler(client, message):
    if not await utils.is_group_admin(client, message):
        await message.reply_text("Admins only.")
        return
    await message.reply_text("Added moderator (placeholder).")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["addmod"]) & filters.group))
