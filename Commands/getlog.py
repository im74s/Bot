from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

COMMAND_INFO = {"name": "/getlog", "desc": "Get current log channel (placeholder).", "usage": "/getlog", "scope": "Group admins only", "example": "/getlog"}

async def handler(client, message):
    if not await utils.is_group_admin(client, message):
        await message.reply_text("Admins only.")
        return
    await message.reply_text("Current log channel: not set (placeholder).")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["getlog"]) & filters.group))
