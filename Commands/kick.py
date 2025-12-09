from pyrogram import filters
from pyrogram.types import ChatPermissions, Message

async def kick(client, message: Message):
    chat_id = message.chat.id
    # determine target user
    if message.reply_to_message and message.reply_to_message.from_user:
        target_user_id = message.reply_to_message.from_user.id
    else:
        parts = message.text.split(None, 1)
        if len(parts) < 2:
            await message.reply("Usage: /kick <user_id|@username> or reply to a user")
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

    # permission checks: only admins can invoke
    try:
        invoker = await client.get_chat_member(chat_id, message.from_user.id)
        if invoker.status not in ("administrator", "creator"):
            await message.reply("You must be an admin to use this command.")
            return
    except Exception:
        pass

    # kick = ban then unban so user can rejoin
    try:
        await client.ban_chat_member(chat_id, target_user_id)
        await client.unban_chat_member(chat_id, target_user_id)
        await message.reply("User kicked successfully.")
    except Exception as e:
        await message.reply(f"Failed to kick user: {e}")
