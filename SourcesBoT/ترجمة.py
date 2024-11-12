from telebot import *;import requests,telebot,os
G1 = '' # - [> توكـن <]
G2 = 5846480832 # - [> ايـدي <]
F = {}
G = telebot.TeleBot(G1)
if not os.path.exists('id.txt'):
    with open('id.txt','w') as F:
        pass
G3 = {'en': '🇬🇧','es': '🇪🇸','ar': '🇸🇦','fr': '🇫🇷','de': '🇩🇪','zh': '🇨🇳','ja': '🇯🇵','ru': '🇷🇺','it': '🇮🇹','pt': '🇧🇷','hi': '🇮🇳','ko': '🇰🇷','tr': '🇹🇷','nl': '🇳🇱','sv': '🇸🇪','da': '🇩🇰','fi': '🇫🇮','no': '🇳🇴','pl': '🇵🇱','cs': '🇨🇿','ro': '🇷🇴','hu': '🇭🇺','th': '🇹🇭','vi': '🇻🇳','el': '🇬🇷','bg': '🇧🇬','sk': '🇸🇰','sl': '🇸🇮','hr': '🇭🇷','lv': '🇱🇻','lt': '🇱🇹','et': '🇪🇪','cat': '🇨🇦','ga': '🇮🇪','is': '🇮🇸','mt': '🇲🇹','ms': '🇲🇾','sw': '🇰🇪','xh': '🇿🇦','zu': '🇿🇦','tl': '🇵🇭','jw': '🇮🇩','ne': '🇳🇵','pa': '🇮🇳','bn': '🇧🇩','si': '🇱🇰','am': '🇪🇹','yi': '🇮🇱','ku': '🇹🇷','cy': '🇬🇧','eo': '🇪🇸','la': '🇻🇦','be': '🇧🇾','uk': '🇺🇦','mn': '🇲🇳','km': '🇰🇭','my': '🇲🇲','sn': '🇿🇼','so': '🇸🇴','sd': '🇵🇰','ps': '🇦🇫','tk': '🇹🇰','qu': '🇵🇪','ay': '🇧🇴','wo': '🇸🇳','ha': '🇳🇬','rw': '🇷🇼','tg': '🇹🇯','ne': '🇳🇵','tl': '🇵🇭'}
def X1(S1):
    with open('id.txt','a') as F:
        F.write(f'{S1}\n')
def X2(S1):
    with open('id.txt','r') as F:
        G4 = F.read().splitlines()
    return str(S1) in G4
@G.message_handler(commands=['start'])
def X3(S2):
    G5 = S2.chat.id
    if not X2(G5):
        X1(G5)
        X6(S2)
    G.send_message(S2.chat.id,'''<b>🌨 ¦ اهـلا بك عزيزي انا بـوت تـرجـمة متـطور .</b>

<b>⚡️ ¦ ارسـل الـرسـالة الان.</b>''',parse_mode='HTML')
@G.message_handler(func=lambda S2: True)
def X4(S2):
    F[S2.chat.id] = S2.text
    F1 = types.InlineKeyboardMarkup(row_width=5)
    F2 = [types.InlineKeyboardButton(text=name,callback_data=code) for code,name in G3.items()]
    F1.add(*F2)
    G.send_message(S2.chat.id,'''<b>⚠️ ¦ اخــتار اللـغة للـترجـمة .</b>''',reply_markup=F1,parse_mode='HTML')
@G.callback_query_handler(func=lambda S3: True)
def X5(S3):
    G5 = S3.message.chat.id
    K1 = F.get(G5,'''<b>📛 ¦ لايـوجد نـص لـكي اتــرجـمة .</b>''')
    K2 = S3.data
    K3 = X7(K1,K2)
    K4 = (f'<b>👤  ¦  [ <code>{K1}</code> ]</b>\n'
      f'<b>━━━━━━━━━━━━━━━━━</b>\n'
      f'<b>♻️  ¦  [ <code>{K3}</code> ]</b>')
    G.edit_message_text(K4,chat_id=G5,message_id=S3.message.message_id,parse_mode='HTML')
def X6(S2):
    G.send_message(G2,f'شخـص جـديد . - ✅\nName - {S2.from_user.first_name}\nUsername - @{S2.from_user.username}\nID - {S2.chat.id}')
def X7(V1,V2):
    H1 = {'Host': 'translate.googleapis.com','Connection': 'Keep-Alive','User-Agent': 'Apache-HttpClient/UNAVAILABLE (java 1.4)'}
    H2 = {'client': 'gtx','sl': 'auto','tl': V2,'dt': 't','ie': 'UTF-8','oe': 'UTF-8','q': V1}
    H3 = requests.get('https://translate.googleapis.com/translate_a/single',params=H2,headers=H1)
    return H3.json()[0][0][0]
G.polling()
