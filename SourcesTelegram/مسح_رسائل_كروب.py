from telethon import *
import re
i = 'api-id'
h = 'api-hash'
x = [5846480832,6454667482]
g = -1001913140681 # ايدي الكروب
v = TelegramClient('see',i,h)
@v.on(events.NewMessage(pattern=r'^.م (\d+)$'))
async def hhhh(c):
    e = c.chat_id
    p = c.sender_id
    k = g
    if p not in x:
        return
    if c.is_group and e == k:
        b = re.match(r'^.م (\d+)$',c.raw_text)
        if b:
            z = int(b.group(1))
            s = await v.get_permissions(e,p)
            if s.is_admin:
                o = await v.get_messages(e,limit=z)
                for c in o:
                    await v.delete_messages(e,c.id)
                await c.reply(f"**✨ ¦ تـم مـسح  {len(o)} رسـالـه .**")
with v:
    v.run_until_disconnected()
