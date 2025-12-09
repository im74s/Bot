from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

COMMAND_INFO = {"name": "/removemod", "desc": "Remove moderator (placeholder).", "usage": "/removemod <reply>", "scope": "Group admins only", "example": "/removemod (reply)"}

async def handler(client, message):
    if not await utils.is_group_admin(client, message):
        await message.reply_text("Admins only.")
        return
    await message.reply_text("Removed moderator (placeholder).")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["removemod"]) & filters.group))
