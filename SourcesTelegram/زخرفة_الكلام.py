from telethon import *
import random
i = 'api-id'  
h = 'api-hash'  
v = TelegramClient('see',i,h)
c = [['〚  ','  〛'],['《  ','  》'],['◟ ',' ◞'],['『  ','  』'],['〖  ','  〗'],['「  ','  」'],['﹄ ',' ﹃'],['〘  ','  〙']]
s = [  '✦','└  ⑅','、ヽ','---⋆','ⴰ⁺.﹆','⸝⸝']
p = {  '0': '𝟎','1': '𝟏','2': '𝟐','3': '𝟑','4': '𝟒','5': '𝟓','6': '𝟔','7': '𝟕','8': '𝟖','9': '𝟗'}
def xix(b):  
    x = random.choice(c)  
    z = random.choice(s)  
    l = b.split()  
    o = ""  
    for t in l:  
        r = ""  
        for char in t:
            if char.isdigit():
                r += p[char]
            else:
                r += char
        o += f'`{z} {x[0]}`**{r}**`{x[1]}`\n'
    return o
@v.on(events.NewMessage(outgoing=True))
async def xFx(d):
    k = d.raw_text
    e = xix(k)
    if k != e:
        await d.edit(e)
v.start()
v.run_until_disconnected()
