import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Command handler for /start
def start(update: Update, context: CallbackContext) -> None:
    # React with 🔥 emoji
    context.bot.send_sticker(chat_id=update.effective_chat.id, sticker="🔥")

def main() -> None:
    # Get environment variables
    bot_token = os.getenv('BOT_TOKEN')
    port = int(os.getenv('PORT', 8080))

    # Create the Updater and pass it your bot's token.
    updater = Updater(token=bot_token)

    # Register handlers
    updater.dispatcher.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_webhook(listen='0.0.0.0', port=port, url_path=bot_token)
    updater.bot.set_webhook(f'https://<your-koyeb-app-name>.koyeb.app/{bot_token}')

    updater.idle()

if __name__ == '__main__':
    main()
