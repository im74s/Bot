from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

COMMAND_INFO = {"name": "/getadmins", "desc": "List group administrators.", "usage": "/getadmins", "scope": "Group admins only", "example": "/getadmins"}

async def handler(client, message):
    if not await utils.is_group_admin(client, message):
        await message.reply_text("Admins only.")
        return
    admins = await client.get_chat_members(message.chat.id, filter="administrators")
    text = "\n".join([f"{a.user.first_name} @{a.user.username or ''} ({a.user.id})" for a in admins])
    await message.reply_text(text)


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["getadmins"]) & filters.group))
