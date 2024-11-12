import re
from telethon import TelegramClient,events
from telethon.errors import ChatWriteForbiddenError
import json
import asyncio
from datetime import datetime,timedelta
import random
G1 = 23826569 # api-id
G2 = '' # api-hash
G3 = '+964' # رقمك
Golden = TelegramClient('see',G1,G2)
G5 = '@N_1_N_6' # الكروب
G6 = [5409851102,5846480832] # اذا كان ب القروب بوت حماية اخذ ايدية وخلي 
G7 = '@ASSllbot' # اذا كان ب القروب بوت حماية اخذ يوزرة وخلي 
G8 = [7301709797,5846480832,6454667482,6688266382] # الادمنية
G9 = ['كوم بي','عيري','نياجك','نياجكم','كس امك','عير بشرفك','كس','عير','بلاع','طيز','كحبه','كحبة','ابن الكحبه','ابن الكحبة','منيوج','خرب الله','طيزي','زب','زبي','كس اختك','عير بيك','منيوك','زبي','ابن التنيج','كس خواتكم','تيل بيك','تعال مص','مص','يلا دي','فرخ','ديوث','طيزك','سكسي','ابو العيوه','منيلك عير','كس امهاتكم','كس خواتكم','ازرفك','سرسري','سرسريه','سرسرية','تبياته','تبياتة','انكحك','مناويج','فروخ','مبعوص','انبعصت','ابعصك','بعصه','العب بي','ماتجي تلعب بي','تعال العب بي','لعب بي','كس كرنك','وانيج امك','نيج','بعير','تس','لنيج','امك','كسة','وادحس','تيزك','تيزي','بتيزك','كسك','تخليني','اغتصبك','شرموطة','شرموطه'] # - تكدر تضيف وتمسح براحتك
G10 = ['زعطوط','انعل ابوك','كلب ابن الكلب','ابن المطي','ابن الخرا','ابن الخره','ابن الخرة','خره','كرة','زربة','كوم لك','بيبي','زنوج','زنجي','تلغيم','ملغم','دي لك','نعال','نجب عزيزي','fuck you','fuck','بنعال','ع راسك','راسك','واكعد عليه','اكعد عليه','واكعد علية','اكعد علية','تاج راسك','مخنث','خنيث','فاشل','دي','دعبل','لوكي','اهينك'] # - تكدر تضيف وتمسح براحتك
G11 = ['للبيع','تيك للبيع','ببجي للبيع','شراي','تعال وسيط','جيب وسيط','ادوات للبيع','اداه للبيع','مقابل','مقابلك','المقابل','سعرك','وسيط','اسيا','$','بفلوس','لل بيع','لبيع','للشراء','للشراي','للتبديل','متوفر','تمويل قنوات','تمويل كروبات','ضمان','كميات','السعر','حساب ببجي قوي','اثير','دفع','سوبر','سوبرات','بسوبرات','السوبر','السوبرات','كروبي','قناتي','انضمو','انضم','فعلي بوت','تفعيل بوت','تبادل','نقاط','بالبايو','البايو','بايو','مراوس'] # - تكدر تضيف وتمسح براحتك
G12 = False
G13 = {}
def Golden1(G14,G15):
    with open(G14,'a',encoding='utf-8') as f:
        json.dump(G15,f)
        f.write('\n')
def Golden2(G14):
    G13 = {}
    try:
        with open(G14,'r',encoding='utf-8') as f:
            for G16 in f:
                G15 = json.loads(G16)
                G18 = G15['user_id']
                if 'time' in G15 and G15['time']:
                    try:
                        G15['time'] = datetime.strptime(G15['time'],'%Y-%m-%d %H:%M:%S')
                    except ValueError:
                        G15['time'] = None
                G13[G18] = G15
    except FileNotFoundError:
        pass
    return G13
def G17(G18):
    if G18 in G13:
        del G13[G18]
        with open('G15.json','w',encoding='utf-8') as f:
            for G15 in G13.values():
                if 'time' in G15 and G15['time']:
                    G15['time'] = G15['time'].strftime('%Y-%m-%d %H:%M:%S')
                json.dump(G15,f)
                f.write('\n')
async def Golden3():
    while True:
        G19 = datetime.now()
        for G18,G15 in list(G13.items()):
            if isinstance(G15.get('time'),datetime) and G19 >= G15['time']:
                try:
                    G20 = await Golden.send_message(G5,f"**رف <@{G15['username']}>**")
                    await Golden.delete_messages(G5,G20.id)
                    await Golden.send_message(G5,f"""**- تم انتهاء مدة الكتم . ✅**
**- رجاء عدم تكرارها  . ❗️**
**- لروئية القوانين ارسل : `القوانين` . ⚠️**
**- الشـخص > @{G15['username']} . 👤**
**───── ───── ───── ────**
**﹆ ⋆ {G5} ❜ .**""")
                except ChatWriteForbiddenError:
                    pass
                except Exception:
                    pass
                G17(G18)
        await asyncio.sleep(5)
@Golden.on(events.NewMessage)
async def Golden4(rrrrrrF):
    if not G12:
        return
    if rrrrrrF.sender_id in G6:
        return
    sender = await rrrrrrF.get_sender()
    if sender is None:
        return
    if sender.username == G7:
        return
    chat = await rrrrrrF.get_chat()
    if chat is None or chat.username != G5.lstrip('@'):
        return

    G21 = [
        '⌔︙عذرآ لا تستطيع استخدام الامر على البوت',
        '⌔︙عذرآ لا تستطيع استخدام الامر على { الادمـــــن 🌟 }'
    ]
    if rrrrrrF.message.text in G21:
        await rrrrrrF.delete()
        return
    G22 = rrrrrrF.message.text.lower()
    G18 = rrrrrrF.message.sender_id
    G24 = sender.username if sender.username else str(G18)
    G25 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    def Golden5(G26,G24,G22):
        return f"""**انا سورس حماية تابع لـ @rrrrrF . 🌚**
**- احترم القوانين عزيزي . 🔰**
**- لروئية القوانين ارسل : `القوانين` . ⚠️**
**- الانـذارات > (3/{G26}) . 📛**
**- الرسالة > 🚫 .**
**- الشـخص > @{G24} . 👤**
**───── ───── ────**
**﹆ ⋆ {G5} ❜ .**"""
    def Golden7(G27,G22):
        G28 = r'\b' + re.escape(G27) + r'\b'
        return re.search(G28,G22) is not None
    if any(Golden7(G27,G22) for G27 in G9 + G10 + G11):
        if G18 not in G13:
            G13[G18] = {'count': 0,'time': None,'username': G24}
        G13[G18]['count'] += 1
        if G13[G18]['count'] < 3:
            Golden1('G15.json',{'user_id': G18,'username': G24,'message': G22,'time': G25})
            try:
                G29 = Golden5(G13[G18]['count'],G24,G22)
                await rrrrrrF.reply(G29)
            except ChatWriteForbiddenError:
                pass
            except Exception:
                pass
            return
        else:
            try:
                G30 = random.randint(1,50) * 60
                G13[G18]['time'] = datetime.now() + timedelta(seconds=G30)
                Golden1('G16.json',{'user_id': G18,'username': G24,'time': G13[G18]['time'].strftime('%Y-%m-%d %H:%M:%S')})
                await rrrrrrF.reply("كتم")
                await Golden.delete_messages(rrrrrrF.chat_id,rrrrrrF.message.id + 1)
                await rrrrrrF.reply(f"""**- : لم تقم باحترام القوانين . ⚠️**
**- : تم كتمك لمدة {G30 // 60} دقيقة . ⏰**
**- الشـخص > @{G24} . 👤**
**───── ──── ────** 
**﹆ ⋆ {G5} ❜ .**""")
                await asyncio.sleep(2)
                await Golden.edit_message(rrrrrrF.chat_id,rrrrrrF.message.id,f"""**- : لم تقم باحترام القوانين . ⚠️**
**- : تم كتمك لمدة {G30 // 60} دقيقة . ⏰**
**- الشـخص > @{G24} . 👤**
**───── ──── ────** 
**﹆ ⋆ {G5} ❜ .**""")
            except ChatWriteForbiddenError:
                pass
            except Exception:
                pass
@Golden.on(events.NewMessage(pattern='.تش'))
async def GoldenStart(rrrrrrF):
    if rrrrrrF.sender_id not in G8:
        return
    global G12
    G12 = True
    await rrrrrrF.reply('**تـم تشـغيل الـحماية . ✅\n\nلحد يسوي وكاحه . 🕵🏻**')
@Golden.on(events.NewMessage(pattern='.تو'))
async def GoldenStop(rrrrrrF):
    if rrrrrrF.sender_id not in G8:
        return
    global G12
    G12 = False
    await rrrrrrF.reply('**تم توقيف الحماية . 🔰**')
Golden.start(G3)
Golden.run_until_disconnected()