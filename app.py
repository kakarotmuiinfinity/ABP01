import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler

# Get environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", "8080"))
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# Function to handle /start command
async def start(update: Update, context):
    # Send 🔥 emoji as a reaction to the /start command
    await update.message.reply_text("🔥")

# Initialize the application
app = Application.builder().token(BOT_TOKEN).build()

# Add handler for /start command
app.add_handler(CommandHandler("start", start))

# Set webhook
async def set_webhook():
    await app.bot.set_webhook(url=WEBHOOK_URL)

if __name__ == "__main__":
    # Create an async context for setting the webhook and running the bot
    async def main():
        # Set webhook before starting the bot
        await set_webhook()
        
        # Start the webhook
        app.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=BOT_TOKEN
        )

    # Run the async main function
    asyncio.run(main())
    
