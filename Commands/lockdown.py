from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

COMMAND_INFO = {"name": "/lockdown", "desc": "Restrict sending messages to admins only.", "usage": "/lockdown", "scope": "Group admins only", "example": "/lockdown"}

async def handler(client, message):
    if not await utils.is_group_admin(client, message):
        await message.reply_text("Admins only.")
        return
    try:
        await client.set_chat_permissions(message.chat.id, {"can_send_messages": False})
        await message.reply_text("Group locked down: only admins can send messages.")
    except Exception as e:
        await message.reply_text(f"Failed to lockdown: {e}")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["lockdown"]) & filters.group))
