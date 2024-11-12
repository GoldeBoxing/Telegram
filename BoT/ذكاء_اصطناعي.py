import requests,json,telebot
T = 'token'  # - [> توكـن <]
KK = '' # - [> Key chatGPT <]
B = telebot.TeleBot(T)
he = {'Host': 'api.openai.com','Accept': 'text/event-stream,application/json','Cache-Control': 'no-cache','Authorization': f'Bearer {KK}','Accept-Charset': 'UTF-8','User-Agent': 'Ktor client','Content-Type': 'application/json'}
@B.message_handler(commands=['start'])
def C1(mess):
    B.reply_to(mess,'''<b>🤖 ¦ اهـلا بك عزيزي انا بـوت الـذكاء الاصـطناعي .</b>

<b>⚡️ ¦ هـل يمـكننـي مسـاعدتـك .</b>''',parse_mode='HTML')
@B.message_handler(func=lambda msg: True)
def C2(msg):
    m = msg.text
    tyr = B.send_message(msg.chat.id,"✨")
    dat = {'model': 'gpt-4o-mini','messages': [{'role': 'system','content': 'You are a helpful assistant that responds in the language specified by the user.'},{'role': 'user','content': m}],'n': 1,'stream': True}
    r = requests.post('https://api.openai.com/v1/chat/completions',headers=he,json=dat)
    rs = ""
    for xx in r.iter_lines():
        if xx and xx.decode('utf-8').startswith('data: '):
            try:
                js = json.loads(xx.decode('utf-8')[6:])
                if 'choices' in js and len(js['choices']) > 0:
                    rs += js['choices'][0]['delta'].get('content','')
            except json.JSONDecodeError:
                continue
    if '```' in rs:
        B.edit_message_text(rs,chat_id=msg.chat.id,message_id=tyr.message_id,parse_mode='Markdown')
    else:
        B.edit_message_text(f"<b>{rs}</b>",chat_id=msg.chat.id,message_id=tyr.message_id,parse_mode='HTML')
B.polling()