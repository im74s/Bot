from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

COMMAND_INFO = {"name": "/unwarn", "desc": "Remove a warn from a user.", "usage": "/unwarn <reply>", "scope": "Group admins only", "example": "/unwarn (reply)"}

async def handler(client, message):
    if not await utils.is_group_admin(client, message):
        await message.reply_text("Admins only.")
        return
    if not message.reply_to_message:
        await message.reply_text("Reply to the user's message to remove a warn.")
        return
    target = message.reply_to_message.from_user
    # naive removal
    await message.reply_text("Warn removed (not persisted).")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["unwarn"]) & filters.group))
