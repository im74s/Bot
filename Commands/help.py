from pyrogram import filters
from pyrogram.handlers import MessageHandler
from . import register_all

async def help_handler(client, message):
    args = message.text.split(maxsplit=1)
    if len(args) > 1:
        query = args[1].strip().lower()
        for cmd in register_all.USER_COMMANDS + register_all.ADMIN_COMMANDS:
            if cmd.get("name").lstrip("/").lower() == query.lstrip("/"):
                text = (
                    f"{cmd.get('name')} - {cmd.get('desc')}\n"
                    f"Usage: {cmd.get('usage')}\n"
                    f"Scope: {cmd.get('scope')}\n"
                    f"Example: {cmd.get('example')}\n"
                )
                await message.reply_text(text)
                return
        await message.reply_text("Command not found.")
        return

    lines = []
    lines.append("Bot Help - Full Command List\n")
    lines.append("Usage: /help <command> to get details about a single command.\n")
    lines.append("User commands:\n")
    for cmd in register_all.USER_COMMANDS:
        lines.append(f"{cmd.get('name')} - {cmd.get('desc')}\nUsage: {cmd.get('usage')}\n")
    lines.append("\nAdmin commands (group admins only):\n")
    for cmd in register_all.ADMIN_COMMANDS:
        lines.append(f"{cmd.get('name')} - {cmd.get('desc')}\nUsage: {cmd.get('usage')}\n")
    text = "\n".join(lines)
    # send in chunks to avoid exceeding limits
    chunk_size = 4000
    for i in range(0, len(text), chunk_size):
        await message.reply_text(text[i:i+chunk_size])


def register(app):
    app.add_handler(MessageHandler(help_handler, filters.command(["help"]) & (filters.private | filters.group)))
