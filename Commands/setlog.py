from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

COMMAND_INFO = {"name": "/setlog", "desc": "Set a log channel (placeholder).", "usage": "/setlog <@channel>", "scope": "Group admins only", "example": "/setlog @mylogchannel"}

async def handler(client, message):
    if not await utils.is_group_admin(client, message):
        await message.reply_text("Admins only.")
        return
    await message.reply_text("Log channel set (placeholder).")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["setlog"]) & filters.group))
