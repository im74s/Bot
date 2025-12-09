from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

COMMAND_INFO = {"name": "/pin", "desc": "Pin a message (reply to message).", "usage": "/pin <reply>", "scope": "Group admins only", "example": "/pin (reply)"}

async def handler(client, message):
    if not await utils.is_group_admin(client, message):
        await message.reply_text("Admins only.")
        return
    if not message.reply_to_message:
        await message.reply_text("Reply to a message to pin it.")
        return
    try:
        await client.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
        await message.reply_text("Message pinned.")
    except Exception as e:
        await message.reply_text(f"Failed to pin: {e}")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["pin"]) & filters.group))
