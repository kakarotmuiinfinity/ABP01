import os
import asyncio
from pyrogram import Client, filters
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# API ID and Hash for Telegram Client API
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Create a Pyrogram Client (this is your bot)
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Start command handler
@app.on_message(filters.command("start"))
async def start(client, message):
    # React to the message with a 🔥 emoji
    await message.react("🔥")
    
    # Send a sticker
    sticker_message = await message.reply_sticker("CAACAgUAAxkBAAIgL2cHg1wOoOZ7uBA5Q8uh8wF2DN1xAAIEAAPBJDExieUdbguzyBAeBA")
    
    # Wait for 2 seconds
    await asyncio.sleep(2)
    
    # Delete the sticker
    await client.delete_messages(message.chat.id, sticker_message.id)

# Start the Pyrogram client
app.run()
