from pyrogram.types import Message

async def unban(client, message: Message):
    chat_id = message.chat.id
    parts = message.text.split(None, 1)
    if message.reply_to_message and message.reply_to_message.from_user:
        target_user_id = message.reply_to_message.from_user.id
    else:
        if len(parts) < 2:
            await message.reply("Usage: /unban <user_id|@username> or reply to a user")
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
        await client.unban_chat_member(chat_id, target_user_id)
        await message.reply("User unbanned successfully.")
    except Exception as e:
        await message.reply(f"Failed to unban user: {e}")
