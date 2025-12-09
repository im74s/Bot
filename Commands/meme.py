from pyrogram import filters
from pyrogram.handlers import MessageHandler

COMMAND_INFO = {"name": "/meme", "desc": "Send a placeholder meme text.", "usage": "/meme", "scope": "DM and Group", "example": "/meme"}

async def handler(client, message):
    await message.reply_text("[meme placeholder] https://i.imgflip.com/1bij.jpg")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["meme"]) & (filters.private | filters.group)))
