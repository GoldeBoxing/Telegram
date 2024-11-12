from telethon import *
s_ = '' # - [ > ايبي ايدي < ]
h_ = '' # - [ > ايبي هاش < ]
d_ = 5846480832 # - [ > ايديك < ]
i = TelegramClient('see',s_,h_)
@i.on(events.NewMessage(pattern=r'.م (.+) (\d+)'))
async def G(l):
    if l.sender_id == d_:
        t_ = l.pattern_match.group(1)
        o = int(l.pattern_match.group(2))
        await l.delete()
        for _ in range(o):
            await l.reply(t_)
i.start()
i.run_until_disconnected()
