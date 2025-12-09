from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

COMMAND_INFO = {"name": "/testadmin", "desc": "Test admin check", "usage": "/testadmin", "scope": "Group", "example": "/testadmin"}

async def handler(client, message):
    chat = message.chat
    user = message.from_user
    
    await message.reply_text(f"Chat type: {chat.type}\nYour ID: {user.id}")
    
    try:
        member = await client.get_chat_member(chat.id, user.id)
        await message.reply_text(f"Your status: {member.status}\nIs admin according to utils: {await utils.is_group_admin(client, message)}")
    except Exception as e:
        await message.reply_text(f"Error getting member info: {e}")

def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["testadmin"]) & filters.group))
