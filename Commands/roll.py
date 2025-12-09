from pyrogram import filters
from pyrogram.handlers import MessageHandler
import random

COMMAND_INFO = {"name": "/roll", "desc": "Roll dice, default 6 sides.", "usage": "/roll [sides]", "scope": "DM and Group", "example": "/roll 20"}

async def handler(client, message):
    args = message.text.split()
    sides = 6
    if len(args) > 1:
        try:
            sides = max(1, int(args[1]))
        except:
            pass
    await message.reply_text(str(random.randint(1, sides)))


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["roll"]) & (filters.private | filters.group)))
