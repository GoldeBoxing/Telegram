from telethon import TelegramClient,events
from telethon.tl.types import PeerChannel
G1 = '$$$'  # - [ > ايبي ايدي < ]
G2 = '$$$'  # - [ > ايبي هاش < ]
G3 = 'N_1_N_6'  # - [ > الكروب < ]
G4 = 5846480832  # - [ > ايديك < ]
G5 = 5292982033  # - [ > ايدي الشخص الي تريد تقلدة < ]
G6 = False
Golden = TelegramClient('see',G1,G2)
async def sSs():
    @Golden.on(events.NewMessage(pattern=r".تق"))
    async def xXx(rrrrrF):
        global G6
        if rrrrrF.sender_id == G4:
            G6 = True
            await rrrrrF.reply("**✨ ¦ تــم تفـعيل التــقليد . **")
    @Golden.on(events.NewMessage(pattern=r".تو"))
    async def zZz(rrrrrF):
        global G6
        if rrrrrF.sender_id == G4:
            G6 = False
            await rrrrrF.reply("**✨ ¦ تـم ايقاف التــقليد . **")
    G7 = await Golden.get_entity(G3)
    @Golden.on(events.NewMessage(chats=PeerChannel(G7.id)))
    async def tTt(rrrrrF):
        if G6 and rrrrrF.sender_id == G5:
            await rrrrrF.reply(rrrrrF.message.message)
    await Golden.run_until_disconnected()
with Golden:
    Golden.loop.run_until_complete(sSs())
