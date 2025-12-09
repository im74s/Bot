from pyrogram import filters
from pyrogram.handlers import MessageHandler

COMMAND_INFO = {"name": "/dog", "desc": "Send a dog image placeholder.", "usage": "/dog", "scope": "DM and Group", "example": "/dog"}

async def handler(client, message):
    await message.reply_text("[dog image placeholder] https://placedog.net/300/300")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["dog"]) & (filters.private | filters.group)))
