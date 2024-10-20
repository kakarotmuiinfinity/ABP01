import os
from telegram import Update
from telegram.ext import Application, CommandHandler

# Get environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", "8080"))
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# Function to handle /start command
async def start(update: Update, context):
    # Reaction to the /start command
    await update.message.reply_text("🔥")

# Initialize the application
app = Application.builder().token(BOT_TOKEN).build()

# Add handler for /start command
app.add_handler(CommandHandler("start", start))

# Set webhook
async def set_webhook():
    await app.bot.set_webhook(url=WEBHOOK_URL)

if __name__ == "__main__":
    # Instead of using asyncio.run(), await the webhook setup and start the bot
    app.initialize()  # Initialize the app without asyncio.run()
    
    # Now set the webhook directly
    app.bot.loop.create_task(set_webhook())  # Use the current event loop to set webhook
    
    # Run the webhook, without trying to close or re-open the event loop
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=BOT_TOKEN
    )
    
