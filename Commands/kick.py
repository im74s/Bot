from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

COMMAND_INFO = {"name": "/kick", "desc": "Kick a user (group admins only).", "usage": "/kick <reply or @username>", "scope": "Group admins only", "example": "/kick @user"}

async def handler(client, message):
    if not await utils.is_group_admin(client, message):
        await message.reply_text("Admins only: this command works in groups for group admins.")
        return
    target = message.reply_to_message.from_user if message.reply_to_message else None
    if not target:
        args = message.text.split(maxsplit=1)
        if len(args) > 1:
            target = await client.get_users(args[1])
    if not target:
        await message.reply_text("Usage: /kick <reply or @username>")
        return
    try:
        await client.kick_chat_member(message.chat.id, target.id)
        await client.unban_chat_member(message.chat.id, target.id)
        await message.reply_text("User kicked.")
    except Exception as e:
        await message.reply_text(f"Failed to kick: {e}")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["kick"]) & filters.group))
