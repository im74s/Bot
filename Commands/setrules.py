from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

COMMAND_INFO = {"name": "/setrules", "desc": "Set group rules (placeholder).", "usage": "/setrules <text>", "scope": "Group admins only", "example": "/setrules Be kind"}

async def handler(client, message):
    if not await utils.is_group_admin(client, message):
        await message.reply_text("Admins only.")
        return
    await message.reply_text("Rules set (placeholder).")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["setrules"]) & filters.group))
