from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

COMMAND_INFO = {"name": "/unlock", "desc": "Remove lockdown and allow members to send messages.", "usage": "/unlock", "scope": "Group admins only", "example": "/unlock"}

async def handler(client, message):
    if not await utils.is_group_admin(client, message):
        await message.reply_text("Admins only.")
        return
    try:
        await client.set_chat_permissions(message.chat.id, {"can_send_messages": True, "can_send_media_messages": True, "can_send_other_messages": True})
        await message.reply_text("Group unlocked.")
    except Exception as e:
        await message.reply_text(f"Failed to unlock: {e}")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["unlock"]) & filters.group))
