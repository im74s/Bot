from pyrogram import filters
from pyrogram.handlers import MessageHandler

COMMAND_INFO = {"name": "/echo", "desc": "Echo back provided text.", "usage": "/echo <text>", "scope": "DM and Group", "example": "/echo hello"}

async def handler(client, message):
    args = message.text.split(maxsplit=1)
    if len(args) == 1:
        await message.reply_text("Usage: /echo <text>")
        return
    await message.reply_text(args[1])


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["echo"]) & (filters.private | filters.group)))
