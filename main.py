import asyncio
from pyrogram import Client
from Commands import Admin  # if the file is Admin.py

# -------------------------------
# CONFIG - Replace these values
# -------------------------------
API_ID = 22071176              # Your Telegram API_ID
API_HASH = "7ed5401b625a0a4d3c45caf12c87f166"   # Your Telegram API_HASH
BOT_TOKEN = "8248367956:AAEd42MVgLX-EMZVWVSU0tCx2-_vW4mCkxI"  # Your bot to>
# -------------------------------

# Create the Pyrogram client
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKE>

# Run the bot
if __name__ == "__main__":
    print("Bot is starting...")
    app.run()



