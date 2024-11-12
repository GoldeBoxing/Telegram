from telethon import TelegramClient,events
Gm1 = ''  # api-id
Gm2 = ''  # api-hash
GoldID = 5846480832 # id
client = TelegramClient('see',Gm1,Gm2)
@client.on(events.NewMessage(pattern=r'(?i)(مسح)'))
async def reemo(event):
    if event.sender_id != GoldID:
        return  
    async for message in client.iter_messages(event.chat_id,from_user='me'):
        await message.delete()
    await event.respond("✅ - Done")
client.start()
client.run_until_disconnected()
