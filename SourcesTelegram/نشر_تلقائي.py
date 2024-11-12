from telethon import TelegramClient,events
import asyncio
import re
idd = 23826569 #api-id
has = 'test'#api-hash
see = 'see'
client = TelegramClient(see,idd,has)
mex = 100
stoper = True
@client.on(events.NewMessage(pattern='/sand'))
async def GoldenStart(event):
    global stoper
    if stoper:
        G1 = event.message.message
        G2 = re.compile(r'/sand -m (.+?) -g (.+?) -s (\d+) -t (\d+)')
        G3 = G2.search(G1)
        if G3:
            G4 = G3.group(1).replace('\\n', '\n')
            G5 = G3.group(2).split()[:mex]
            G6 = int(G3.group(3))
            G7 = int(G3.group(4))
            for _ in range(G7):
                tasks = []
                for G8 in G5:
                    task = client.send_message(G8, G4)
                    tasks.append(task)
                await asyncio.gather(*tasks)
                await asyncio.sleep(G6)
@client.on(events.NewMessage(pattern='/stop'))
async def GoldenStop(event):
    global stoper
    stoper = False
    await event.reply(". STOP .")
client.start()
client.run_until_disconnected()
