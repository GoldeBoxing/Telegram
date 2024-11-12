from telethon import *
from telethon.tl.functions.contacts import *
i = 'api-id'
h = 'api-hash'
f = 'id-tele'
x = TelegramClient('see',i,h)
@x.on(events.NewMessage(pattern='.مسح'))
async def c(rrrrrF):
    k = rrrrrF.sender_id
    chat_id = rrrrrF.chat_id
    if k != f:
        return
    y = await x(GetContactsRequest(hash=0))
    if y.users:
        v = [user.id for user in y.users]
        if v:
            d = await x(DeleteContactsRequest(id=v))
            await rrrrrF.reply(f"**✨ ¦ تـم مـسح {len(d.users)} جـهـة اتـصال .**")
    else:
        await rrrrrF.reply("**📛 ¦ لايـوجـد جـهات اتــصال .**")
x.start()
x.run_until_disconnected()
