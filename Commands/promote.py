from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

COMMAND_INFO = {"name": "/promote", "desc": "Promote a user to admin (group admins only).", "usage": "/promote <reply or @username>", "scope": "Group admins only", "example": "/promote @user"}

async def handler(client, message):
    if not await utils.is_group_admin(client, message):
        await message.reply_text("Admins only.")
        return
    target = message.reply_to_message.from_user if message.reply_to_message else None
    if not target:
        await message.reply_text("Usage: /promote <reply or @username>")
        return
    try:
        await client.promote_chat_member(message.chat.id, target.id, can_change_info=True, can_delete_messages=True, can_invite_users=True, can_pin_messages=True, can_promote_members=False)
        await message.reply_text("User promoted to admin (with limited rights).")
    except Exception as e:
        await message.reply_text(f"Failed to promote: {e}")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["promote"]) & filters.group))
