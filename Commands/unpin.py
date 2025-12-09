from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

COMMAND_INFO = {"name": "/unpin", "desc": "Unpin the current pinned message.", "usage": "/unpin", "scope": "Group admins only", "example": "/unpin"}

async def handler(client, message):
    if not await utils.is_group_admin(client, message):
        await message.reply_text("Admins only.")
        return
    try:
        await client.unpin_chat_message(message.chat.id)
        await message.reply_text("Unpinned.")
    except Exception as e:
        await message.reply_text(f"Failed to unpin: {e}")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["unpin"]) & filters.group))
