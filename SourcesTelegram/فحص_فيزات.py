from telethon import TelegramClient
import asyncio
import time
G1 = 'id'
G2 = 'hash'
G3 = '@SDBB_Bot'
G4 = input('- FILE > ')
async def X():
    Golden = TelegramClient('see',G1,G2)
    await Golden.start()
    await Golden.get_me()
    with open(G4,'r') as GG:
        G5 = GG.readlines()
    for G6 in G5:
        G7 = G6.strip()
        G8 = f"/chk {G7}"
        await Golden.send_message(G3,G8)
        await asyncio.sleep(14)
    await Golden.disconnect()
asyncio.run(X())
