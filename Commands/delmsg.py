from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

COMMAND_INFO = {"name": "/delmsg", "desc": "Delete a specific message by id.", "usage": "/delmsg <message_id>", "scope": "Group admins only", "example": "/delmsg 12345"}

async def handler(client, message):
    if not await utils.is_group_admin(client, message):
        await message.reply_text("Admins only.")
        return
    args = message.text.split(maxsplit=1)
    if len(args) == 1:
        await message.reply_text("Usage: /delmsg <message_id>")
        return
    try:
        mid = int(args[1])
        await client.delete_messages(message.chat.id, mid)
        await message.reply_text("Message deleted.")
    except Exception as e:
        await message.reply_text(f"Failed to delete message: {e}")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["delmsg"]) & filters.group))
