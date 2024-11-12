from telethon import TelegramClient,events
import datetime
import random
import time
Gm1 = ''# - api-id
Gm2 = '' # - api-hash 
GoldID = 5846480832 # id-telegram
client = TelegramClient('see',Gm1,Gm2)
Geeemo = ["✨","💥","🌈","⚔️","📿","💌","🤎","🔰","🔹","🌚","💠","🧃","🪬","🌐","😻"]
@client.on(events.NewMessage(pattern=r'(?i)(me|اني)'))
async def Gm4(event):
    if event.sender_id != GoldID:
        return
    Gx1 = random.choice(Geeemo)
    Gx2 = await event.get_sender()
    Gx3 = await client.get_messages(Gx2,limit=1)
    Gx4 = len(Gx3)
    if Gx4 > 0:
        photo = await client.download_profile_photo(Gx2)
    else:
        photo = None
    if event.is_private:
        Gx5 = await client.get_messages(Gx2,limit=1)
    else:
        Gx5 = await client.get_messages(event.chat_id,from_user=Gx2,limit=1)
    Gx5 = Gx5.total
    Gx6 = datetime.datetime.now().strftime('%H:%M:%S')
    Gx7 = datetime.datetime.now().strftime('%Y-%m-%d')
    Gx8 = (
        f"{Gx1} - name : {Gx2.first_name}\n"
        f"{Gx1} - username : @{Gx2.username}\n"
        f"{Gx1} - ID : {Gx2.id}\n"
        f"{Gx1} - photo : {Gx4}\n"
        f"{Gx1} - message : {Gx5}\n"
        f"{Gx1} - account : 2017,4,19\n" # اختياري
        f"{Gx1} - time : {Gx6}\n"
        f"{Gx1} - days : {Gx7}"
    )
    if photo:
        await event.respond(Gx8,file=photo)
    else:
        await event.respond(Gx8)
@client.on(events.NewMessage(pattern=r'(?i)(منو)'))
async def Gm5(event):
    if event.sender_id != GoldID:
        return
    if event.is_reply:
        Gx9 = await event.get_reply_message()
        Gx2 = await Gx9.get_sender()
    else:
        args = event.message.text.split()
        if len(args) < 2:
            await event.respond("❌ - Error\n✅ - منو <username>\n✅ - منو <id>\n✅ - منو <message>")
            return
        identifier = args[1]
        if identifier.isdigit():
            Gx2 = await client.get_entity(int(identifier))
        else:
            Gx2 = await client.get_entity(identifier)
    Gx3 = await client.get_messages(Gx2,limit=1)
    Gx4 = len(Gx3)
    if Gx4 > 0:
        photo = await client.download_profile_photo(Gx2)
    else:
        photo = None
    Gx5 = await client.get_messages(event.chat_id,from_user=Gx2,limit=1)
    Gx5 = Gx5.total
    Gx6 = datetime.datetime.now().strftime('%H:%M:%S')
    Gx7 = datetime.datetime.now().strftime('%Y-%m-%d')
    try:
        me = await client.get_me()
        Gx10 = me.date.strftime('%Y-%m-%d') if me.date else ''
    except AttributeError:
        Gx10 = ''
    Gx1 = random.choice(Geeemo)
    Gx8 = (
        f"{Gx1} - name : {Gx2.first_name}\n"
        f"{Gx1} - username : @{Gx2.username}\n"
        f"{Gx1} - ID : {Gx2.id}\n"
        f"{Gx1} - photo : {Gx4}\n"
        f"{Gx1} - message : {Gx5}\n"
        f"{Gx1} - account : {Gx10}\n"
        f"{Gx1} - time : {Gx6}\n"
        f"{Gx1} - days : {Gx7}"
    )
    if photo:
        await event.respond(Gx8,file=photo)
    else:
        await event.respond(Gx8)
Golden_stop = False
@client.on(events.NewMessage(pattern=r'(?i)بحث (.+)'))
async def Teammmmmmmm1(event):
    global Golden_stop
    if event.sender_id != GoldID:
        return
    args = event.pattern_match.group(1).split(maxsplit=1)
    if len(args) < 2:
        await event.respond("❌ - Error\n✅ : بحث <@channel/@group> <message>")
        return
    Gx10 = args[0]
    Gx11 = args[1]
    try:
        Golden_stop = True
        GTX = 0
        async for message in client.iter_messages(Gx10,search=Gx11):
            if not Golden_stop:
                break
            GTX += 1
            Gx12 = f"https://t.me/{Gx10.split('@')[1]}/{message.id}"
            await event.respond(f"🔗 - {Gx12}")
        await event.respond(f"🕵️‍♂️ - {GTX}")
    except Exception as e:
        await event.respond(f"❌ - Error")
    finally:
        Golden_stop = False
@client.on(events.NewMessage(pattern=r'(?i)خلاص'))
async def Teammmmmmmm4(event):
    global Golden_stop
    if event.sender_id != GoldID:
        return
    Golden_stop = False
    await event.respond("🛑 - stop")
client.start()
client.run_until_disconnected()