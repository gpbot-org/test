import os
from flask import Flask
from telethon import TelegramClient, events
from threading import Thread

# Initialize Flask app
app = Flask(__name__)

# Retrieve environment variables using os
api_id = int(os.getenv("ID"))
api_hash = os.getenv("HASH")
bot_token = os.getenv("TOKEN")

# Initialize Telethon client with bot token
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# Flask route for Render's health check
@app.route('/')
def health_check():
    return "Bot is running!", 200

# Telethon event handler
@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply("Hello! The bot is running with Telethon.")

# Start Flask in a separate thread
def run_flask():
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))

# Start Telethon client in the main thread
def run_telethon():
    client.run_until_disconnected()

# Start both Flask and Telethon
if __name__ == "__main__":
    Thread(target=run_flask).start()  # Run Flask in a thread
    run_telethon()  # Run Telethon in the main thread
