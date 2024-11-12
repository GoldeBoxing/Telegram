import os
import requests
from telethon import TelegramClient, sync
from telethon import functions, types
from telethon import errors
import configparser
import time
import datetime
import random
G2 = ('\x1b[1;32m')
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
G27 = '\x1b[38;5;86m'
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
time1 = time.localtime()
time2 = time.strftime('%d/%m/%Y')
now = datetime.datetime.now()
time3 = now.strftime("%I:%M:%S")
config = configparser.ConfigParser()
Glogo = (f"""{G20}
    ████████ ███████ ██      ███████  ██████  ██████   █████  ███    ███
       ██    ██      ██      ██      ██       ██   ██ ██   ██ ████  ████
       ██    █████   ██      █████   ██   ███ ██████  ███████ ██ ████ ██
       ██    ██      ██      ██      ██    ██ ██   ██ ██   ██ ██  ██  ██
       ██    ███████ ███████ ███████  ██████  ██   ██ ██   ██ ██      ██
		                       
		        ██    ██ ███████ ███████ ██████                     
		        ██    ██ ██      ██      ██   ██                    
		        ██    ██ ███████ █████   ██████                    
		        ██    ██      ██ ██      ██   ██                    
		         ██████  ███████ ███████ ██   ██                        
		                               
                  - Username Checker -
                - by  Golden | @rrrrrf -
    """)
if not os.path.exists('session.session'):
    Goldid = input(f'{G24} - Enter ID Telegram ==>    ')
    print(f"{G12}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    Goldtok = input(f'{G26} - Enter TOKEN Telegram ==>    ')
    print(f"{G12}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    api_id = input(f'{G14} - Enter your API ID ==>    ')
    print(f"{G12}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    api_hash = input(f'{G19} - Enter your API Hash ==>    ')
    print(f"{G12}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    config['default'] = {'api_id': api_id, 'api_hash': api_hash}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
else:
    Goldid = input(f'{G24} - Enter ID Telegram ==>    ')
    print(f"{G12}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    Goldtok = input(f'{G26} - Enter TOKEN Telegram ==>    ')
    print(f"{G12}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    config.read('config.ini')
    api_id = config.get('default', 'api_id')
    api_hash = config.get('default', 'api_hash')
client = TelegramClient('see', api_id, api_hash)
client.start()
def Golden1(account):
    try:
        Gx1 = client(functions.account.CheckUsernameRequest(username=account))
        if Gx1:
            print(f"✅ {G6}- {G21}{account}")
            Goldentele = f"""
            [ ✅ ] account ready
            ═════════════════➢
            [✅] Users   » {account}
            [✅] Time    » {time3}
            [✅] Date   » {time2}
            ═════════════════➢
            [🤴🏻]  => @rrrrrf"""
            requests.post(f"https://api.telegram.org/bot{Goldtok}/sendMessage?chat_id={Goldid}&text="+str(Goldentele))
            with open('AVAILABLE.txt', 'a') as file:
                file.write(f"{account}\n")
        else:
            print(f"❌ {G6}- {G2}{account}")
    except errors.FloodWaitError as fW:
        pass
    except errors.UsernameInvalidError:
        print("🚫 - 🚫")
    except errors.rpcbaseerrors.BadRequestError as bR:
        print(f"⚠️ {G6}-{G3}", bR.message)
def Golden2():
    os.system('rm -rf list.txt')
    a5 = '\x1b[38;5;197m'
    a3 = '\x1b[38;5;46m'
    a4 = '\x1b[38;5;82m'
    a6 = '\x1b[38;5;204m'
    print(f"""
{a5}[{a3}1{a5}]{a4} ثلاثي | #_#_#  
{a5}[{a3}2{a5}]{a4} شبه رباعي مميز | #__#_
{a5}[{a3}3{a5}]{a4} رباعي  | #_#_#_#
{a5}[{a3}4{a5}]{a4} خماسي | #####
{a5}[{a3}5{a5}]{a4} سداسي | ######
{a5}[{a3}6{a5}]{a4} سداسي حرفين | ######
{a5}[{a3}7{a5}]{a4} سباعي  | #######
{a5}[{a3}8{a5}]{a4} سباعي حرفين | #######
    """)
def Golden3(C):
    R = "".join(random.choices("qwertyuiopasdfghjklzxcvbnm"))
    R2 = "".join(random.choices("_"))
    R3 = "".join(random.choices("qwertyuiopasdfghjklzxcvbnm0123456789"))
    R5 = "".join(random.choices("qwertyuiopasdfghjklzxcvbnm0123456789"))
    R6 = "".join(random.choices("qwertyuiopasdfghjklzxcvbnm0123456789"))
    R7 = "".join(random.choices("qwertyuiopasdfghjklzxcvbnm0123456789"))
    R8 = "".join(random.choices("0123456789"))
    R9 = "".join(random.choices("0123456789"))
    if C == "1":
        List_X = R+R2+R3+R2+R5
    elif C == "2":
        List_X = R3+R2+R8+R2+R3+R2+R9
    elif C == "3":
        List_X = R+R2+R7+R2+R3+R2+R5
    elif C == "4":
        List_X = R3+R6+R3+R3+R3
    elif C == "5":
        List_X = R3+R6+R3+R3+R3+R3
    elif C == "6":
        List_X = R3+R6+R3+R3+R3+R6
    elif C == "7":
        List_X = R3+R6+R3+R3+R3+R3+R3
    elif C == "8":
        List_X = R3+R3+R6+R3+R3+R3+R6
    return List_X
def Golden4():
    Golden2()
    Gx2 = input('Enter = > ')
    Gx3 = 1000
    if Gx2 not in ["1","2","3","4","5","6","7","8"]:
        print('Error .')
        return
    for _ in range(Gx3):
        Gx4 = Golden3(Gx2)
        with open('list.txt', 'a') as file:
            file.write(f'{Gx4}\n')
    os.system('clear')
    print(Glogo)
    Golden5()
def Golden5():
    Gx5 = config.get('default', 'delay', fallback='3')
    with open('list.txt', 'r', encoding='utf-8-sig') as file:
        Gx6 = file.read().split('\n')
    for name in Gx6:
        Golden1(name)
        time.sleep(int(Gx5))
    print('All done')
def Dev_Golden():
    print(Glogo)
    Golden4()
Dev_Golden()