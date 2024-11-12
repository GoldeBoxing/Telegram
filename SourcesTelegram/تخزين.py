from telethon import TelegramClient,events
from telethon.tl.functions.messages import CreateChatRequest
from telethon.tl.types import InputPeerUser
import os
import re
import json
rf1 = '' # - api-id
rf2 = '' # - api-hash
rf3 = '+964' # - رقمك
rf4 = 'GR.json'
iraq = TelegramClient('see',rf1,rf2)
async def Golden3(name):
    me = await iraq.get_me()
    rf26 = [InputPeerUser(me.id,me.access_hash)]
    rf27 = await iraq(CreateChatRequest(title=name,users=rf26))
    return rf27.chats[0]
async def Golden():
    await iraq.start(phone=rf3)
    if os.path.exists(rf4):
        with open(rf4,'r') as file:
            rf5 = json.load(file)
            rf6 = rf5.get('gold1')
            rf7 = rf5.get('gold2')
    else:
        rf8 = "التخزين الخارجي"
        rf9 = await Golden3(rf8)
        rf10 = "التخزين الداخلي"
        rf11 = await Golden3(rf10)
        with open(rf4,'w') as file:
            json.dump({
                'gold1': rf9.id,
                'gold2': rf11.id
            },file)
        rf6 = rf9.id
        rf7 = rf11.id
    @iraq.on(events.NewMessage)
    async def Golden1(event):
        me = await iraq.get_me()
        rf12 = me.id
        if event.is_private:
            rf13 = await event.get_sender()
            if event.sender_id != rf12 and not rf13.bot:
                rf14 = rf13
                if event.message.message:
                    rf15 = f"✨ - @{rf14.username}\n\n💌 - " if rf14.username else f"✨ -  {rf14.id}\n"
                    rf16 = rf15 + event.message.message
                    await iraq.send_message(rf6,rf16)
                if event.message.media:
                    rf15 = f"✨ - @{rf14.username}\n\nBy - @rrrrrF" if rf14.username else f"✨ -  {rf14.id}\n"
                    rf17 = await event.message.download_media()
                    await iraq.send_file(rf6,rf17,caption=rf15)
                    os.remove(rf17)
            elif event.sender_id == rf12:
                if event.message.message:
                    rf15 = f"✨ - @{me.username}\n\n💌 - " if me.username else f"👤 - {me.id}\n"
                    rf16 = rf15 + event.message.message
                    await iraq.send_message(rf7,rf16)
                    rf18 = await event.get_reply_message()
                    if rf18:
                        receiver_username = rf18.sender.username if rf18.sender.username else rf18.sender.id
                        rf19 = f"✨ - @{me.username} ==> 👥- @{receiver_username}\n\n💌 - " + event.message.message
                        await iraq.send_message(rf7,rf19)
                if event.message.media:
                    rf15 = f"✨ - @{me.username}\n\nBy - @rrrrrF" if me.username else f"👤 - {me.id}\n"
                    rf16 = rf15
                    rf17 = await event.message.download_media()
                    await iraq.send_file(rf7,rf17,caption=rf16)
                    os.remove(rf17)
                    rf18 = await event.get_reply_message()
                    if rf18:
                        receiver_username = rf18.sender.username if rf18.sender.username else rf18.sender.id
                        rf19 = f"✨ - @{me.username} ==> 👥- @{receiver_username}\n\n💌 - "
                        await iraq.send_file(rf7,rf17,caption=rf19)
                        os.remove(rf17)
    @iraq.on(events.NewMessage(pattern='.سحب (.+)'))
    async def Golden2(event):
        rf20 = event.pattern_match.group(1)
        rf21 = re.match(r'https://t\.me/(.+)/(\d+)',rf20)
        if rf21:
            rf22 = rf21.group(1)
            rf23 = int(rf21.group(2))
            try:
                rf24 = await iraq.get_messages(rf22,ids=rf23)
                if rf24:
                    if rf24.message:
                        rfr = rf24.message
                    else:
                        rfr = ""
                    if rf24.media:
                        rf25 = await rf24.download_media()
                        await iraq.send_file(rf7,rf25,caption=rfr)
                        os.remove(rf25)
                    else:
                        await iraq.send_message(rf7,rfr)
            except Exception as e:
                await event.reply(f"⚠️ - Error")
        else:
            await event.reply("⚠️ - https://t.me/<channel>/<message>")
iraq.loop.run_until_complete(Golden())
iraq.run_until_disconnected()