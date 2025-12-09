from pyrogram import filters
from pyrogram.handlers import MessageHandler

COMMAND_INFO = {"name": "/quote", "desc": "Send a random inspirational quote.", "usage": "/quote", "scope": "DM and Group", "example": "/quote"}

_QUOTES = ["Be yourself; everyone else is already taken.", "Do or do not. There is no try."]

async def handler(client, message):
    import random
    await message.reply_text(random.choice(_QUOTES))


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["quote"]) & (filters.private | filters.group)))
