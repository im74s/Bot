from pyrogram.enums import ChatMemberStatus

def admin_only(func):
    async def wrapper(client, message):
        if message.chat.type not in ("group", "supergroup"):
            await message.reply_text("This command only works in groups.")
            return

        if message.sender_chat:
            return await func(client, message)

        if not message.from_user:
            await message.reply_text("Anonymous admins are not supported.")
            return

        member = await client.get_chat_member(
            message.chat.id,
            message.from_user.id
        )

        if member.status not in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            await message.reply_text("Admins only.")
            return

        return await func(client, message)

    return wrapper
