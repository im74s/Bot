from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

COMMAND_INFO = {"name": "/clean", "desc": "Clean bot messages or recent messages (placeholder).", "usage": "/clean <count>", "scope": "Group admins only", "example": "/clean 50"}

async def handler(client, message):
    if not await utils.is_group_admin(client, message):
        await message.reply_text("Admins only.")
        return
    await message.reply_text("Clean placeholder: implement message deletion logic here.")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["clean"]) & filters.group))
