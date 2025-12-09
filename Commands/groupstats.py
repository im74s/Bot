from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

COMMAND_INFO = {"name": "/groupstats", "desc": "Show basic group stats.", "usage": "/groupstats", "scope": "Group admins only", "example": "/groupstats"}

async def handler(client, message):
    if not await utils.is_group_admin(client, message):
        await message.reply_text("Admins only.")
        return
    members = await client.get_chat_members_count(message.chat.id)
    await message.reply_text(f"Members: {members}")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["groupstats"]) & filters.group))
