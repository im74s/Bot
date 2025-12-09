from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

COMMAND_INFO = {"name": "/unmute", "desc": "Unmute a user.", "usage": "/unmute <reply or @username>", "scope": "Group admins only", "example": "/unmute (reply)"}

async def handler(client, message):
    if not await utils.is_group_admin(client, message):
        await message.reply_text("Admins only.")
        return
    target = message.reply_to_message.from_user if message.reply_to_message else None
    if not target:
        args = message.text.split(maxsplit=1)
        if len(args) > 1:
            target = await client.get_users(args[1])
    if not target:
        await message.reply_text("Usage: /unmute <reply or @username>")
        return
    try:
        await client.restrict_chat_member(message.chat.id, target.id, can_send_messages=True)
        await message.reply_text("User unmuted.")
    except Exception as e:
        await message.reply_text(f"Failed to unmute: {e}")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["unmute"]) & filters.group))
