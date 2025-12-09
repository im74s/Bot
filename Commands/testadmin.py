from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import utils

COMMAND_INFO = {
    "name": "/testadmin",
    "desc": "Test admin permissions and debug",
    "usage": "/testadmin",
    "scope": "Group",
    "example": "/testadmin"
}

async def handler(client, message):
    chat = message.chat
    user = message.from_user
    
    # Basic info
    info_lines = []
    info_lines.append("🔍 DEBUG INFO:")
    info_lines.append(f"├─ Chat Type: {chat.type}")
    info_lines.append(f"├─ Chat ID: {chat.id}")
    info_lines.append(f"├─ Chat Title: {chat.title or 'N/A'}")
    info_lines.append(f"├─ Your ID: {user.id}")
    info_lines.append(f"├─ Your Username: @{user.username or 'N/A'}")
    info_lines.append(f"└─ Your Name: {user.first_name or 'N/A'}")
    
    await message.reply_text("\n".join(info_lines))
    
    # Try to get member status
    try:
        member = await client.get_chat_member(chat.id, user.id)
        
        status_lines = []
        status_lines.append("\n✅ MEMBER STATUS:")
        status_lines.append(f"├─ Status: {member.status}")
        status_lines.append(f"├─ Is Admin (raw): {member.status in ('administrator', 'creator')}")
        status_lines.append(f"└─ Is Admin (utils): {await utils.is_group_admin(client, message)}")
        
        await message.reply_text("\n".join(status_lines))
        
    except Exception as e:
        error_msg = f"❌ ERROR:\n{type(e).__name__}: {e}"
        await message.reply_text(error_msg)

def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["testadmin"]) & filters.group))
