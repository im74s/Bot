from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils
import os, sys

COMMAND_INFO = {"name": "/restart", "desc": "Restart the bot process (placeholder).", "usage": "/restart", "scope": "Group admins only", "example": "/restart"}

async def handler(client, message):
    if not await utils.is_group_admin(client, message):
        await message.reply_text("Admins only.")
        return
    await message.reply_text("Restarting (placeholder).")
    # actual restart would re-launch the process; left as placeholder


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["restart"]) & filters.group))
