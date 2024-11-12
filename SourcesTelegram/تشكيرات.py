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
ch2 = ['@N_9_N_6','@N_1_N_6']
Geeemo = ["?","??","??","??","??","??","??","??","??","??","??","??","??","??","??"]
client = TelegramClient('see',Gm1,Gm2)
async def mech():
    for ch1 in ch2:
        try:
            await client(JoinChannelRequest(ch1))
        except Exception:
            pass
async def ch3():
    await client.start()
    await mech()
@client.on(events.NewMessage(pattern=r'(?i)(.id|.????)'))
async def Golden1(rrrrrF):
    if rrrrrF.sender_id != GoldID:
        return
    await rrrrrF.delete()
    Gx1 = random.choice(Geeemo)
    Gx2 = await rrrrrF.get_sender()
    Gx3 = await client.get_messages(Gx2,limit=1)
    Gx4 = len(Gx3)
    if Gx4 > 0:
        photo = await client.download_profile_photo(Gx2)
    else:
        photo = None
    if rrrrrF.is_private:
        Gx5 = await client.get_messages(Gx2,limit=1)
    else:
        Gx5 = await client.get_messages(rrrrrF.chat_id,from_user=Gx2,limit=1)
    Gx5 = Gx5.total
    Gx6 = datetime.datetime.now().strftime('%H:%M:%S')
    Gx7 = datetime.datetime.now().strftime('%Y-%m-%d')
    Gx8 = (
        f"**+ ? ID ??.? **? `{Gx2.id}` ?\n"
        f"**+ ? name ??.? **? `{Gx2.first_name}` ? \n"
        f"**+ ? username ??.? **?  `@{Gx2.username}` ?\n"
        f"**+ ? photo ??.? ? {Gx4} ?\n"
        f"**+ ? message ??.? ? {Gx5} ?**\n"
        f"**+ ? account ??.? ? 2018-5-9 ?**\n" 
        f"**+ ? time ??.? ? {Gx6} ?**\n"
        f"**+ ? days ??.? ? {Gx7} ?**\n"
        f"**----- ----- ----- ----**\n**? ? @rrrrrF ? .**"
    )
    try:
        if rrrrrF.is_group:
            chat = await rrrrrF.get_chat()
            if chat.photo:
                if photo:
                    await rrrrrF.respond(Gx8,file=photo)
                else:
                    await rrrrrF.respond(Gx8)
            else:
                await rrrrrF.respond(Gx8)
        else:
            if photo:
                await rrrrrF.respond(Gx8,file=photo)
            else:
                await rrrrrF.respond(Gx8)
    except ForbiddenError as e:
        await rrrrrF.respond(Gx8)
@client.on(events.NewMessage(pattern=r'(?i)(.???)'))
async def Golden2(rrrrrF):
    if rrrrrF.sender_id != GoldID:
        return
    await rrrrrF.delete()
    if rrrrrF.is_reply:
        Gx9 = await rrrrrF.get_reply_message()
        Gx2 = await Gx9.get_sender()
    else:
        args = rrrrrF.message.text.split()
        if len(args) < 2:
            await rrrrrF.respond("? - Error\n? - ??? <username>\n? - ??? <id>\n? - ??? <message>")
            return
        identifier = args[1]
        if identifier.isdigit():
            Gx2 = await client.get_entity(int(identifier))
        else:
            Gx2 = await client.get_entity(identifier)
    Gx3 = await client.get_messages(Gx2,limit=1)
    Gx4 = len(Gx3)
    photo = await client.download_profile_photo(Gx2) if Gx4 > 0 else None
    Gx5 = await client.get_messages(rrrrrF.chat_id,from_user=Gx2,limit=1)
    Gx5 = Gx5.total
    Gx6 = datetime.datetime.now().strftime('%H:%M:%S')
    Gx7 = datetime.datetime.now().strftime('%Y-%m-%d')
    try:
        me = await client.get_me()
        Gx10 = me.date.strftime('%Y-%m-%d') if me.date else ''
    except AttributeError:
        Gx10 = ''
    Gx1 = random.choice(Geeemo)
    Gx8 = (
        f"**+ ? ID ??.? **? `{Gx2.id}` ?\n"
        f"**+ ? name ??.? **? `{Gx2.first_name}` ? \n"
        f"**+ ? username ??.? **?  `@{Gx2.username}` ?\n"
        f"**+ ? photo ??.? ? {Gx4} ?\n"
        f"**+ ? message ??.? ? {Gx5} ?**\n"
        f"**+ ? account ??.? ? {Gx10} ?**\n" 
        f"**+ ? time ??.? ? {Gx6} ?**\n"
        f"**+ ? days ??.? ? {Gx7} ?**\n"
        f"**----- ----- ----- ----**\n**? ? @rrrrrF ? .**"
    )
    try:
        if photo:
            await rrrrrF.respond(Gx8,file=photo)
        else:
            await rrrrrF.respond(Gx8)
    except rpcbaseerrors.ForbiddenError:
        await rrrrrF.respond(Gx8)
Golden_stop = False
@client.on(events.NewMessage(pattern=r'(?i)(.??????? ?????|.insta) (.+)'))
async def Golden5(rrrrrF):
    if rrrrrF.sender_id != GoldID:
        return
    await rrrrrF.delete()
    Gso1 = rrrrrF.pattern_match.group(2)
    Gso2 = {
        'accept': '*/*',
        'accept-encoding': 'gzip,deflate,br',
        'accept-language': 'ar',
        'cookie': 'csrftoken=qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI;mid=Yw2UXgAEAAE4Z0qqjhY5LAruCxGL;ig_did=581A8852-CB4E-4DCE-8112-8DBD48CFA6DF;ig_nrcb=1',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-ua': '"Chromium";v="104"," Not A;Brand";v="99","Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'x-asbd-id': '198387',
        'x-csrftoken': 'qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
    }
    Gso3 = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={Gso1}'
    Gso4 = requests.get(Gso3,headers=Gso2).json()
    Gso5 = Gso4["data"]["user"]["biography"]
    Gso6 = Gso4["data"]["user"]["edge_followed_by"]["count"]
    Gso7 = Gso4["data"]["user"]["edge_follow"]["count"]
    Gso8 = Gso4["data"]["user"]["full_name"]
    Gso9 = Gso4["data"]["user"]["id"]
    Gso10 = Gso4["data"]["user"]["edge_owner_to_timeline_media"]["count"]
    Gso11 = requests.get(f"https://o7aa.pythonanywhere.com/?id={Gso9}").json()["date"]
    Gso12 = Gso4["data"]["user"]["profile_pic_url_hd"]
    Gso13 = f"""?? **Instagram** ???
. ? ? ? ? ? ? ? ? ? ? .
???? ? **Name** - ? {Gso8}
???????????????
???? ? **Username** - ? {Gso1}
???????????????
???? ? **Followers** - ?? {Gso6} ?
???????????????
???? ? **Following** - ? ? {Gso7} ?
???????????????
???? ? **ID** - ? ? {Gso9} ?
???????????????
???? ? **Bio** - ? {Gso5}
???????????????
???? ? **Video** - ? {Gso10}
???????????????
???? ? **Date** - ? {Gso11}
---- ----- ----- ----
**? ? @rrrrrF ? .**
"""
    await rrrrrF.respond(Gso13,file=None)
@client.on(events.NewMessage(pattern=r'(?i).tik (.+)|.??????? ??? (.+)'))
async def Golden6(rrrrrF):
    if rrrrrF.sender_id != GoldID:
        return
    await rrrrrF.delete()
    Gso14 = rrrrrF.pattern_match.group(2)
    Gso15 = {"user-agent": generate_user_agent()}
    Gso16 = requests.get(f"https://www.tiktok.com/@{Gso14}",headers=Gso15).text
    try:
        Gso17 = Gso16.split('"signature":')[1].split(',')[0].replace('"','')
        Gso18 = Gso16.split('"heartCount":')[1].split(',')[0]
        Gso19 = Gso16.split('"videoCount":')[1].split(',')[0]
        Gso20 = Gso16.split('"nickname":')[1].split(',')[0].replace('"','')
        Gso21 = Gso16.split('"followerCount":')[1].split(',')[0]
        Gso22 = Gso16.split('"id":"')[1].split('"')[0]
        Gso23 = Gso16.split('"followingCount":')[1].split(',')[0]
        Gso24 = Gso16.split('"privateAccount":')[1].split(',')[0]
        Gso25 = Gso16.split('"region":"')[1].split('"')[0]
        Gso26 = f"""??**Tiktok** ???
-----------------
???? ? **Name** ? {Gso20}
-----------------
???? ? **Username** ? {Gso14} 
-----------------
???? ? **ID** ? ? {Gso22} ?
-----------------
???? ? **Followers** ? ? {Gso21} ?
-----------------
???? ? **Following** ? ? {Gso23} ?
-----------------
???? ? **Video** ? ? {Gso19} ?
-----------------
???? ? **Like** ? ? {Gso18} ?
-----------------
???? ? **Private** ? ? {Gso24} ?
-----------------
???? ? **Country** ? ? {Gso25} ?
-----------------
???? ? **Date** ? ? None ?
-----------------
???? ? **Bio** ? ? {Gso17} ?
**----- ----- ----- ----**
**? ? @rrrrrF ? .**
"""
        await rrrrrF.respond(Gso26)
    except Exception as e:
        await rrrrrF.respond(f"?? ??  *Error* . ?")
@client.on(events.NewMessage(pattern=r'(?i)roll (.+)|.?????? (.+)'))
async def Golden7(rrrrrF):
    if rrrrrF.sender_id != GoldID:
        return
    await rrrrrF.delete()
    Gso27 = rrrrrF.pattern_match.group(1) or rrrrrF.pattern_match.group(2)
    Gsoem,Gsopas = Gso27.split(':')
    headers = {
        "ETP-Anonymous-ID": str(uuid1()),
        "Request-Type": "SignIn",
        "Accept": "application/json",
        "Accept-Charset": "UTF-8",
        "User-Agent": "Ktor client",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "beta-api.crunchyroll.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip"
    }
    Gso28 = {
        "grant_type": "password",
        "username": Gsoem,
        "password": Gsopas,
        "scope": "offline_access",
        "client_id": "yhukoj8on9w2pcpgjkn_",
        "client_secret": "q7gbr7aXk6HwW5sWfsKvdFwj7B1oK1wF",
        "device_type": "FIRETV",
        "device_id": str(uuid1()),
        "device_name": "kara"
    }
    Gso29 = requests.post("https://beta-api.crunchyroll.com/auth/v1/token",data=Gso28,headers=headers)
    if "refresh_token" in Gso29.text:
        Gso30 = Gso29.json()
        Gso31 = Gso30["access_token"]
        Gso32 = Gso30["refresh_token"]
        Gso33 = Gso30["expires_in"]
        Gso34 = Gso30["token_type"]
        Gso35 = Gso30["scope"]
        Gso36 = Gso30["country"]
        Gso37 = Gso30["account_id"]
        Gso38 = Gso30["profile_id"]
        Gso39 = f"""**??( crunchyroll ) ??? **\n**-----------------**
**???? ?** `{Gsoem}`
-----------------
**???? ?** `{Gsopas}`
-----------------
**???? ?** `{Gso31}`
-----------------
**???? ?** `{Gso32}`
-----------------
**???? ?** `{Gso33}`
-----------------
**???? ?** `{Gso34}`
-----------------
**???? ?** `{Gso35}`
-----------------
**???? ?** `{Gso36}`
-----------------
**???? ?** `{Gso37}`
-----------------
**???? ?** `{Gso38}`
**----- ----- ----- ----**
**? ? @rrrrrF ? .**
"""
        await rrrrrF.respond(Gso39)
    else:
        await rrrrrF.respond("? - Ban")
def Gsoen(username,password):
    Gso41 = "https://www.instagram.com/"
    Gso42 = Gso41 + "accounts/login/ajax/"
    Gso43 = requests.Session()
    Gso43.headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'Referer': Gso41
    }
    Gso44 = Gso43.get(Gso41)
    Gso43.headers.update({'X-CSRFToken': Gso44.cookies['csrftoken']})
    Gso45 = {'username': username,'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:' + password}
    Gso46 = Gso43.post(Gso42,data=Gso45,allow_redirects=True)
    if Gso46.json().get('authenticated'):
        return Gso46.cookies.get('sessionid')
    else:
        return None
@client.on(events.NewMessage(pattern=r'(?i).????? (.+)'))
async def Golden9(rrrrrF):
    if rrrrrF.sender_id != GoldID:
        return
    await rrrrrF.delete()
    data = rrrrrF.pattern_match.group(1)
    try:
        username,password = data.split(':')
    except ValueError:
        await rrrrrF.respond("??- Error")
        return
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0',
        'Accept': '*/*',
        'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
        'X-CSRFToken': 'ouliAoSFAkO4AAl9hrVEPSQXgG1RqpqW',
        'X-Instagram-AJAX': '1012414091',
        'X-IG-App-ID': '936619743392459',
        'X-ASBD-ID': '129477',
        'X-IG-WWW-Claim': 'hmac.AR0B7i9i1Y5DYrc-YtG1No34bwsyj6BSo59bLMf6ONfx0aXu',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://www.instagram.com',
        'Alt-Used': 'www.instagram.com',
        'Connection': 'keep-alive',
        'Referer': 'https://www.instagram.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin'
    }
    Gsoar = str(time.time()).split('.')[0]
    data = {
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{Gsoar}:{password}',
        'optIntoOneTap': 'false',
        'queryParams': '{}',
        'trustedDeviceRecords': '{}',
        'username': username
    }
    response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/',headers=headers,data=data)
    if 'userId' in response.text:
        session_id = Gsoen(username,password)
        if session_id:
            Gso606 = f"**?? ?   ????  ??? ??? ????????? ?????? .**\n\n**?? ?   ????  ???  ????? ??? ???????? ????????? .**"
            await rrrrrF.respond(Gso606)
            await client.send_message('me',f"\n**?? ?   ????  ??? Sessionid** ? `{session_id}`\n\n**----- ----- ----- ----**\n**? ? @rrrrrF ? .**")
        else:
            await rrrrrF.respond("**?? ??  Error . ?**")
    else:
        await rrrrrF.respond("**?? ??  Error . ?**")
@client.on(events.NewMessage(pattern=r'(?i).???? (.+)'))
async def shahid_login(rrrrrF):
    if rrrrrF.sender_id != GoldID:
        return
    await rrrrrF.delete()
    credentials = rrrrrF.pattern_match.group(1)
    email,pas = credentials.split(':')
    G1 = "https://api2.shahid.net/proxy/v2.1/usersservice/userStatus?country=TN"
    G2 = {
        "Host": "api2.shahid.net",
        "UUID": "web",
        "profile": "{\"id\":\"bdcb6780-ab9e-11ed-95fb-0d7f829f8f56\",\"master\":true,\"ageRestriction\":false}",
        "Accept": "application/json",
        "Accept-Language": "fr",
        "Accept-Encoding": "gzip,deflate,br",
        "Content-Type": "application/json",
        "Origin": "https://shahid.mbc.net",
        "language": "FR",
        "profile-key": "{\"isAdult\":true}",
        "User-Agent": "Shahid/7.35.0.3876 CFNetwork/1390 Darwin/22.0.0 (iPhone/11_Pro iOS/16.0.2) Safari/604.1",
        "Referer": "https://shahid.mbc.net/",
        "x-dtc": 'sn="v_4_srv_12_sn_69D2E5A1BCDC498509E5F25BC0AEE23F",pc="12$23475834_233h26vWKJLUUVHCAEFKTHMHGOCRFCMUMPDCMWU-0e0",v="1676423475840IES4681GMCH9B0M75M2NFP4O5683EPA3",app="a28d789e067b813f",r="https://shahid.mbc.net/fr/widgets/login?mobile=true&enableUpgrade=false&deviceId=099523DD-0A4D-4728-93D5-179110BF8CC9&deviceSerial=099523DD-0A4D-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV"'
    }
    G3 = {
        "username": email,
        "captchaToken": "HG45YgHr%^&Qad$56GhrF4G466Dhy@%^J6&jD789qAft^@yT%^*JhjyfwDD"
    }
    res1 = requests.post(G1,headers=G2,json=G3)
    tk = int(time.time())
    G11 = f"https://api2.shahid.net/proxy/v2.1/usersservice/validateLogin?t={tk}&country=TN"
    G22 = {
        "Host": "api2.shahid.net",
        "UUID": "web",
        "profile": "{\"id\":\"bdcb6780-ab9e-11ed-95fb-0d7f829f8f56\",\"master\":true,\"ageRestriction\":false}",
        "Accept": "application/json",
        "Accept-Language": "fr",
        "Accept-Encoding": "gzip,deflate,br",
        "Content-Type": "application/json",
        "Origin": "https://shahid.mbc.net",
        "language": "FR",
        "profile-key": "{\"isAdult\":true}",
        "User-Agent": "Shahid/7.35.0.3876 CFNetwork/1390 Darwin/22.0.0 (iPhone/11_Pro iOS/16.0.2) Safari/604.1",
        "Referer": "https://shahid.mbc.net/",
        "x-dtc": 'sn="v_4_srv_12_sn_69D2E5A1BCDC498509E5F25BC0AEE23F",pc="12$23540062_272h17vWKJLUUVHCAEFKTHMHGOCRFCMUMPDCMWU-0e0",v="1676423475840IES4681GMCH9B0M75M2NFP4O5683EPA3",app="a28d789e067b813f",r="https://shahid.mbc.net/fr/widgets/login-password"'
    }
    G33 = {
        "email": email,
        "rawPassword": pas,
        "subscribeToNewsLetter": False,
        "terms": True,
        "deviceSerial": "",
        "deviceType": "",
        "physicalDeviceType": "",
        "label": "",
        "isNewUser": False,
        "captchaToken": "HG45YgHr%^&Qad$56GhrF4G466Dhy@%^J6&jD789qAft^@yT%^*JhjyfwDD",
        "isEmailVerified": False,
        "isEmailVerifiedZerobounce": False
    }
    res2 = requests.post(G11,headers=G22,json=G33).json()
    if 'success' in res2:
        Gsoer = (f'-?-?-?-?-? -?-?-?-?-? -?-?-?-?-? -?-?-?-?-?\n'
                f'**? ? Email ? {email}**\n'
                f'**? ? Password ? {pas}**\n'
                f'-?-?-?-?-? -?-?-?-?-? -?-?-?-?-? -?-?-?-?-?\n'
                f'**?  ?  firstName** >< {res2.get("user",{}).get("firstName","")}\n'
                f'??  ???  ?? ? ??  ??  ??\n'
                f'**?  ?  lastName** >< {res2.get("user",{}).get("lastName","")}\n'
                f'??  ???  ?? ? ??  ??  ??\n'
                f'**?  ?  userName** >< {res2.get("user",{}).get("userName","")}\n'
                f'??  ???  ?? ? ??  ??  ??\n'
                f'**?  ?  mobileNumber** >< {res2.get("user",{}).get("mobileNumber","")}\n'
                f'??  ???  ?? ? ??  ??  ??\n'
                f'**?  ?  email** >< {res2.get("user",{}).get("email","")}\n'
                f'??  ???  ?? ? ??  ??  ??\n'
                f'**?  ?  language** >< {res2.get("user",{}).get("language","")}\n'
                f'??  ???  ?? ? ??  ??  ??\n'
                f'**?  ?  paymentMethodType** >< {res2.get("userAdditionalValues",{}).get("paymentInfo",{}).get("paymentMethodType","")}\n'
                f'??  ???  ?? ? ??  ??  ??\n'
                f'**?  ?   paymentInfo** >< {res2.get("userAdditionalValues",{}).get("paymentInfo","")}\n'
                f'??  ???  ?? ? ??  ??  ??\n'
                f'**?  ?   currentDate** >< {res2.get("currentDate","")}\n'
                f'-?-?-?-?-? -?-?-?-?-? -?-?-?-?-? -?-?-?-?-?\n'
                f'**?? Golden ?? @rrrrrF ? ?**\n'
                f'**?? channel ?? @N_9_N_6 ? ?**\n'
                f'-?-?-?-?-? -?-?-?-?-? -?-?-?-?-? -?-?-?-?-?')
        await rrrrrF.respond(Gsoer)
    else:
        await rrrrrF.respond(f'**?? ??  Ban . ?  **{email}:{pas}')
async def Gso505(email,password):
    Gso55 = random.randrange(70000000,80000000)
    Gso56 = random.randrange(50000,60000)
    Gso57 = random.randrange(50000,60000)
    Gso58 = random.randrange(4700,5000)
    Gso59 = random.randrange(1500,2000)
    Gso60 = random.randrange(22000,23000)
    Gso61 = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(24))
    Gso62 = {
        'Host': 'b-graph.facebook.com',
        'X-Fb-Connection-Quality': 'EXCELLENT',
        'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; RMX3740 Build/QP1A.190711.020) [FBAN/FB4A;FBAV/4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZVrealme;FBDV/RMX3740;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.0,width=540,height=960};FB_FW/1;FBRV/483172840;]',
        'X-Tigon-Is-Retry': 'false',
        'X-Fb-Friendly-Name': 'authenticate',
        'X-Fb-Connection-Bandwidth': str(Gso55),
        'Zero-Rated': '0',
        'X-Fb-Net-Hni': str(Gso56),
        'X-Fb-Sim-Hni': str(Gso57),
        'X-Fb-Request-Analytics-Tags': '{"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"unknown"}',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Fb-Connection-Type': 'WIFI',
        'X-Fb-Device-Group': str(Gso58),
        'Priority': 'u=3,i',
        'Accept-Encoding': 'gzip,deflate',
        'X-Fb-Http-Engine': 'Liger',
        'X-Fb-Client-Ip': 'true',
        'X-Fb-Server-Cluster': 'true',
        'Content-Length': str(Gso59)
    }
    Gso63 = {
        'adid': str(uuid.uuid4()),
        'format': 'json',
        'device_id': str(uuid.uuid4()),
        'email': email,
        'password': '#PWD_FB4A:0:{}:{}'.format(str(time.time())[:10],password),
        'generate_analytics_claim': '1',
        'community_id': '',
        'linked_guest_account_userid': '',
        'cpl': True,
        'try_num': '1',
        'family_device_id': str(uuid.uuid4()),
        'secure_family_device_id': str(uuid.uuid4()),
        'credentials_type': 'password',
        'account_switcher_uids': [],
        'fb4a_shared_phone_cpl_experiment': 'fb4a_shared_phone_nonce_cpl_at_risk_v3',
        'fb4a_shared_phone_cpl_group': 'enable_v3_at_risk',
        'enroll_misauth': False,
        'generate_session_cookies': '1',
        'error_detail_type': 'button_with_disabled',
        'source': 'login',
        'machine_id': str(Gso61),
        'jazoest': str(Gso60),
        'meta_inf_fbmeta': 'V2_UNTAGGED',
        'advertiser_id': str(uuid.uuid4()),
        'encrypted_msisdn': '',
        'currently_logged_in_userid': '0',
        'locale': 'id_ID',
        'client_country_code': 'ID',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'Fb4aAuthHandler',
        'api_key': '882a8490361da98702bf97a021ddc14d',
        'sig': str(uuid.uuid4()),
        'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    }
    Gso64 = requests.post('https://b-graph.facebook.com/auth/login',data=Gso63,headers=Gso62)
    Gso65 = Gso64.json()
    if 'session_key' in Gso65 and 'access_token' in Gso65:
        Gso66 = Gso65['access_token']
        Gso67 = ''.join(['{}={};'.format(i['name'],i['value']) for i in Gso65.get('session_cookies',[])])
        return {'token': Gso66,'cookies': Gso67}
    else:
        return {'token': 'Ban'}
@client.on(events.NewMessage(pattern='.??? (.+)'))
async def Golden12(rrrrrF):
    if rrrrrF.sender_id != GoldID:
        return
    await rrrrrF.delete()
    data = rrrrrF.pattern_match.group(1)
    email,password = data.split(':')
    Gso404 = await Gso505(email,password)
    if Gso404['token'] != 'Ban':
        Gso606 = """**?? ?   ????  ??? ??? ????????? ?????? .**\n\n**?? ?   ????  ???  ????? ??? ???????? ????????? .**"""
        Goldfas = f"\n**?? ?   ????  ??? Token** ? `{Gso404['token']}`\n\n**?? ?   ????  ??? Cookies** ? `{Gso404['cookies']}`\n**----- ----- ----- ----**\n**? ? @rrrrrF ? .**"
    else:
        Gso606 = "**?? ??  Error . ?  **"
        Goldfas = Gso606
    await rrrrrF.reply(Gso606)
    await client.send_message('me',Goldfas)
@client.on(events.NewMessage(pattern='.???? (.+)'))
async def Golden13(rrrrrF):
    if rrrrrF.sender_id != GoldID:
        return
    await rrrrrF.delete()
    Gso72 = rrrrrF.pattern_match.group(1)
    Gso73 = requests.get(f'https://api.telegram.org/bot{Gso72}/getMe')
    if '"ok":true' in Gso73.text:
        Gso74 = Gso73.json()
        Gso75 = Gso74['result']
        Gso76 = (
            f"**?  ??  . Done ?**\n? ? ? ? ? ? ? ? ? ? ? ? ? ?\n"
            f"**?  ??  . ** ? `{Gso75['id']}` ?"
            f"**-_-_-_-_-_-_-_-_-_-_-_-_-_-**\n"
            f"**?  ??  . **? `{Gso75['first_name']}` ?\n"
            f"**-_-_-_-_-_-_-_-_-_-_-_-_-_-**\n"
            f"**?  ??  . **? `{Gso75['username']}` ?"
            f"\n**----- ----- ----- ----**\n**? ? @rrrrrF ? .**"
        )
    else:
        Gso76 = f"**?? ??  Error . ?**\n**----- ----- ----- ----**\n**? ? @rrrrrF ? .**"
    await rrrrrF.respond(Gso76)
@client.on(events.NewMessage(pattern='.??????? (.+)'))
async def handle_spotify_command(rrrrrF):
    if rrrrrF.sender_id != GoldID:
        return
    await rrrrrF.delete()
    details = rrrrrF.pattern_match.group(1)
    email,password = details.split(':')
    def Check(email,pas):
        Gxxx1 = ""
        Gxxx2 = ""
        Gxxx3 = ""
        Gxxx4 = ""
        Gx5 = ""
        Gxx = "https://accounts.spotify.com/en/login"
        Gxxx5 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/80.0.3987.149 Safari/537.36",
            "Pragma": "no-cache",
            "Accept": "*/*"}
        Dx1 = requests.get(Gxx,headers=Gxxx5)
        Gxxx1 = re.search(r'__Host-device_id=(.*?);',Dx1.headers['Set-Cookie']).group(1)
        Gxxx2 = re.search(r'sp_sso_csrf_token=(.*?);',Dx1.headers['Set-Cookie']).group(1)
        Gxxx3 = re.search(r'__Host-sp_csrf_sid=(.*?);',Dx1.headers['Set-Cookie']).group(1)
        Gxxx4 = re.search(r'__Secure-TPASESSION=(.*?);',Dx1.headers['Set-Cookie']).group(1)
        Gxxx5 = re.search(r'"flowCtx":"(.*?)"',Dx1.text).group(1)
        Dxxx2 = "https://accounts.spotify.com/login/password"
        Dxxx3 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/109.0.0.0 Safari/537.36",
            "Pragma": "no-cache",
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": f"__Host-device_id={Gxxx1}; __Secure-TPASESSION={Gxxx4}; sp_sso_csrf_token={Gxxx2}; sp_tr=false; __Host-sp_csrf_sid={Gxxx3}; remember={email}",
            "Origin": "https://accounts.spotify.com",
            "Referer": "https://accounts.spotify.com/en/login",
            "X-CSRF-Token": Gxxx2
        }
        Dxxx4 = {
            "username": email,
            "password": pas,
            "remember": "false",
            "continue": "https://accounts-gue1.spotify.com/floss/complete/05-243deba9-011d-4ae3-a9e2-d26187993d5e;2;044e1130-1091-4b3c-814a-a8cdaa190005?state=3-AQAl2UNaXwof8y_Nd7nnm81IwmyL4cUlRAa3N2ttiIva-Vd7uduZS0rMUOsHgJ1I94XtDwB7QBb2eKzETGoCIwo27npbKCh5KBAiq24weYkbVNMUSbb3oAM_X0zllL4LQyJgyIKaOLj3KXM6gr4egAsvHbnUPjc&flow_ctx=f80afa00-f44-4765-za435-7569aec3yui7845:1707078938",
            "listenerAppExperiment": "true",
            "flowCtx": Gxxx5
        }
        Dxxx2 = requests.post(Dxxx2,headers=Dxxx3,data=Dxxx4)
        if '"result":"ok"' in Dxxx2.text:
            return (f'—————————————————————\n'
                    f'- Email - {email}\n'
                    f'- Password - {pas}\n'
                    f'—————————————————————\n'
                    f'Golden - @rrrrrF\n'
                    f'channel - @N_9_N_6\n'
                    f'—————————————————————')
        else:
            return "Error"
    result = Check(email,password)
    if result == "Error":
        Dxxx99 = "**?? ??  Error . ?  **"
    else:
        Dxxx99 = f"**? - Done**\n\n{result}"
    await rrrrrF.respond(Dxxx99)
if __name__ == '__main__':
    client.loop.run_until_complete(ch3())
    client.run_until_disconnected()
