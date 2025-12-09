from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

COMMAND_INFO = {"name": "/purge", "desc": "Purge messages (reply to start).", "usage": "/purge <count>", "scope": "Group admins only", "example": "/purge 100"}

async def handler(client, message):
    if not await utils.is_group_admin(client, message):
        await message.reply_text("Admins only.")
        return
    await message.reply_text("Purge placeholder.")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["purge"]) & filters.group))
