from pyrogram import filters
from pyrogram.handlers import MessageHandler

COMMAND_INFO = {"name": "/cancelreminder", "desc": "Cancel reminders (not implemented).", "usage": "/cancelreminder <id>", "scope": "DM and Group", "example": "/cancelreminder 1"}

async def handler(client, message):
    await message.reply_text("Cancel reminder: not implemented in this simple version.")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["cancelreminder"]) & (filters.private | filters.group)))
