from pyrogram import filters
from pyrogram.handlers import MessageHandler

COMMAND_INFO = {"name": "/id", "desc": "Get your user and chat ID.", "usage": "/id", "scope": "DM and Group", "example": "/id"}

async def handler(client, message):
    uid = message.from_user.id
    cid = message.chat.id
    await message.reply_text(f"Your user id: {uid}\nChat id: {cid}")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["id"]) & (filters.private | filters.group)))
