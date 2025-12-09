from pyrogram import filters
from pyrogram.handlers import MessageHandler
from .note import _NOTES

COMMAND_INFO = {"name": "/listnotes", "desc": "List your saved notes.", "usage": "/listnotes", "scope": "DM only recommended", "example": "/listnotes"}

async def handler(client, message):
    uid = message.from_user.id
    notes = _NOTES.get(uid, [])
    if not notes:
        await message.reply_text("No notes saved.")
    else:
        await message.reply_text("\n".join(f"{i+1}. {n}" for i,n in enumerate(notes)))


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["listnotes"]) & (filters.private | filters.group)))
