from pyrogram import filters
from pyrogram.handlers import MessageHandler

COMMAND_INFO = {"name": "/translate", "desc": "Translate text (placeholder).", "usage": "/translate <lang> <text>", "scope": "DM and Group", "example": "/translate es Hello"}

async def handler(client, message):
    await message.reply_text("Translation placeholder: function not implemented.")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["translate"]) & (filters.private | filters.group)))
