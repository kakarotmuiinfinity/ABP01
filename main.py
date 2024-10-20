import os
from telegram import Update
from telegram.ext import CommandHandler, ApplicationBuilder

# Load environment variables
BOT_TOKEN = os.getenv('BOT_TOKEN')
PORT = int(os.getenv('PORT', 8080))  # Default to 8080 if not provided
WEBHOOK_URL = os.getenv('WEBHOOK_URL')  # Webhook URL from environment variables

async def start(update: Update, context):
    """Handle the /start command with a 🔥 reaction."""
    await update.message.reply_sticker("🔥")

def main():
    # Create the bot application
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add handler for /start command
    application.add_handler(CommandHandler('start', start))

    # Start the bot with a webhook
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=BOT_TOKEN,
        webhook_url=f"{WEBHOOK_URL}/{BOT_TOKEN}"
    )

if __name__ == '__main__':
    main()
    
