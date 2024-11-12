import requests,os,time;from fake_useragent import *;from telethon import *
G2 = '\x1b[38;5;196m' 
G27 = '\x1b[38;5;121m' 
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
m1 = '\x1b[38;5;196m'
a36 = '\x1b[38;5;228m'
G20 = '\x1b[1;92m\x1b[38;5;212m'
G16 = '\x1b[1;92m\x1b[38;5;208m'
a6 = '\x1b[38;5;5m'
GT1 = '\x1b[1;92m\x1b[38;5;46m'
GT2 = '\x1b[1;92m\x1b[38;5;50m'
GT3 = '\x1b[38;5;196m'
GT4 = '\x1b[1;92m\x1b[38;5;210m'
GT5 = '\x1b[38;5;90m'
GT6 = '\x1b[38;5;93m'
GT9 = '\x1b[38;5;123m'
Fok = 0
Ftm = 0
Fac = 0
Bok = 0
Btm = 0
Bac = 0
Er = 0
token = ''  # - [ > تـوكنك < ]
ID = 5846480832  # - [ > ايديك < ]
XG1 = ''  # - [ > ايبي ايدي < ]
XG2 = ''  # - [ > ايبي هاش < ]
X = TelegramClient('X-Golden',XG1,XG2)
def XxX():
    global Fok,Ftm,Fac,Bok,Btm,Bac,Er
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'{GT2}[ {GT1}By{GT2}] {GT3}- {GT4}GoLdEn {GT3}- {GT9}@rrrrrF {GT5}.\n{m1}----------------------{G20}')
    XG3 = input(f"1 - [ FILE ]\n2 - [ USER ]\n{a36}[%]- Enter > ")
    if XG3 == '1':
        XG4 = input("- Enter File Name : > ")
        with open(XG4,'r',encoding='utf-8') as f:
            XG5 = f.readlines()
    elif XG3 == '2':
        XAC = input("- Enter Username : > ")
        XG5 = [XAC]
    else:
        return
    if XG3 == '1':
        while True:
            for XUS in XG5:
                XUS = XUS.strip()
                if not XUS:
                    continue
                XG6 = UserAgent()
                XG7 = f"https://fragment.com/username/{XUS}"
                XG8 = {"User-Agent": XG6.random,"Pragma": "no-cache","Accept": "*/*"}
                XG9 = requests.post(XG7,headers=XG8)
                if "Minimum Bid" in XG9.text or 'Decreases by' in XG9.text:
                    Bok += 1
                    XG10 = 'Tele-[❌-Fragment].txt'
                    with open(XG10,'a',encoding='utf-8') as f:
                        f.write(XUS + '\n')
                else:
                    Fok += 1
                    XG10 = 'Tele-[✅-Fragment].txt'
                    with open(XG10,'a',encoding='utf-8') as f:
                        f.write(XUS + '\n')
                    XG7 = f"https://t.me/{XUS}"
                    XG9 = requests.post(XG7,headers=XG8)
                    if "a new era of messaging" in XG9.text or "If you have <strong>Telegram</strong>,you can contact <a" in XG9.text:
                        Ftm += 1
                        XG10 = 'Tele-[✅-t.me].txt'
                        with open(XG10,'a',encoding='utf-8') as f:
                            f.write(XUS + '\n')
                        try:
                            XG11 = X(functions.account.CheckUsernameRequest(username=XUS))
                            if XG11:
                                Fac += 1
                                Us = (f'''🌈 - {XUS} .
—————————————————————
🐉 - @rrrrrF .''')
                                requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={Us}')
                                XG10 = 'Tele-[✅-Telegram].txt'
                                with open(XG10,'a',encoding='utf-8') as f:
                                    f.write(XUS + '\n')
                                print(f"{G}[+] Hit - {XUS}")
                        except errors.UsernameInvalidError:
                           Bac += 1
                        except errors.rpcbaseerrors.BadRequestError as e:
                            Er += 1
                    else:
                        Btm += 1
                        XG10 = 'Tele-[❌-t.me].txt'
                        with open(XG10,'a',encoding='utf-8') as f:
                            f.write(XUS + '\n')
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'ـ' * 40)
                print(f'''{G}[√] Fragment : {B}{Fok}
{G}[√] t.me : {B}{Ftm}
{G}[√] Hit : {B}{Fac}
{G16}----------------------
{m1}[X] Fragment : {B}{Bok}
{m1}[X] t.me : {B}{Btm}
{m1}[X] Bad : {B}{Bac}
{G16}----------------------
{G27}[X] Error : {B}{Er}''')
                print(f'{B}ـ'*40)
                print(f'{G2}Golden {G20}- {G27}@rrrrrF')
                print(f'{B}ـ'*40)
                print(f'{S}[+] {B}{XUS}')
                print(f'{B}ـ'*40)
    elif XG3 == '2':
        XUS = XAC.strip()
        while True:
            XG6 = UserAgent()
            XG7 = f"https://fragment.com/username/{XUS}"
            XG8 = {"User-Agent": XG6.random,"Pragma": "no-cache","Accept": "*/*"}
            XG9 = requests.post(XG7,headers=XG8)
            if "Minimum Bid" in XG9.text or 'Decreases by' in XG9.text:
                Bok += 1
                XG10 = 'Tele-[❌-Fragment].txt'
                with open(XG10,'a',encoding='utf-8') as f:
                    f.write(XUS + '\n')
            else:
                Fok += 1
                XG10 = 'Tele-[✅-Fragment].txt'
                with open(XG10,'a',encoding='utf-8') as f:
                    f.write(XUS + '\n')
                XG7 = f"https://t.me/{XUS}"
                XG9 = requests.post(XG7,headers=XG8)
                if "a new era of messaging" in XG9.text or "If you have <strong>Telegram</strong>,you can contact <a" in XG9.text:
                    Ftm += 1
                    XG10 = 'Tele-[✅-t.me].txt'
                    with open(XG10,'a',encoding='utf-8') as f:
                        f.write(XUS + '\n')
                    try:
                        XG11 = X(functions.account.CheckUsernameRequest(username=XUS))
                        if XG11:
                            Fac += 1
                            Us = (f'''🌈 - {XUS} .
—————————————————————
🐉 - @rrrrrF .''')
                            requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={Us}')
                            XG10 = 'Tele-[✅-Telegram].txt'
                            with open(XG10,'a',encoding='utf-8') as f:
                                f.write(XUS + '\n')
                            print(f"{G}[+] Hit - {XUS}")
                            break
                    except errors.UsernameInvalidError:
                       Bac += 1
                       XG10 = 'Tele-[❌-Telegram].txt'
                    except errors.rpcbaseerrors.BadRequestError as e:
                        Er += 1
                else:
                    Btm += 1
                    XG10 = 'BadTelegram.txt'
                    with open(XG10,'a',encoding='utf-8') as f:
                        f.write(XUS + '\n')
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'ـ' * 40)
            print(f'''{G}[√] Fragment : {B}{Fok}
{G}[√] t.me : {B}{Ftm}
{G}[√] Hit : {B}{Fac}
{G16}----------------------
{m1}[X] Fragment : {B}{Bok}
{m1}[X] t.me : {B}{Btm}
{m1}[X] Bad : {B}{Bac}
{G16}----------------------
{G27}[X] Error : {B}{Er}''')
            print(f'{B}ـ'*40)
            print(f'{G2}Golden {G20}- {G27}@rrrrrF')
            print(f'{B}ـ'*40)
            print(f'{S}[+] {B}{XUS}')
            print(f'{B}ـ'*40)
X.start();XxX()