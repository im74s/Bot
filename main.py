from pyrogram import Client
from Commands import Admin  # adjust if your file is Admin.py

# -------------------------------
# CONFIG - Your Telegram API info
# -------------------------------
API_ID = 22071176               # Your API_ID
API_HASH = "7ed5401b625a0a4d3c45caf12c87f166"  # Your API_HASH
BOT_TOKEN = "8248367956:AAEd42MVgLX-EMZVWVSU0tCx2-_vW4mCkxI"  # Your bot token
# -------------------------------

# Create the Pyrogram client
app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

if __name__ == "__main__":
    print("Bot is starting...")
    app.run()
