from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

COMMAND_INFO = {"name": "/setwelcome", "desc": "Set welcome message (not persisted).", "usage": "/setwelcome <text>", "scope": "Group admins only", "example": "/setwelcome Welcome!"}

async def handler(client, message):
    if not await utils.is_group_admin(client, message):
        await message.reply_text("Admins only.")
        return
    await message.reply_text("Welcome message set (in-memory placeholder).")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["setwelcome"]) & filters.group))
