from datetime import datetime as da
from random import choice as ch
from aiocron import crontab as cr
from pyrogram import Client, idle
from pytz import timezone as time
myid = ''
myhash = ''
mynumb = '' 
time_zone,fonts = time("Asia/Baghdad"),[["𝟬", "𝟭", "𝟮", "𝟯", "𝟰", "𝟱", "𝟲", "𝟳", "𝟴", "𝟵"]]
app = Client("mysee",myid,myhash,phone_number=mynumb)
@cr("*/1 * * * *", tz=time_zone, start=False)
async def change_name():
    table = str.maketrans("0123456789", "".join(ch(fonts)))
    time,biot = da.now(time_zone).strftime("%I:%M"),"Time > {}"
    await app.update_profile(last_name=time.translate(table),bio=biot.format(time.translate(table)))
app.start(),change_name.start(),idle(),change_name.stop(),app.stop()
