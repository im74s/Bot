from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

COMMAND_INFO = {"name": "/broadcast", "desc": "Broadcast a message to a list (admin-only, placeholder).", "usage": "/broadcast <text>", "scope": "Group admins only", "example": "/broadcast Hello"}

async def handler(client, message):
    if not await utils.is_group_admin(client, message):
        await message.reply_text("Admins only.")
        return
    await message.reply_text("Broadcast placeholder: integrate your subscriber list to send messages.")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["broadcast"]) & filters.group))
