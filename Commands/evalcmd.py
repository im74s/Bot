from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

COMMAND_INFO = {"name": "/eval", "desc": "Evaluate Python code (disabled by default).", "usage": "/eval <code>", "scope": "Group admins only (disabled)", "example": "/eval 1+1"}

async def handler(client, message):
    await message.reply_text("Eval is disabled for safety. Remove this placeholder to enable.")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["eval"]) & filters.group))
