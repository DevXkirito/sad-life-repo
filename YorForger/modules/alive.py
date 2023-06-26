from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from YorForger.events import register



PHOTO = "https://telegra.ph/file/ff2fa22dfa6ae838cc6cd.jpg"

@app.on_message(filters.command("alive"))
async def awake(client, message):
  TEXT = f"**ʜᴇʏ, ɪ ᴀᴍ ₮₳₦JłⱤØӾ₭₳₦₳Ø.** \n\n"
  TEXT += f"**➖➖➖➖➖➖➖➖➖**"
  TEXT += f"**» ᴍʏ ᴏᴡɴᴇʀ : [Kirito 『 𓃠 』](https://t.me/Kirito_est)** \n\n"
  TEXT += f"**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"**»ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n\n"
  TEXT += f"**➖➖➖➖➖➖➖➖➖**"
 
BUTTON = InlineKeyboardMarkup(
    [[
        InlineKeyboardButton("Update", url="https://t.me/TeamxXYZ"),
        InlineKeyboardButton("Support", url="https://t.me/MitsuriHelpSupport")
    ]]
)
    await client.send_photo(message.chat.id, PHOTO, caption=TEXT, reply_markup=BUTTON)
