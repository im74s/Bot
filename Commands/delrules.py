from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

COMMAND_INFO = {"name": "/delrules", "desc": "Delete rules (placeholder).", "usage": "/delrules", "scope": "Group admins only", "example": "/delrules"}

async def handler(client, message):
    if not await utils.is_group_admin(client, message):
        await message.reply_text("Admins only.")
        return
    await message.reply_text("Rules deleted (placeholder).")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["delrules"]) & filters.group))
