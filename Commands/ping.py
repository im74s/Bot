from pyrogram import filters
from pyrogram.handlers import MessageHandler
import time

COMMAND_INFO = {"name": "/ping", "desc": "Check bot latency.", "usage": "/ping", "scope": "DM and Group", "example": "/ping"}

async def handler(client, message):
    start = time.time()
    m = await message.reply_text("Pong...")
    end = time.time()
    await m.edit_text(f"Pong! {int((end-start)*1000)} ms")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["ping"]) & (filters.private | filters.group)))
