from pyrogram.types import Message

async def demote(client, message: Message):
    chat_id = message.chat.id
    if message.reply_to_message and message.reply_to_message.from_user:
        target_user_id = message.reply_to_message.from_user.id
    else:
        parts = message.text.split(None, 1)
        if len(parts) < 2:
            await message.reply("Usage: /demote <user_id|@username> or reply to a user")
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

    try:
        # demote by removing admin privileges
        await client.promote_chat_member(
            chat_id,
            target_user_id,
            is_anonymous=False,
            can_change_info=False,
            can_post_messages=False,
            can_edit_messages=False,
            can_delete_messages=False,
            can_invite_users=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False,
        )
        await message.reply("User demoted from admin successfully.")
    except Exception as e:
        await message.reply(f"Failed to demote user: {e}")
