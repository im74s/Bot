from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils
import datetime

COMMAND_INFO = {"name": "/mute", "desc": "Mute a user for X minutes.", "usage": "/mute <minutes> <reply or @username>", "scope": "Group admins only", "example": "/mute 10 (reply)"}

async def handler(client, message):
    if not await utils.is_group_admin(client, message):
        await message.reply_text("Admins only.")
        return
    args = message.text.split(maxsplit=2)
    if len(args) < 2:
        await message.reply_text("Usage: /mute <minutes> <reply or @username>")
        return
    try:
        minutes = int(args[1])
    except:
        await message.reply_text("Invalid minutes value.")
        return
    target = message.reply_to_message.from_user if message.reply_to_message else None
    if not target and len(args) < 3:
        await message.reply_text("Reply or provide username to mute.")
        return
    if not target:
        target = await client.get_users(args[2])
    until = datetime.datetime.utcnow() + datetime.timedelta(minutes=minutes)
    try:
        await client.restrict_chat_member(message.chat.id, target.id, until_date=until, can_send_messages=False)
        await message.reply_text("User muted.")
    except Exception as e:
        await message.reply_text(f"Failed to mute: {e}")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["mute"]) & filters.group))
