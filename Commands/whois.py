from pyrogram import filters
from pyrogram.handlers import MessageHandler

COMMAND_INFO = {"name": "/whois", "desc": "Get info about a user via reply or @username.", "usage": "/whois <reply or @username>", "scope": "DM and Group", "example": "/whois @username"}

async def handler(client, message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user
    else:
        args = message.text.split(maxsplit=1)
        if len(args) == 1:
            await message.reply_text("Usage: /whois <reply or @username>")
            return
        user = await client.get_users(args[1])
    info = f"ID: {user.id}\nName: {user.first_name or ''} {user.last_name or ''}\nUsername: @{user.username or 'n/a'}"
    await message.reply_text(info)


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["whois"]) & (filters.private | filters.group)))
