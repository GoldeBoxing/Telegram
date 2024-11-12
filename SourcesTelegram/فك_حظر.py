from telethon import TelegramClient,events
import asyncio
from telethon.tl.functions.messages import DeleteHistoryRequest
H1 = '$$$'  # - [ > ايبي ايدي < ]
H2 = '$$$'  # - [ > ايبي هاش < ]
H3 = 5846480832  # - [ > ايديك < ]
Hossam = TelegramClient('see',H1,H2)
@Hossam.on(events.NewMessage(pattern='.فك'))
async def Hs1(I_S_4):
    Hoss = await I_S_4.get_sender()
    if Hoss.id != H3:
        return
    if Hoss.is_self:
        H4 = await I_S_4.reply(f"""**✨ ¦ انتــضر عــزيـزي جــاري فـك الـحضـر عـنك . **
**👨🏻‍💻 ¦ تم بـرمجـة الـسورس علـئ يـد ₊ @rrrrrF ⁺ .**""")
        await Hossam.send_message('@SpamBot','/start')
        await asyncio.sleep(2)
        H5 = await Hossam.get_messages('@SpamBot',limit=1)
        if "Good news,no limits are currently applied to your account. You’re free as a bird!" or "أخبار جيدة" or "أنت حر" or "لا يتم تطبيق حدود حاليا على حسابك" in msg[0].message:
            await H4.edit(f"""**✅ ¦ انــت غــير مـحضـور. **""")
            await Hossam(DeleteHistoryRequest(peer='@SpamBot',max_id=H5[0].id))
        else:
            HxH = H5[0].buttons
            if HxH and len(HxH) >= 3:
                await H5[0].click(1)
            await asyncio.sleep(2)
            H5 = await Hossam.get_messages('@SpamBot',limit=1)
            HxH = H5[0].buttons
            if HxH and len(HxH) >= 2:
                await H5[0].click(1)
            await Hossam.send_message('@SpamBot','/start')
            await asyncio.sleep(2)
            H5 = await Hossam.get_messages('@SpamBot',limit=1)
            if "Good news,no limits are currently applied to your account. You’re free as a bird!" or "أخبار جيدة" or "أنت حر" or "لا يتم تطبيق حدود حاليا على حسابك" in msg[0].message:
                await H4.edit(f"""**🔰 ¦ تــم فـك الـحضـر عـنك . **""")
            else:
                await I_S_4.reply(f"""**📛 ¦ لــم يــتم فـك الحـضر عــنك . **""")
            await Hossam(DeleteHistoryRequest(peer='@SpamBot',max_id=H5[0].id))
Hossam.start()
Hossam.run_until_disconnected()
