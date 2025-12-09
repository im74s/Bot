from pyrogram import filters
from pyrogram.handlers import MessageHandler

COMMAND_INFO = {
    "name": "/start",
    "desc": "Start the bot and get basic instructions.",
    "usage": "/start",
    "scope": "DM and Group",
    "example": "/start"
}

async def start_handler(client, message):
    text = (
        "Hello! I'm your bot.\n\n"
        "Use /help to see all available commands.\n"
        "Admin commands only work for group administrators when used inside groups."
    )
    await message.reply_text(text)


def register(app):
    app.add_handler(MessageHandler(start_handler, filters.command(["start"]) & (filters.private | filters.group)))
