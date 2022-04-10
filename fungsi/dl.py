from datetime import datetime
import requests
import time
from bs4 import BeautifulSoup
import io
import sys
import traceback
from pyrogram import Client
from pyrogram import filters

import asyncio




@Client.on_message(filters.command("mega") & filters.private & filters.incoming)
async def lendrive(_, message):
    await message.reply_text("bentar bro...")
    url = str(message.text).split(" ")[1]
    print(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    for a in soup.find_all('a', href=True):
        if "mega.nz" in a['href']:
            await message.reply_text(a['href'])



@Client.on_message(filters.command("zip") & filters.private & filters.incoming)
async def lendrive(_, message):
    await message.reply_text("bentar bro...")
    url = str(message.text).split(" ")[1]
    print(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    for a in soup.find_all('a', href=True):
        if "zippyshare.com" in a['href']:
            await message.reply_text(a['href'])




    #pesan = await message.reply_text("halo")


