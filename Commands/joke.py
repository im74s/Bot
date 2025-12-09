from pyrogram import filters
from pyrogram.handlers import MessageHandler

COMMAND_INFO = {"name": "/joke", "desc": "Send a random joke (placeholder).", "usage": "/joke", "scope": "DM and Group", "example": "/joke"}

_JOKES = ["Why did the scarecrow win an award? Because he was outstanding in his field.", "I told my computer I needed a break, and it said 'No problem - I'll go to sleep.'"]

async def handler(client, message):
    import random
    await message.reply_text(random.choice(_JOKES))


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["joke"]) & (filters.private | filters.group)))
