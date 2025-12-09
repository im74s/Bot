from pyrogram import filters
from pyrogram.handlers import MessageHandler

COMMAND_INFO = {"name": "/avatar", "desc": "Get avatar of a user (reply or username).", "usage": "/avatar <reply or @username>", "scope": "DM and Group", "example": "/avatar @username"}

async def handler(client, message):
    target = None
    if message.reply_to_message:
        target = message.reply_to_message.from_user
    else:
        args = message.text.split(maxsplit=1)
        if len(args) > 1:
            target = await client.get_users(args[1])
    if not target:
        await message.reply_text("Usage: /avatar <reply or @username>")
        return
    photos = await client.get_user_photos(target.id, limit=1)
    if photos.total_count == 0:
        await message.reply_text("User has no avatar.")
        return
    await client.send_photo(message.chat.id, photos.photos[0].file_id)


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["avatar"]) & (filters.private | filters.group)))
