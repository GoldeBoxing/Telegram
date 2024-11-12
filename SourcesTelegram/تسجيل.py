from telethon.sync import TelegramClient,events
import re
idd = '' # ايبي ايدي
ha = '' # ايبي هاش
sis ='see.session' # اسم الجلسة
client = TelegramClient(sis,idd,ha)
@client.on(events.NewMessage(from_users=777000))
async def Golden(event):
    otp = re.search(r'\b(\d{5})\b', event.raw_text)
    if otp:
        print("Code :", otp.group(0))
print('wait . . .')
client.start()
client.run_until_disconnected()
