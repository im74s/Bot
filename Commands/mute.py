from pyrogram.types import Message, ChatPermissions

async def mute(client, message: Message):
    chat_id = message.chat.id
    if message.reply_to_message and message.reply_to_message.from_user:
        target_user_id = message.reply_to_message.from_user.id
    else:
        parts = message.text.split(None, 1)
        if len(parts) < 2:
            await message.reply("Usage: /mute <user_id|@username> or reply to a user")
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
        await client.restrict_chat_member(
            chat_id,
            target_user_id,
            permissions=ChatPermissions(
                can_send_messages=False,
                can_send_media_messages=False,
                can_send_other_messages=False,
                can_add_web_page_previews=False,
            ),
        )
        await message.reply("User muted successfully.")
    except Exception as e:
        await message.reply(f"Failed to mute user: {e}")
