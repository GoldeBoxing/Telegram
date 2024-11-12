from telethon import TelegramClient,events
import random
import asyncio
G1 = '$$$'  # - [ > ايبي ايدي < ]
G2 = '$$$'  # - [ > ايبي هاش < ]
G3 = 5846480832  # - [ > ايديك < ]
grr = 'N_1_N_6'  # - [ > الكروب < ]
G4 = ["**💌 ¦ مشــتاقـين . **","**❤️‍🩹 ¦ ويـن مخـتفي . **","**💔 ¦ زعـلان عـليك . **","**📿 ¦ اللـه بـ الخـير . **","**✨ ¦ احــبك . **","**🌚 ¦ ويــنك . **","**🧸 ¦ فديـتك . **","**🦦 ¦ ثكــيل . **","**💃🏻 ¦ كــولدن يسـئل علـيك . **","**🧚🏻 ¦ تع بحـضني . **","**🫦 ¦ امــوت عليــك . **","**🥲 ¦ نايـم كاعـد . **","**🌝 ¦ هـا خـالي . **","**😒 ¦ ويــن طــامـس . **","**🥺 ¦ خــايـن . **","**🫀 ¦ كـيوت . **"]
Golden = TelegramClient('see',G1,G2)
G5 = False
G6 = None
async def Mx1():
    return await Golden.get_participants(grr)
async def Mx2(Gss):
    global G5
    while G5:
        G7 = await Mx1()
        if G7:
            G8 = random.choice(G7)
            G9 = G8.first_name if G8.first_name else "واحد من الناس"
            if G8.username:
                lin = f"https://t.me/{G8.username}"
            else:
                lin = f"tg://openmessage?user_id={G8.id}"
            G10 = random.choice(G4) + f"[{G9}]({lin})"
            await Golden.send_message(grr,G10,parse_mode='markdown')
        await asyncio.sleep(Gss)
@Golden.on(events.NewMessage(pattern=r'.تك (\d+)'))
async def Mx2(rrrrrf):
    global G5,G6
    if rrrrrf.sender_id != G3:
        return
    Gss = int(rrrrrf.pattern_match.group(1))
    if not G5:
        G5 = True
        await rrrrrf.reply(f"""**✨ ¦ تــم تفـعيل التاك الـعشوائي . **
**🔰 ¦ الــمدة بيـن كــل شخـص . `{Gss}` .**""")
        G6 = asyncio.create_task(Mx2(Gss))
@Golden.on(events.NewMessage(pattern=r'.تو'))
async def Mx3(rrrrrf):
    global G5,G6
    if rrrrrf.sender_id != G3:
        return  
    if G5:
        G5 = False
        if G6:
            G6.cancel()
        await rrrrrf.reply("**🚫 ¦ تم توقيـف الـتاك العشــوائي .**")
with Golden:
    Golden.run_until_disconnected()
