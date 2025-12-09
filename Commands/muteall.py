from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

COMMAND_INFO = {"name": "/muteall", "desc": "Mute all non-admins (placeholder).", "usage": "/muteall", "scope": "Group admins only", "example": "/muteall"}

async def handler(client, message):
    if not await utils.is_group_admin(client, message):
        await message.reply_text("Admins only.")
        return
    await message.reply_text("Muteall placeholder: use restrict_chat_member in a loop to mute members.")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["muteall"]) & filters.group))
