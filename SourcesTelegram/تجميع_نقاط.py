from telethon import *;import asyncio;from telethon.tl.functions.channels import *
D1 = 'api-id'
D2 = 'api-hash'
D3 = 5846480832
Demo = TelegramClient('Demo',D1,D2)
@Demo.on(events.NewMessage(pattern='.دعمكم'))
async def xXx(N):
    if N.sender_id != D3:
        return
    await N.reply('** ¦ انتــضر . **')
    await Demo.send_message('@DamKombot','/start')
    D4 = await Demo.get_messages('@DamKombot',limit=1)
    if 'مرحبا بك في بوت DomKom' in D4[0].message:
        D5 = D4[0].buttons
        if D5:
            await D4[0].click(1)
        await asyncio.sleep(1)
        D4 = await Demo.get_messages('@DamKombot',limit=1)
        if ' تجميع نقاط' in D4[0].message:
            D5 = D4[0].buttons
            if D5:
                await D4[0].click(1)
            while True:
                D4 = await Demo.get_messages('@DamKombot',limit=1)
                if 'اشترك فالقناة' in D4[0].message:
                    D6 = D4[0].message
                    D7 = None
                    for D8 in D6.split():
                        if D8.startswith('@'):
                            D7 = D8
                            break
                    if D7:
                        await Demo(JoinChannelRequest(D7))
                        D5 = D4[0].buttons
                        if D5:
                            await D4[0].click(0)
                        await asyncio.sleep(1)
                elif 'لا يوجد قنوات حالياً ' in D4[0].message:
                    await N.reply('** ¦ تـم اكمـال التـجـميع .**')
                    break
Demo.start()
Demo.run_until_disconnected()
