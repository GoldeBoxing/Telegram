import asyncio
from telethon import TelegramClient,events
from telethon.tl.functions.contacts import GetContactsRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.errors import (
    UserPrivacyRestrictedError,ChatAdminRequiredError,
    ChannelPrivateError,FloodWaitError,UserNotMutualContactError
)
from telethon.tl.types import InputPeerChannel,InputPeerChat
G1 = '$$$'  # - [ > ايبي ايدي < ]
G2 = '$$$'  # - [ > ايبي هاش < ]
G3 = 5846480832  # - [ > ايديك < ]
G4 = True
G5 = []
Golden = TelegramClient('see',G1,G2)
async def sSs():
    await Golden.start()
    @Golden.on(events.NewMessage(pattern='.تش'))
    async def xXx(rrrrrF):
        global G4
        if rrrrrF.sender_id != G3:
            return
        if G4:
            await rrrrrF.reply(f"""**✨ ¦ انتضـر عــزيزي جـاري جلـب اعضـاء . **""")
            try:
                G6 = await Golden(GetContactsRequest(hash=0))
                G7 = [contact.user_id for contact in G6.contacts]
                G8 = len(G5)
                for i,Gid in enumerate(G7[G8:],start=G8):
                    if Gid not in G5 and G4:
                        try:
                            if rrrrrF.is_channel:
                                await Golden(InviteToChannelRequest(rrrrrF.chat_id,[Gid]))
                            elif rrrrrF.is_group:
                                await Golden(AddChatUserRequest(rrrrrF.chat_id,Gid,fwd_limit=10))
                            user = await Golden.get_entity(Gid)
                            username = user.username if user.username else ""
                            user_name = f"@{username}" if username else ""
                            G5.append(Gid)
                            await asyncio.sleep(5)
                        except UserNotMutualContactError:
                            print(f"< X > - {Gid}")
                        except FloodWaitError as e:
                            await asyncio.sleep(e.seconds)
                            await xXx(rrrrrF)
                        except UserPrivacyRestrictedError:
                            print(f"< A > - {Gid}")
                        except Exception:
                            print(f"< X >")
                await rrrrrF.reply("**🐉 ¦ تـم الاكــتمال بـنجاح .**")
            except ChatAdminRequiredError:
                await rrrrrF.reply("**⚠️ ¦ انـت لـيس مشـرف فـيها .**")
            except ChannelPrivateError:
                await rrrrrF.reply("**📛 ¦ تـاكد مـن انـها عـامة .**")
        else:
            await rrrrrF.reply("**✅ ¦ تـم ايـقاف الـرشـق .**")
    @Golden.on(events.NewMessage(pattern='.تو'))
    async def vVv(rrrrrF):
        global G4
        if rrrrrF.sender_id == G3:
            G4 = False
            await rrrrrF.reply("**✅ ¦ تـم ايـقاف الـرشـق .**")
    await Golden.run_until_disconnected()
with Golden:
    Golden.loop.run_until_complete(sSs())
