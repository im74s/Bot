from pyrogram import filters
from pyrogram.handlers import MessageHandler
import datetime

COMMAND_INFO = {"name": "/time", "desc": "Show server time.", "usage": "/time", "scope": "DM and Group", "example": "/time"}

async def handler(client, message):
    now = datetime.datetime.utcnow()
    await message.reply_text(f"UTC time: {now.isoformat()}Z")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["time"]) & (filters.private | filters.group)))
