from pyrogram import filters
from . import register_all

def register(app):
    @app.on_message(filters.command("help") & (filters.private | filters.group))
    async def help_handler(client, message):
        args = message.text.split(maxsplit=1)

        if len(args) > 1:
            query = args[1].strip().lower()

            for cmd in register_all.USER_COMMANDS + register_all.ADMIN_COMMANDS:
                if cmd["name"].lstrip("/").lower() == query.lstrip("/"):
                    await message.reply_text(
                        f"{cmd['name']} - {cmd['desc']}\n"
                        f"Usage: {cmd['usage']}\n"
                        f"Scope: {cmd['scope']}\n"
                        f"Example: {cmd['example']}"
                    )
                    return

            await message.reply_text("Command not found.")
            return

        lines = [
            "Bot Help - Full Command List\n",
            "Usage: /help <command>\n",
            "User commands:\n",
        ]

        for cmd in register_all.USER_COMMANDS:
            lines.append(f"{cmd['name']} - {cmd['desc']}\nUsage: {cmd['usage']}\n")

        lines.append("\nAdmin commands:\n")

        for cmd in register_all.ADMIN_COMMANDS:
            lines.append(f"{cmd['name']} - {cmd['desc']}\nUsage: {cmd['usage']}\n")

        text = "\n".join(lines)

        for i in range(0, len(text), 4000):
            await message.reply_text(text[i:i + 4000])
