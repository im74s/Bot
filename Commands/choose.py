from pyrogram import filters
from pyrogram.handlers import MessageHandler
import random

COMMAND_INFO = {"name": "/choose", "desc": "Choose randomly among comma-separated options.", "usage": "/choose opt1, opt2, ...", "scope": "DM and Group", "example": "/choose red, blue, green"}

async def handler(client, message):
    args = message.text.split(maxsplit=1)
    if len(args) == 1:
        await message.reply_text("Usage: /choose opt1, opt2, ...")
        return
    opts = [o.strip() for o in args[1].split(",") if o.strip()]
    if not opts:
        await message.reply_text("No options provided.")
        return
    await message.reply_text(random.choice(opts))


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["choose"]) & (filters.private | filters.group)))
