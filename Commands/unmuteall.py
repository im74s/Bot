from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

COMMAND_INFO = {"name": "/unmuteall", "desc": "Unmute all members (placeholder).", "usage": "/unmuteall", "scope": "Group admins only", "example": "/unmuteall"}

async def handler(client, message):
    if not await utils.is_group_admin(client, message):
        await message.reply_text("Admins only.")
        return
    await message.reply_text("Unmuteall placeholder.")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["unmuteall"]) & filters.group))
