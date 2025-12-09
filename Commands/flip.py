from pyrogram import filters
from pyrogram.handlers import MessageHandler
import random

COMMAND_INFO = {"name": "/flip", "desc": "Flip a coin.", "usage": "/flip", "scope": "DM and Group", "example": "/flip"}

async def handler(client, message):
    await message.reply_text(random.choice(["Heads", "Tails"]))


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["flip"]) & (filters.private | filters.group)))
