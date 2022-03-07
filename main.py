import asyncio
from pyrogram import filters, Client
from config import Config
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

Flux = Client("Test",
               api_id=Config.API_ID,
               api_hash=Config.API_HASH,
               bot_token=Config.BOT_TOKEN
          )

START_TXT = """👋 Hi There!\n\nThis Bot Is Made For Testing Purposes 🌀\n\n If You Want To Contribute, Help The Developer In Learning Pyrogram 🛠."""
@Flux.on_message(filters.command(["start"]))
async def start(Client, message):
  await message.reply_text(
    text="Hi",
    disable_web_page_preview =True,
    reply_markup = InlineKeyboardMarkup(
      [
        [InlineKeyboardButton('Developer', url='t.me/TheMalwareAwakens'), InlineKeyboardButton('Bots', url='t.me/TheMalwareZone')]
      ]
    )
  )
  
Flux.run()
