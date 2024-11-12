import requests
import os
import random
import time
import datetime
m1_Golden = time.localtime()
m2_Golden = time.strftime('''%d/%m/%Y''')
now = datetime.datetime.now()
e_Golden = now.strftime("%I:%M:%S")

def X_Code():
    return ''.join(random.choices('0123456789', k=7))
Code = X_Code()
t_Golden=input('  \x1b[38;5;117m[\x1b[1;32m•\x1b[38;5;117m]  \x1b[38;5;180m- Enter Token Telegram   \x1b[38;5;117m')
print('\x1b[2;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ')
i_Golden=input('  \x1b[38;5;117m[\x1b[1;32m+\x1b[38;5;117m]- Enter id Telegram  \x1b[38;5;117m')
h_Golden = (f"""
[ 🤖 ] تحقق .
━━━━━━━━━━━━━━━━━━━━━━━━
[ ⚠️ ] الـكود   » {Code}

[ 🕗 ] الوقت    » {e_Golden}

[ 📆 ] التاريخ   » {m2_Golden}

[ 👨🏻‍💻 ] المـبرمج   » @rrrrrf
━━━━━━━━━━━━━━━━━━━━━━━━""")
requests.post(f"https://api.telegram.org/bot{t_Golden}/sendMessage?chat_id={i_Golden}&text="+str(h_Golden))
print('\x1b[2;33m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ')
print(f' يجب ادخال الكود الذي ارسلنا لك ع التليجرام للتاكد انك ليس روبوت')
print('\x1b[2;33m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ')
c_Golden = input('\x1b[1;32m Enter Code  \x1b[1;31m=\x1b[1;33m=\x1b[1;34m=\x1b[1;35m> \x1b[1;32m')
print('\x1b[2;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
if c_Golden == f'{Code}':
    print('\n\x1b[1;35m=\x1b[1;31m=\x1b[1;34m>\x1b[1;32m جـاري الـتحقق. . . .')
    time.sleep(7)
    print('\x1b[1;35m=\x1b[1;31m=\x1b[1;34m>\x1b[1;32m  اهـلا بــك')
    time.sleep(4)
    print('\x1b[1;34m=\x1b[1;33m=\x1b[1;31m>\x1b[1;32m ✅')
    g_Golden = ('[ ✅ ] تـم تـسجـيل بــنجاح  .')
    requests.post(f"https://api.telegram.org/bot{t_Golden}/sendMessage?chat_id={i_Golden}&text="+str(g_Golden))
else:
    print('\x1b[1;34m=\x1b[1;33m=\x1b[1;31m>\x1b[1;32m اهـلا بــك')
    time.sleep(4)
    print('\x1b[1;35m=\x1b[1;31m=\x1b[1;34m>\x1b[1;32m ❌')
    time.sleep(4)
    print('\x1b[1;34m=\x1b[1;33m=\x1b[1;31m>\x1b[1;31m انت روبوت لا يسمح لك ب الدخول . ؟')
    exit()
os.system('clear')