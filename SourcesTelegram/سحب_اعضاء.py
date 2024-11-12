from telethon import TelegramClient,events
from telethon.tl.functions.channels import InviteToChannelRequest
import asyncio
d = '$$$' # - [ > ايبي ايدي < ]
z = '$$$' # - [ > ايبي هاش < ]
b = 5846480832 # - [ > ايديك < ]
q = 'N_1_N_6' # - [ > الكروب الاساسي < ]
m = '$$$' # - [ > الكروب الي تسحب منه < ]
i = TelegramClient('see',d,z)
c = set()
async def gold(dos):
    if dos.id in c:
        return
    try:
        await i(InviteToChannelRequest(q,[dos]))
        c.add(dos.id)
        print(f"Good - {dos.first_name} - {dos.id} .")
    except Exception as e:
        if 'A wait of' in str(e):
            wt = int(str(e).split('A wait of ')[1].split(' seconds')[0])
            print(f"er - {dos.first_name} - {dos.id} - {wt} .")
            await asyncio.sleep(wait_time)
            await gold(dos)
async def bb():
    await i.start()
    @i.on(events.NewMessage(pattern='.تش'))
    async def bo(rrr):
        if rrr.sender_id != b:
            return
        v = await i.get_entity(m)
        async for dos in i.iter_participants(v):
            if dos.bot: 
                continue
            await gold(dos)
            await asyncio.sleep(5)
    await i.run_until_disconnected()
t = asyncio.get_event_loop()
t.run_until_complete(bb())
