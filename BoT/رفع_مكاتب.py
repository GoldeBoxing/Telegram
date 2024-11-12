import telebot,zipfile,os,subprocess,shutil,random
from telebot import types
GoldTok = '' #توكن
GoldTokPy = [''] #هنا تخلي توكن حسابك pypi 
GoldSex = 0
Goldad = 5846480832 #ايديك
bot = telebot.TeleBot(GoldTok)
G1 = 0
G2 = 0
G3 = {}
G4 = 0
G9 = {}
G17 = 0
G30 = 0
def Golden1():
    global GoldSex
    token = GoldTokPy[GoldSex]
    GoldSex = (GoldSex + 1) % len(GoldTokPy)
    return token
def Golden3():
    N1 = random.randint(1,9)
    N2 = random.randint(0,9)
    N3 = random.randint(0,9)
    return f"{N1}.{N2}.{N3}"
@bot.message_handler(commands=['start'])
def Golden4(message):
    global G4
    G4 += 1
    G5 = 'https://t.me/botpythonpypi/3'
    G6 = types.InlineKeyboardMarkup()
    G7 = types.InlineKeyboardButton("العربية",callback_data="Gtr1")
    G8 = types.InlineKeyboardButton("English",callback_data="Gtr2")
    G6.add(G7,G8)
    bot.send_photo(message.chat.id,photo=G5,reply_markup=G6)
    Gnmrod = f"Done - ✅\nName - {message.from_user.first_name}\nUsername - @{message.from_user.username}\nID - {message.chat.id}"
    bot.send_message(Goldad,Gnmrod)
@bot.callback_query_handler(func=lambda call: call.data.startswith("Gtr"))
def Golden9(call):
    if call.data == "Gtr1":
        G9[call.message.chat.id] = "ar"
    elif call.data == "Gtr2":
        G9[call.message.chat.id] = "en"
    bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
    G10 = 'https://t.me/botpythonpypi/4'
    G11 = types.InlineKeyboardMarkup()
    G12 = types.InlineKeyboardButton("⌯ رفع مكتبة ⌯" if G9[call.message.chat.id] == 'ar' else "Upload Library",callback_data="Gn1")
    G13 = types.InlineKeyboardButton(f"⌯ المستخدمين ⌯" if G9[call.message.chat.id] == 'ar' else f"User Count",callback_data="Gn2")
    G14 = types.InlineKeyboardButton(f"⌯ المكاتب المرفوعة ⌯" if G9[call.message.chat.id] == 'ar' else f"Library",callback_data="Gn3")
    G15 = types.InlineKeyboardButton("⌯ المبرمج ⌯" if G9[call.message.chat.id] == 'ar' else "Coder",url="https://t.me/rrrrrF")
    G11.add(G12)
    G11.add(G13,G14)
    G11.add(G15)
    bot.send_photo(call.message.chat.id,photo=G10,reply_markup=G11)
@bot.callback_query_handler(func=lambda call: call.data == "Gn1")
def Golden10(call):
    bot.send_message(chat_id=call.message.chat.id,text="🔰 - أرسل الملف بصيغة .zip")
@bot.callback_query_handler(func=lambda call: call.data == "back")
def Golden11(call):
    global G16,G17
    bot.delete_message(chat_id=call.message.chat.id,message_id=call.message.message_id)
    G11 = types.InlineKeyboardMarkup()
    G18 = types.InlineKeyboardButton("⌯ رفع المكتبة ⌯" if G9.get(call.message.chat.id,'ar') == 'ar' else "Upload Library",callback_data="Gn1")
    G19 = types.InlineKeyboardButton(f"⌯ المستخدمين ⌯" if G9.get(call.message.chat.id,'ar') == 'ar' else "Users",callback_data="Gn2")
    G20 = types.InlineKeyboardButton(f"⌯ المكاتب المرفوعة ⌯" if G9.get(call.message.chat.id,'ar') == 'ar' else "Library",callback_data="Gn3")
    G21 = types.InlineKeyboardButton("⌯ المبرمج ⌯" if G9.get(call.message.chat.id,'ar') == 'ar' else "Coder",url="https://t.me/rrrrrF")
    G11.add(G18)
    G11.add(G19,G20)
    G11.add(G21)
    G22 = 'https://t.me/botpythonpypi/3'
    bot.send_photo(call.message.chat.id,photo=G22,reply_markup=G11)
@bot.callback_query_handler(func=lambda call: call.data == "Gn2")
def Golden12(call):
    text = f"👥 - {G4}" if G9.get(call.message.chat.id,'ar') == 'ar' else f"👥 - {G4}"
    bot.answer_callback_query(callback_query_id=call.id,show_alert=True,text=text)
@bot.callback_query_handler(func=lambda call: call.data == "Gn3")
def Golden13(call):
    text = f"🗂 - {G17}" if G9.get(call.message.chat.id,'ar') == 'ar' else f"🗂 - {G17}"
    bot.answer_callback_query(callback_query_id=call.id,show_alert=True,text=text)
@bot.message_handler(content_types=['document'])
def Golden14(message):
    if message.document.mime_type == 'application/zip':
        G23 = bot.reply_to(message,". . ⏳ . ." if G9.get(message.chat.id,'ar') == 'ar' else ". . ⏳ . .")
        G24 = bot.get_file(message.document.file_id)
        G25 = bot.download_file(G24.GxF)
        G26 = os.path.join(os.getcwd(),"Gop1")
        src = f"{message.document.file_name}"
        with open(src,'wb') as new_file:
            new_file.write(G25)
        with zipfile.ZipFile(src,'r') as zip_ref:
            zip_ref.extractall(G26)
        G27 = []
        for root,dirs,files in os.walk(G26):
            for file in files:
                if file.endswith('.tar.gz') or file.endswith('.whl'):
                    G28 = os.path.join(root,file)
                    G27.append(G28)
        global G30
        if G27:
            for G28 in G27:
                G33 = Golden15(G28)
                token = Golden1()
                command = [
                    'twine','upload',G28,
                    '-u','__token__',
                    '-p',token
                ]
                subprocess.run(command,check=True)
                G30 += 1
                name = G33.get('name','error')
                version = G33.get('version','error')
                files = ','.join(G33.get('files',['error']))
                bot.edit_message_text(chat_id=message.chat.id,message_id=G23.message_id,text=f"✅ -  successfully .\n\n" +
                                                                                                f"🌐 - {os.path.basename(G28)}\n" +
                                                                                                f"♻️ - {name}\n" +
                                                                                                f"📂 - {version}")
        else:
            bot.edit_message_text(chat_id=message.chat.id,message_id=G23.message_id,text="❌ - Error")
        os.remove(src)
        shutil.rmtree(G26)
    else:
        bot.send_message(chat_id=message.chat.id,text="❌ - يرجى ارسال ملف بصيغة . zip")
def Golden15(GxF):
    Vx1 = ''.join(random.choices('qwertyuiopasdfghjklzxcvbnm1234567890',k=12))
    Vx2 = f"{random.randint(1,9)}.{random.randint(0,9)}.{random.randint(0,9)}"
    Vx3 = [] 
    return {'name': Vx1,'version': Vx2,'files': Vx3}
bot.polling()
