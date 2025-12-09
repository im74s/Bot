from pyrogram import filters
from pyrogram.handlers import MessageHandler

COMMAND_INFO = {"name": "/math", "desc": "Math expression (wrapper for /calc).", "usage": "/math <expression>", "scope": "DM and Group", "example": "/math 1+1"}

async def handler(client, message):
    await client.send_message(message.chat.id, "Use /calc for math. This is an alias.")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["math"]) & (filters.private | filters.group)))
