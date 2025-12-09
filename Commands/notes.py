from pyrogram import filters
from pyrogram.handlers import MessageHandler
from .note import _NOTES

COMMAND_INFO = {"name": "/notes", "desc": "Count your notes.", "usage": "/notes", "scope": "DM only recommended", "example": "/notes"}

async def handler(client, message):
    uid = message.from_user.id
    await message.reply_text(f"You have {len(_NOTES.get(uid,[]))} notes.")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["notes"]) & (filters.private | filters.group)))
