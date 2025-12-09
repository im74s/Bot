from pyrogram import Client

# -------------------------------
# CONFIG - Your Telegram API info
# -------------------------------
API_ID = 22071176
API_HASH = "7ed5401b625a0a4d3c45caf12c87f166"
BOT_TOKEN = "7918136133:AAEdGPNoeRAtory8zUGKR8-dBU6GAJNQ5D8"
# -------------------------------

# Create the Pyrogram client
app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Register admin command handlers once the app is created
from Commands import admin_commands
admin_commands.register_admin_commands(app)

if __name__ == "__main__":
    print("Bot is starting...")
    app.run()
