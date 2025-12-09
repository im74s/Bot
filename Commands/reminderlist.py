from pyrogram import filters
from pyrogram.handlers import MessageHandler

COMMAND_INFO = {"name": "/reminderlist", "desc": "List active reminders (not persistent).", "usage": "/reminderlist", "scope": "DM and Group", "example": "/reminderlist"}

async def handler(client, message):
    await message.reply_text("Reminder listing not persisted in this simple implementation.")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["reminderlist"]) & (filters.private | filters.group)))
