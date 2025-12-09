from pyrogram import filters
from pyrogram.handlers import MessageHandler

# Simple in-memory notes per user
_NOTES = {}

COMMAND_INFO = {"name": "/note", "desc": "Save a private note.", "usage": "/note <text>", "scope": "DM only recommended", "example": "/note buy milk"}

async def handler(client, message):
    args = message.text.split(maxsplit=1)
    if len(args) == 1:
        await message.reply_text("Usage: /note <text>")
        return
    uid = message.from_user.id
    _NOTES.setdefault(uid, []).append(args[1])
    await message.reply_text("Note saved.")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["note"]) & (filters.private | filters.group)))
