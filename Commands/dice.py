from pyrogram import filters
from pyrogram.handlers import MessageHandler
import random

COMMAND_INFO = {"name": "/dice", "desc": "Roll a dice (1-6).", "usage": "/dice", "scope": "DM and Group", "example": "/dice"}

async def handler(client, message):
    await message.reply_text(str(random.randint(1,6)))


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["dice"]) & (filters.private | filters.group)))
