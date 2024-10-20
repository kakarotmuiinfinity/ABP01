import os
from telegram import Update
from telegram.ext import Application, CommandHandler

# Get environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
PORT = int(os.getenv("PORT", "8080"))
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# Function to handle /start command
async def start(update: Update, context):
    # Reaction to the /start command, sending 🔥 as a reaction
    await update.message.reply_text("🔥")  # As a reaction, not a message (adjust as needed)

# Initialize the application
app = Application.builder().token(BOT_TOKEN).build()

# Add handler for /start command
app.add_handler(CommandHandler("start", start))

# Set webhook (This is how Telegram will communicate with your bot)
async def set_webhook():
    await app.bot.set_webhook(url=WEBHOOK_URL)

# Start the bot on the specified port
if __name__ == "__main__":
    set_webhook()
    app.run_webhook(listen="0.0.0.0", port=PORT, url_path=BOT_TOKEN)
    
