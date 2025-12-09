from pyrogram.types import Message

async def promote(client, message: Message):
    chat_id = message.chat.id

    # Resolve target user
    if message.reply_to_message and message.reply_to_message.from_user:
        target_user_id = message.reply_to_message.from_user.id
    else:
        parts = message.text.split(None, 1)
        if len(parts) < 2:
            await message.reply("Usage: /promote <user_id|@username> or reply to a user")
            return
        arg = parts[1].strip()
        try:
            if arg.isdigit():
                target_user_id = int(arg)
            else:
                user = await client.get_users(arg)
                target_user_id = user.id
        except Exception:
            await message.reply("Could not find the specified user.")
            return

    # Define privileges (Pyrogram 2.x)
    privileges = {
        "is_anonymous": False,
        "can_manage_chat": False,
        "can_delete_messages": True,
        "can_manage_video_chats": False,
        "can_restrict_members": True,
        "can_promote_members": False,
        "can_change_info": True,
        "can_invite_users": True,
        "can_pin_messages": True,
        "can_post_messages": False,
        "can_edit_messages": False,
        "can_manage_topics": True
    }

    try:
        await client.promote_chat_member(
            chat_id=chat_id,
            user_id=target_user_id,
            privileges=privileges
        )
        await message.reply("User promoted to admin successfully.")
    except Exception as e:
        await message.reply(f"Failed to promote user: {e}")
