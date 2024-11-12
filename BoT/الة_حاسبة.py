import telebot
from telebot import types
G1 = '' #توكنك
G2 = telebot.TeleBot(G1)
def Golden1(G7=""):
    G3 = types.InlineKeyboardMarkup()
    G4 = [
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9'],
        ['0']
    ]
    G5 = ['+','-','×','÷','^','%','√']
    for G6 in G4:
        G3.add(*[types.InlineKeyboardButton(button,callback_data=button) for button in G6])
    G3.add(*[types.InlineKeyboardButton(op,callback_data=op) for op in G5],row_width=4)
    G3.add(types.InlineKeyboardButton('C',callback_data='C'),row_width=1)
    G3.add(types.InlineKeyboardButton('=',callback_data='='),row_width=1)
    return G3
@G2.callback_query_handler(func=lambda call: True)
def Golden2(call):
    if call.data == '=':
        G7 = call.message.text
        try:
            G7 = G7.replace('×','*').replace('÷','/').replace('√','**0.5')
            G8 = str(eval(G7))
        except:
            G8 = "❌"
        G2.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=G8,reply_markup=Golden1())
    elif call.data == 'C':
        G2.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="0",reply_markup=Golden1())
    else:
        if call.message.text == "0":
            Gx123 = call.data
        else:
            Gx123 = call.message.text + call.data
        G2.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=Gx123,reply_markup=Golden1(Gx123))
@G2.message_handler(commands=['start'])
def Golden3(Gx0):
    G2.send_message(Gx0.chat.id,"0",reply_markup=Golden1())
G2.polling()
