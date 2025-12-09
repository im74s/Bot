from pyrogram import filters
from pyrogram.handlers import MessageHandler
import time

COMMAND_INFO = {"name": "/uptime", "desc": "Show bot uptime.", "usage": "/uptime", "scope": "DM and Group", "example": "/uptime"}

START_TIME = time.time()

async def handler(client, message):
    await message.reply_text(str(int(time.time() - START_TIME)) + " seconds")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["uptime"]) & (filters.private | filters.group)))
