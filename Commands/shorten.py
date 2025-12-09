from pyrogram import filters
from pyrogram.handlers import MessageHandler

COMMAND_INFO = {"name": "/shorten", "desc": "Shorten a URL (placeholder).", "usage": "/shorten <url>", "scope": "DM and Group", "example": "/shorten https://example.com"}

async def handler(client, message):
    await message.reply_text("Shorten placeholder: integrate a URL shortener API.")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["shorten"]) & (filters.private | filters.group)))
