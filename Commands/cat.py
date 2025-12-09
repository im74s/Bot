from pyrogram import filters
from pyrogram.handlers import MessageHandler

COMMAND_INFO = {"name": "/cat", "desc": "Send a cat image placeholder.", "usage": "/cat", "scope": "DM and Group", "example": "/cat"}

async def handler(client, message):
    await message.reply_text("[cat image placeholder] https://placekitten.com/300/300")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["cat"]) & (filters.private | filters.group)))
