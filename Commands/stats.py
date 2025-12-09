from pyrogram import filters
from pyrogram.handlers import MessageHandler
import time

START_TIME = time.time()

COMMAND_INFO = {"name": "/stats", "desc": "Show basic bot stats.", "usage": "/stats", "scope": "DM and Group", "example": "/stats"}

async def handler(client, message):
    uptime = int(time.time() - START_TIME)
    await message.reply_text(f"Uptime: {uptime} seconds")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["stats"]) & (filters.private | filters.group)))
