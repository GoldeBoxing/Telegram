import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import telebot
import time
import json
import os
from telebot import types
Goldservr = 'smtp-mail.outlook.com'
Goldport = 587
Goldservr2 = 'smtp.gmail.com'
Goldport2 = 587
Goldtok = ''# - توكن بوتك
gold_iq = 'rrrrrF'# - يوزر المبرمج بدون @
gold_zi = 'I_S_4'# - يوزر المالك بدون @
gold_ph = 'https://t.me/e2exxx/5148' # - اذا تريد تغير صورة الاوامر فقط خلي رابط صورة بدال هاذ الرابط
bot = telebot.TeleBot(Goldtok)
def GoldenStart(Golden1,Golden2,Golden3,Golden4,Golden5):
    server = None
    try:
        msg = MIMEMultipart()
        msg['From'] = Golden4
        msg['To'] = Golden1
        msg['Subject'] = Golden2
        msg.attach(MIMEText(Golden3,'plain'))
        if '@outlook' in Golden4 or '@hotmail' in Golden4:
            server = smtplib.SMTP(Goldservr,Goldport)
        elif '@gmail' in Golden4:
            server = smtplib.SMTP(Goldservr2,Goldport2)
        if server:
            server.starttls()
            server.login(Golden4,Golden5)
            server.sendmail(Golden4,Golden1,msg.as_string())
            server.quit()
            return True
        else:
            return False
    except Exception as e:
        if server:
            server.quit()
        pass
        return False
def GoldenX2(domain=None):
    try:
        with open('Gold-email_pas.json','r') as f:
            accounts = json.load(f)
            if domain:
                filtered_accounts = {email: password for email,password in accounts.items() if email.endswith(domain)}
                return filtered_accounts
            return accounts
    except FileNotFoundError:
        return {}
def GoldenX3(accounts):
    try:
        with open('Gold-email_pas.json','w') as f:
            json.dump(accounts,f,ensure_ascii=False,indent=4)
        pass
    except Exception as e:
        pass
def GoldenX4(Fib):
    try:
        with open(Fib,'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return None
def GoldenX5(Fib,data):
    try:
        with open(Fib,'w') as f:
            f.write(data)
        pass
    except Exception as e:
        pass
def GoldenX6(message):
    user_info = f"""- ID : {message.from_user.id}
- Name : {message.from_user.first_name} {message.from_user.last_name}
- Username : @{message.from_user.username}
- Time : {time.strftime('%Y-%m-%d %H:%M:%S')}
    """
    bot.send_message(message.chat.id,user_info)
@bot.message_handler(commands=['start'])
def start(message):
    GoldenZ1 = f'{gold_ph}'
    GoldenZ3 = types.InlineKeyboardMarkup()
    GoldenZ4 = types.InlineKeyboardButton(text='⌁ بدء الإرسال ⌁',callback_data='phonk_1')
    GoldenZ5 = types.InlineKeyboardButton(text='⌁ اضافة حساب ⌁',callback_data='phonk_2')
    GoldenZ6 = types.InlineKeyboardButton(text='⌁ تعيين الرسالة ⌁',callback_data='phonk_3')
    GoldenZ7 = types.InlineKeyboardButton(text='⌁ تعيين الموضوع ⌁',callback_data='phonk_4')
    GoldenZ8 = types.InlineKeyboardButton(text='⌁ تعيين السرعة ⌁',callback_data='phonk_5')
    GoldenZ9 = types.InlineKeyboardButton(text='⌁ عرض معلوماتك ⌁',callback_data='phonk_6')
    GoldenZ10 = types.InlineKeyboardButton(text='⌁ مسح الايميلات ⌁',callback_data='phonk_7')
    GoldenZ11 = types.InlineKeyboardButton(text='⌁ ايميل الدعم ⌁',callback_data='phonk_8')
    GoldenZ12 = types.InlineKeyboardButton(text='⌁ عدد الرسائل ⌁',callback_data='phonk_9')
    GoldenZ14 = types.InlineKeyboardButton(text='⌁ المبرمج ⌁',url=f'https://t.me/{gold_iq}')
    GoldenZ15 = types.InlineKeyboardButton(text='⌁ المالك ⌁',url=f'https://t.me/{gold_zi}')
    GoldenZ3.row(GoldenZ4,GoldenZ5)
    GoldenZ3.row(GoldenZ6,GoldenZ7,GoldenZ8)
    GoldenZ3.row(GoldenZ9,GoldenZ10,GoldenZ11)
    GoldenZ3.row(GoldenZ12)
    GoldenZ3.row(GoldenZ14,GoldenZ15)
    bot.send_photo(message.chat.id,photo=GoldenZ1,reply_markup=GoldenZ3)
@bot.callback_query_handler(func=lambda call: True)
def GoldenGo(call):
    if call.data == 'phonk_1':
        GoldenT1 = GoldenX4('golden1.json')
        GoldenT2 = GoldenX4('golden2.json')
        GoldenT3 = GoldenX4('golden3.json')
        GoldenT4 = GoldenX4('golden4.json')
        GoldenT5 = int(GoldenX4('golden5.json')) if GoldenX4('golden5.json') else None
        if GoldenT1 and GoldenT2 and GoldenT3 and GoldenT4 and GoldenT5:
            accounts = GoldenX2()
            count = 0
            for email,password in accounts.items():
                if count >= GoldenT5:
                    break
                if GoldenStart(email,GoldenT2,GoldenT1,GoldenT4,password):
                    bot.send_message(call.message.chat.id,f'🌐 - تم الارســال [{email}]')
                    count += 1
                    time.sleep(int(GoldenT3))
                else:
                    bot.send_message(call.message.chat.id,f'🌐 - خطـا الارســال [{email}]')
        else:
            bot.send_message(call.message.chat.id,"⚠️ - اتـاكد مـن جـميع المـعلومات كامـلة")
    elif call.data == 'phonk_2':
        bot.send_message(call.message.chat.id,"ارســل الايميل مـع الــباسورد - email:password -\n اذا عنـدك حـسابات هـواي ارسـل \nemail:password\nemail:password\nemail:password")
        bot.answer_callback_query(call.id)
        bot.register_next_step_handler(call.message,phonk_2s)
    elif call.data == 'phonk_3':
        bot.send_message(call.message.chat.id,"🔮 - ادخـل الـرسـالة")
        bot.answer_callback_query(call.id)
        bot.register_next_step_handler(call.message,sphonk_9)
    elif call.data == 'phonk_4':
        bot.send_message(call.message.chat.id,"✉️ - ادخـل الـموضـوع")
        bot.answer_callback_query(call.id)
        bot.register_next_step_handler(call.message,goldsp2)
    elif call.data == 'phonk_5':
        bot.send_message(call.message.chat.id,"♻️ - الـسرعـة")
        bot.answer_callback_query(call.id)
        bot.register_next_step_handler(call.message,goldsp1)
    elif call.data == 'phonk_6':
        GoldenX6(call.message)
        bot.answer_callback_query(call.id)
    elif call.data == 'phonk_7':
        try:
            os.remove('Gold-email_pas.json')
            bot.send_message(call.message.chat.id,"✅ - تـم الـمسح")
        except FileNotFoundError:
            bot.send_message(call.message.chat.id,"⛔️ - لايـوجد ")
        bot.answer_callback_query(call.id)
    elif call.data == 'phonk_8':
        bot.send_message(call.message.chat.id,"🛡 - ايـميـل الدعـم")
        bot.answer_callback_query(call.id)
        bot.register_next_step_handler(call.message,phonk_8)     
    elif call.data == 'phonk_9':
        bot.send_message(call.message.chat.id,"❓ - كـم الـعدد")
        bot.answer_callback_query(call.id)
        bot.register_next_step_handler(call.message,phonk_9)       
    elif call.data == 'check_info':
        goldsp6 = ['Gold-email_pas.json','golden1.json','golden2.json','golden3.json','golden4.json','golden5.json']
        gold_rsp = ""
        for file in goldsp6:
            if os.path.exists(file) and os.stat(file).st_size > 0:
                gold_rsp += f"{file} - ✅\n"
            else:
                gold_rsp += f"{file} - ❌\n"
        bot.send_message(call.message.chat.id,gold_rsp)
        bot.answer_callback_query(call.id)
    elif call.data == 'goldsp5':
        start(call.message)
def phonk_2s(message):
    goldsp3 = message.text.strip()
    goldsp4 = goldsp3.split('\n')
    gold_spx = {}
    for account in goldsp4:
        if ':' in account:
            email,password = account.split(':')
            gold_spx[email.strip()] = password.strip()
    if gold_spx:
        gold_crr1 = GoldenX2()
        gold_crr1.update(gold_spx)
        GoldenX3(gold_crr1)
        bot.send_message(message.chat.id,"✅ - تـم ")
    else:
        bot.send_message(message.chat.id,"🚫 - لايـوجد حـسابات")
def sphonk_9(message):
    GoldenT1 = message.text.strip()
    GoldenX5('golden1.json',GoldenT1)
    bot.send_message(message.chat.id,"✅ - تـم ")
def goldsp2(message):
    GoldenT2 = message.text.strip()
    GoldenX5('golden2.json',GoldenT2)
    bot.send_message(message.chat.id,"✅ - تـم ")
def goldsp1(message):
    GoldenT3 = message.text.strip()
    GoldenX5('golden3.json',GoldenT3)
    bot.send_message(message.chat.id,"✅ - تـم ")
def phonk_8(message):
    GoldenT4 = message.text.strip()
    GoldenX5('golden4.json',GoldenT4)
    bot.send_message(message.chat.id,"✅ - تـم ")
def phonk_9(message):
    GoldenT5 = message.text.strip()
    GoldenX5('golden5.json',GoldenT5)
    bot.send_message(message.chat.id,"✅ - تـم ")
bot.polling()