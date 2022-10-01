import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SiestaRobot.events import register
from SiestaRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/7e6354fd5e96a108d2da5.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**𝙃𝙞 [{event.sender.first_name}](tg://user?id={event.sender.id}), 𝙄'𝙢 𝘼𝙞 𝙃𝙖𝙮𝙖𝙨𝙖𝙠𝙖.** \n\n"
  TEXT += "💠 **𝙄'𝙈 𝙒𝙤𝙧𝙠𝙞𝙣𝙜 𝙋𝙧𝙤𝙥𝙚𝙧𝙡𝙮** \n\n"
  TEXT += f"💠 **𝙈𝙮 𝙇𝙤𝙧𝙙 : [𝙋𝙚𝙣𝙙𝙧𝙖𝙜𝙤𝙣](https://t.me/deadlyXrd)** \n\n"
  TEXT += f"💠 **𝙇𝙞𝙗𝙧𝙖𝙧𝙮 𝙑𝙚𝙧𝙨𝙞𝙤𝙣 :** `{telever}` \n\n"
  TEXT += f"💠 **𝙏𝙚𝙡𝙚𝙩𝙝𝙤𝙣 𝙑𝙚𝙧𝙨𝙞𝙤𝙣 :** `{tlhver}` \n\n"
  TEXT += f"💠 **𝙋𝙮𝙧𝙤𝙜𝙧𝙖𝙢 𝙑𝙚𝙧𝙨𝙞𝙤𝙣 :** `{pyrover}` \n\n"
  TEXT += "**𝙏𝙝𝙖𝙣𝙠𝙨 𝙁𝙤𝙧 𝘼𝙙𝙙𝙞𝙣𝙜 𝙈𝙚 𝙃𝙚𝙧𝙚 ❤️**"
  BUTTON = [[Button.url("Help", "https://t.me/Siestaxbot?start=help"), Button.url("Support", "https://t.me/hayasakateamsupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
