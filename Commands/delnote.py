from pyrogram import filters
from pyrogram.handlers import MessageHandler
from .note import _NOTES

COMMAND_INFO = {"name": "/delnote", "desc": "Delete a note by index.", "usage": "/delnote <index>", "scope": "DM only recommended", "example": "/delnote 1"}

async def handler(client, message):
    args = message.text.split(maxsplit=1)
    if len(args) == 1:
        await message.reply_text("Usage: /delnote <index>")
        return
    try:
        idx = int(args[1]) - 1
    except:
        await message.reply_text("Invalid index.")
        return
    uid = message.from_user.id
    notes = _NOTES.get(uid, [])
    if 0 <= idx < len(notes):
        notes.pop(idx)
        await message.reply_text("Note deleted.")
    else:
        await message.reply_text("Index out of range.")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["delnote"]) & (filters.private | filters.group)))
