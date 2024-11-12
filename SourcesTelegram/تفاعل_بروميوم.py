from telethon.sync import TelegramClient,events
from telethon.tl.functions.messages import SendReactionRequest
from telethon.tl.types import ReactionCustomEmoji
import random
import asyncio
import json
G1=''  # - api-id
G2=''  # - api-hash
f=[5846480832] # - ID
G4=False
Golden=TelegramClient('see',G1,G2)
k=[5472212841081622131,5316767533573884148,5469931384518755322] # - استخرج ايديات الايموجي المميز الي تريدة سويلك كود ويستخرجلك 
try:
    with open('idd.json','r') as file:
        x=json.load(file)
except FileNotFoundError:
    x={}
@Golden.on(events.NewMessage)
async def i(c):
    global G4
    n=c.chat_id
    m=c.sender_id
    if G4 and str(n) in x and m in x[str(n)]:
        selected_emojis=random.sample(k,3)
        await asyncio.sleep(1)
        await Golden(SendReactionRequest(peer=n,msg_id=c.message.id,reaction=[ReactionCustomEmoji(document_id=emoji) for emoji in selected_emojis]))
        await asyncio.sleep(3)
@Golden.on(events.NewMessage(pattern=r'.ت(?: (\d+))?'))
async def a(c):
    if c.sender_id in f:  
        global G4
        if c.is_reply:
            p=await c.get_reply_message()
            o=p.sender_id
        elif c.pattern_match.group(1):
            o=int(c.pattern_match.group(1))
        else:
            return
        n=str(c.chat_id)
        if n not in x:
            x[n]=[]
        if o not in x[n]:
            x[n].append(o)
            with open('idd.json','w') as file:
                json.dump(x,file)
        G4=True
        await c.reply(f"**✨ ¦  تـم تفـعيل الـتفاعل لــ `{o}` .**")
@Golden.on(events.NewMessage(pattern=r'.و(?: (\d+))?'))
async def y(c):
    if c.sender_id in f:
        if c.is_reply:
            p=await c.get_reply_message()
            o=p.sender_id
        elif c.pattern_match.group(1):
            o=int(c.pattern_match.group(1))
        else:
            return
        n=str(c.chat_id)
        if n in x and o in x[n]:
            x[n].remove(o)
            if not x[n]:
                del x[n]
            with open('idd.json','w') as file:
                json.dump(x,file)
        await c.reply(f"**✨ ¦ تـم حــذف ايـديـة `{o}` .**")
Golden.start()
Golden.run_until_disconnected()
