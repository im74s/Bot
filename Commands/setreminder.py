from pyrogram import filters
from pyrogram.handlers import MessageHandler
import asyncio

# simple in-memory reminders per chat
_REMINDERS = {}

COMMAND_INFO = {"name": "/setreminder", "desc": "Set a one-off reminder in minutes.", "usage": "/setreminder <minutes> <text>", "scope": "DM and Group (works only while bot runs)", "example": "/setreminder 10 Take a break"}

async def handler(client, message):
    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        await message.reply_text("Usage: /setreminder <minutes> <text>")
        return
    try:
        minutes = int(args[1])
    except:
        await message.reply_text("Invalid minutes value.")
        return
    text = args[2]
    chat_id = message.chat.id
    async def job():
        await asyncio.sleep(minutes*60)
        await client.send_message(chat_id, f"Reminder: {text}")
    asyncio.create_task(job())
    await message.reply_text(f"Reminder set in {minutes} minutes.")


def register(app):
    app.add_handler(MessageHandler(handler, filters.command(["setreminder"]) & (filters.private | filters.group)))
