from pyrogram import filters

async def is_group_admin(client, message):
    # Returns True if message is in a group/supergroup and sender is an admin or creator
    chat = message.chat
    if chat.type not in ("group", "supergroup"):
        return False
    try:
        member = await client.get_chat_member(chat.id, message.from_user.id)
        status = member.status
        return status in ("administrator", "creator")
    except Exception:
        return False
