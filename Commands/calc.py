from pyrogram import filters
from pyrogram.handlers import MessageHandler

COMMAND_INFO = {"name": "/calc", "desc": "Calculate simple arithmetic (safe eval).", "usage": "/calc 2+2", "scope": "DM only recommended", "example": "/calc 2+3*4"}

SAFE_CHARS = set("0123456789+-*/(). %")

async def handler(client, message):
    args = message.text.split(maxsplit=1)
    if len(args) == 1:
        await message.reply_text("Usage: /calc <expression>")
        return
    expr = args[1]
    if not set(expr) <= SAFE_CHARS:
        await message.reply_text("Invalid characters in expression.")
        return
    try:
        result = eval(expr, {"__builtins__": None}, {})
        await message.reply_text(str(result))
    except Exception:
        await message.reply_text("Error evaluating expression.")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["calc"]) & (filters.private | filters.group)))
