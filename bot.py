import os
import time
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler
import asyncio
from dotenv import load_dotenv

# Load environment variables from .env if present (for local development)
load_dotenv()

# Define the command handler for /start
async def start(update: Update, context):
    # React with 🔥
    await update.message.react("🔥")
    
    # Send the sticker
    sticker_message = await update.message.reply_sticker(sticker="CAACAgUAAxkBAAIgL2cHg1wOoOZ7uBA5Q8uh8wF2DN1xAAIEAAPBJDExieUdbguzyBAeBA")
    
    # Wait for 2 seconds
    await asyncio.sleep(2)
    
    # Delete the sticker
    await context.bot.delete_message(chat_id=sticker_message.chat_id, message_id=sticker_message.message_id)

# Main function to start the bot
def main():
    # Load the bot token from the environment variable
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    
    if not TOKEN:
        raise ValueError("No Telegram Bot Token provided. Set the TELEGRAM_BOT_TOKEN environment variable.")
    
    # Create the bot application
    application = ApplicationBuilder().token(TOKEN).build()

    # Add handler for /start command
    application.add_handler(CommandHandler("start", start))

    # Start polling or webhook based on environment
    USE_WEBHOOK = os.getenv("USE_WEBHOOK", "false").lower() == "true"

    if USE_WEBHOOK:
        # Webhook setup for production
        PORT = int(os.getenv("PORT", 8080))
        URL = os.getenv("WEBHOOK_URL")  # You must set your public URL in the environment

        application.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=TOKEN,
            webhook_url=f"{URL}/{TOKEN}"  # Telegram requires a full URL for the webhook
        )
    else:
        # Polling setup for development or simpler deployment
        application.run_polling()

if __name__ == "__main__":
    main()
