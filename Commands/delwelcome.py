from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

COMMAND_INFO = {"name": "/delwelcome", "desc": "Delete welcome message (not persisted).", "usage": "/delwelcome", "scope": "Group admins only", "example": "/delwelcome"}

async def handler(client, message):
    if not await utils.is_group_admin(client, message):
        await message.reply_text("Admins only.")
        return
    await message.reply_text("Welcome message deleted (placeholder).")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["delwelcome"]) & filters.group))
