import requests;from user_agent import *
F = 07725644610 # - [ > الرقم < ]
H = {'accept': 'application/json,text/plain,*/*','accept-language': 'en-US,en;q=0.9','content-type': 'application/json;charset=UTF-8','origin': 'https://ht.iq','priority': 'u=1,i','referer': 'https://ht.iq/','sec-ch-ua': '"Not)A;Brand";v="99","Opera GX";v="113","Chromium";v="127"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': generate_user_agent()}
J = {'phone': F}
R = requests.post('https://api.ht.iq/api/form/send_otp',headers=H,json=J).text
if '"status":"OTP sent' in R:
    print('❇️ - Good .')
else:
    print('📛 - Bad .')
