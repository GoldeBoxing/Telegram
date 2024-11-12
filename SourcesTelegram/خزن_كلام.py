from telethon import TelegramClient,events; import json,os
G1 = '$$$'  # - [ > ايبي ايدي < ]
G2 = '$$$'  # - [ > ايبي هاش < ]
G3 = 5846480832  # - [ > ايديك < ]
G4 = 'N_1_N_6'  # - [ > الكروب < ]
G5 = '$$$'  # - [ > كروب التخزين < ]
GRX = TelegramClient('see',G1,G2)
def Hossam():
    if os.path.exists('th.json'):
        with open('th.json','r') as f:
            G6 = json.load(f)
    else:
        G6 = {}
    @GRX.on(events.NewMessage(pattern=r'.خ (\d+)',chats=G4))
    async def Hossam2(rrrrrF):
        if rrrrrF.sender_id != G3:
            return
        G7 = rrrrrF.pattern_match.group(1)
        if str(G7) in G6:
            await rrrrrF.reply(f"""**✨ ¦ عــزيـز الـشخـص مــخـزن مـن قـبل . **""")
        else:
            G6[str(G7)] = True
            with open('th.json','w') as f:
                json.dump(G6,f)
            await rrrrrF.reply(f"""**✨ ¦ تـم تفـعيل الـخزيـن عـليه . **""")
    @GRX.on(events.NewMessage(pattern=r'.ع (\d+)',chats=G4))
    async def Hossam3(rrrrrF):
        if rrrrrF.sender_id != G3:
            return
        G7 = rrrrrF.pattern_match.group(1)
        if str(G7) in G6:
            del G6[str(G7)]
            with open('th.json','w') as f:
                json.dump(G6,f)
            await rrrrrF.reply(f"""**✨ ¦ تـم تــوقـيف التـخزيـن عــنـه . **""")
        else:
            await rrrrrF.reply(f"""**✨ ¦ عــزيـز الـشخـص لـم يتـفعل عـليه الـتـخـزين من قـبل . **""")
    @GRX.on(events.NewMessage(chats=G4))
    async def Fuck(rrrrrF):
        if str(rrrrrF.sender_id) in G6:
            await GRX.forward_messages(G5,rrrrrF.message)
    with GRX:
        GRX.run_until_disconnected()
Hossam()
