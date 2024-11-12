from telebot import *
to = '' # - توكتك
bo = telebot.TeleBot(to)
@bo.message_handler(commands=['start'])
def Gss(gold):
    G1 = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
    G2 = types.KeyboardButton(text="₊ مـشاركــة ⁺",request_contact=True)
    G1.add(G2)
    bo.send_message(gold.chat.id,"*⚠️ ¦ عــليك مـشاركـة جهـة اتصـالك لكـي نتـحقق انـك ليـس روبـوت \.*\n\n*🌈 ¦ الــمبـرمج @rrrrrF \.*\n\n*🔰 تــابـع لــ @N_9_N_6 \.*",reply_markup=G1,parse_mode='MarkdownV2')
@bo.message_handler(content_types=['contact'])
def Gxx(gold):
    if gold.contact is not None:
        bo.send_message(gold.chat.id,"*✅ ¦ تـم الـتحـقق انـك انـســان \.*",parse_mode='MarkdownV2')
bo.polling()
