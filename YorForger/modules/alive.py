import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from YorForger.events import register
from YorForger import telethn as tbot


PHOTO = "https://telegra.ph/file/ff2fa22dfa6ae838cc6cd.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ʜᴇʏ, ɪ ᴀᴍ ₮₳₦JłⱤØӾ₭₳₦₳Ø.** \n\n"
  TEXT += f"**➖➖➖➖➖➖➖➖➖**"
  TEXT += f"**» ᴍʏ ᴏᴡɴᴇʀ : [Kirito 『 𓃠 』](https://t.me/Kirito_est)** \n\n"
  TEXT += f"**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"**»ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n\n"
  TEXT += f"**➖➖➖➖➖➖➖➖➖**"
  BUTTON = [[Button.url("Update", "https://t.me/TeamxXYZ"), Button.url("Support", "https://t.me/MitsuriHelpSupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
