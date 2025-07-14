import os
import asyncio
import subprocess
from flask import Flask
from pyrogram import Client, filters

# Flask App (Render requires something running on a port)
web_app = Flask(__name__)

@web_app.route('/')
def index():
    return "✅ M3U8 Telegram Bot Running on Render!"

# Telegram Bot Config
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

bot = Client("m3u8_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.private & filters.text)
async def download_m3u8(client, message):
    url = message.text.strip()
    if not url.endswith(".m3u8"):
        await message.reply("❌ Please send a valid .m3u8 link.")
        return

    await message.reply("📥 Downloading your video, please wait...")

    filename = "video.mp4"
    cmd = f'yt-dlp --hls-use-mpegts -o "{filename}" "{url}"'

    try:
        process = await asyncio.create_subprocess_shell(
            cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()

        if os.path.exists(filename):
            await message.reply_video(video=filename, caption="✅ Done!")
            os.remove(filename)
        else:
            await message.reply("❌ Failed to download the video.")
    except Exception as e:
        await message.reply(f"⚠️ Error: {str(e)}")

# Run both Flask and Telegram bot together
async def start_all():
    await bot.start()
    print("✅ Telegram Bot Started")
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, lambda: web_app.run(host="0.0.0.0", port=10000))

    await idle()

from pyrogram.idle import idle

if __name__ == "__main__":
    asyncio.run(start_all())
