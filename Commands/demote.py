from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

COMMAND_INFO = {"name": "/demote", "desc": "Demote an admin to regular user (group admins only).", "usage": "/demote <reply or @username>", "scope": "Group admins only", "example": "/demote @user"}

async def handler(client, message):
    if not await utils.is_group_admin(client, message):
        await message.reply_text("Admins only.")
        return
    if not message.reply_to_message:
        await message.reply_text("Usage: /demote <reply to admin message>")
        return
    target = message.reply_to_message.from_user
    try:
        await client.promote_chat_member(message.chat.id, target.id, can_change_info=False, can_delete_messages=False, can_invite_users=False, can_pin_messages=False, can_promote_members=False)
        await message.reply_text("User demoted.")
    except Exception as e:
        await message.reply_text(f"Failed to demote: {e}")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["demote"]) & filters.group))
