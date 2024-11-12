import os
import re
import time
import json
import asyncio
import random
import base64
from time import sleep as wh
from random import choice
from requests import post
from urllib.parse import quote
import pyfiglet
from bs4 import BeautifulSoup
import urllib
import requests
import user_agent
from user_agent import generate_user_agent
from uuid import uuid1
from telethon import TelegramClient,events,Button,functions
from telethon.tl import functions
from telethon.events import CallbackQuery
from telethon.tl.custom import Dialog
import datetime
from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import uuid
Gm1 = 23826569 #api-id
Gm2 = '' #api-hash
GoldID = 5846480832 #id-telegram
By = '@rrrrrF' # خلي يوزرك
ch2 = ['@N_9_N_6','@N_1_N_6']
Gs1 = False
Gs2 = False
Gs3 = False
client = TelegramClient('see',Gm1,Gm2)
async def Golden1(GoldTele,text):
    try:
        return await GoldTele.message.edit(text)
    except Exception:
        return await GoldTele.reply(text)
async def mech():
    for ch1 in ch2:
        try:
            await client(JoinChannelRequest(ch1))
        except Exception:
            pass
async def ch3():
    await client.start()
    await mech()
@client.on(events.NewMessage(pattern=".خط 3"))
async def Golden2(GoldTele):
    global Gs3
    if not Gs3:
        Gs3 = True
        await GoldTele.reply(f"✅ - Done\n\n**By - ﹆ ⋆ {By} ❜ .**")
    else:
        Gs3 = False
        await GoldTele.reply(f"📛 - Done\n\n**By - ﹆ ⋆ {By} ❜ .**")
@client.on(events.NewMessage(pattern=".ايقاف 3"))
async def Golden3(GoldTele):
    global Gs3
    if Gs3:
        Gs3 = False
        await GoldTele.reply("📛 - Done\n\n**By - ﹆ ⋆ {By} ❜ .**")
    else:
        Gs3 = True
        await GoldTele.reply(f"✅ - Done\n\n**By - ﹆ ⋆ {By} ❜ .**")
@client.on(events.NewMessage(pattern=".خط 2"))
async def Golden4(GoldTele):
    global Gs2
    if not Gs2:
        Gs2 = True
        await GoldTele.reply(f"✅ - Done\n\n**By - ﹆ ⋆ {By} ❜ .**")
    else:
        Gs2 = False
        await GoldTele.reply(f"📛 - Done\n\n**By - ﹆ ⋆ {By} ❜ .**")
@client.on(events.NewMessage(pattern=".ايقاف 2"))
async def Golden5(GoldTele):
    global Gs2
    if Gs2:
        Gs2 = False
        await GoldTele.reply(f"📛 - Done\n\n**By - ﹆ ⋆ {By} ❜ .**")
    else:
        Gs2 = True
        await GoldTele.reply(f"✅ - Done\n\n**By - ﹆ ⋆ {By} ❜ .**")
@client.on(events.NewMessage(pattern=".خط 1"))
async def Golden6(GoldTele):
    global Gs1
    if not Gs1:
        Gs1 = True
        await GoldTele.reply(f"✅ - Done\n\n**By - ﹆ ⋆ {By} ❜ .**")
    else:
        Gs1 = False
        await GoldTele.reply(f"📛 - Done\n\n**By - ﹆ ⋆ {By} ❜ .**")
@client.on(events.NewMessage(pattern=".ايقاف 1"))
async def Golden7(GoldTele):
    global Gs1
    if Gs1:
        Gs1 = False
        await GoldTele.reply(f"📛 - Done\n\n**By - ﹆ ⋆ {By} ❜ .**")
    else:
        Gs1 = True
        await GoldTele.reply(f"✅ - Done\n\n**By - ﹆ ⋆ {By} ❜ .**")
@client.on(events.NewMessage(outgoing=True))
async def Golden8(GoldTele):
    global Gs1,Gs2,Gs3
    if Gs1:
        try:
            await GoldTele.edit(f"**{GoldTele.message.message}**")
        except Exception:
            pass
    if Gs2:
        try:
            await GoldTele.edit(f"`{GoldTele.message.message}`")
        except Exception:
            pass
    if Gs3:
        try:
            await GoldTele.edit(f"__{GoldTele.message.message}__")
        except Exception:
            pass
client.start()
client.run_until_disconnected()
