from pyrogram import Client
import logging

# -------------------------------
# CONFIGURE LOGGING FIRST
# -------------------------------
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Print to console
        logging.FileHandler('bot.log')  # Save to file
    ]
)

logger = logging.getLogger(__name__)

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

# Register command handlers once the app is created
from Commands import register_all

if __name__ == "__main__":
    logger.info("=" * 50)
    logger.info("Bot is starting...")
    logger.info("Registering commands...")
    logger.info("=" * 50)
    
    register_all.register(app)
    
    logger.info("All commands registered successfully!")
    logger.info("Bot is now running...")
    
    app.run()
