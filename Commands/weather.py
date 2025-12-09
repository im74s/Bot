from pyrogram import filters
from pyrogram.handlers import MessageHandler

COMMAND_INFO = {"name": "/weather", "desc": "Get weather for a city (placeholder).", "usage": "/weather <city>", "scope": "DM and Group", "example": "/weather London"}

async def handler(client, message):
    await message.reply_text("Weather placeholder: integrate an API for real data.")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["weather"]) & (filters.private | filters.group)))
