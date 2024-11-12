from telethon import TelegramClient,events
from telethon.tl.functions.channels import JoinChannelRequest,LeaveChannelRequest
from telethon.tl.functions.messages import DeleteHistoryRequest
from telethon.tl.functions.contacts import DeleteContactsRequest
from telethon.tl.types import InputPeerUser,Channel,User
import os
G1 = '23826569'  # - api-id
G2 = ''  # - api-hash
G3 = 5846480832  # - ايديك
Golden = TelegramClient('see',G1,G2)
cs1 = '.م قنوات' # - تكدر تكتب الي يعجبك لتغير [الامر]
cs2 = '.م كروبات' # - تكدر تكتب الي يعجبك لتغير [الامر]
cs3 = '.م بوتات' # - تكدر تكتب الي يعجبك لتغير [الامر]
cs4 = '.م الناس' # - تكدر تكتب الي يعجبك لتغير [الامر]
cs5 = '.م الكل' # - تكدر تكتب الي يعجبك لتغير [الامر]
cs6 = '.ت قنوات' # - تكدر تكتب الي يعجبك لتغير [الامر]
cs7 = '.ت كروبات' # - تكدر تكتب الي يعجبك لتغير [الامر]
cs8 = '.ت بوتات' # - تكدر تكتب الي يعجبك لتغير [الامر]
cs9 = '.ت الكل' # - تكدر تكتب الي يعجبك لتغير [الامر]
async def G4(goldX):
    if goldX.sender_id != G3:
        return False
    return True
async def Golden1(G7,G8,G9,rrrrrF):
    with open(G7,'w',encoding='utf-8') as f:
        for G26 in G8:
            f.write(f"{G26}\n")
    await rrrrrF.respond(file=G7,message=f"{G9} - {len(G8)}")
    os.remove(G7)
@Golden.on(events.NewMessage(pattern=f'{cs1}'))
async def Golden2(rrrrrF):
    if not await G4(rrrrrF):
        return
    G10 = 0
    G11 = await rrrrrF.respond('**♻️ - انتــضر**')
    async for dialog in Golden.iter_dialogs():
        if dialog.is_channel:
            try:
                await Golden(LeaveChannelRequest(dialog.entity))
                G10 += 1
                await G11.edit(f'**✅ - {G10}**')
            except:
                await G11.edit(f'**❌ - {G10}**')
    await G11.edit(f'✅ - {G10}')
@Golden.on(events.NewMessage(pattern=f'{cs2}'))
async def Golden3(rrrrrF):
    if not await G4(rrrrrF):
        return
    G12 = 0
    G13 = await rrrrrF.respond('**♻️ - انــــتضر .**')
    async for dialog in Golden.iter_dialogs():
        if dialog.is_group:
            try:
                await Golden(LeaveChannelRequest(dialog.entity))
                G12 += 1
                await G13.edit(f'**✅ - {G12}**')
            except:
                await G13.edit(f'**❌ - {G12}**')
    await G13.edit(f'**✅ - {G12}**')
@Golden.on(events.NewMessage(pattern=f'{cs3}'))
async def Golden4(rrrrrF):
    if not await G4(rrrrrF):
        return
    G14 = 0
    G15 = await rrrrrF.respond('**♻️ - انــــتضر .**')
    async for dialog in Golden.iter_dialogs():
        if getattr(dialog.entity,'bot',False):
            try:
                await Golden(LeaveChannelRequest(dialog.entity))
                G14 += 1
                await G15.edit(f'**✅ - {G14}**')
            except:
                await G15.edit(f'**❌ - {G14}**')
    await G15.edit(f'**✅ - {G14}**')
@Golden.on(events.NewMessage(pattern=f'{cs4}'))
async def Golden5(rrrrrF):
    if not await G4(rrrrrF):
        return
    contacts = []
    G17 = await rrrrrF.respond('**♻️ - انــــتضر .**')
    async for dialog in Golden.iter_dialogs():
        if dialog.is_user:
            contacts.append(dialog.entity.id)
            try:
                await Golden(DeleteHistoryRequest(peer=dialog.entity,max_id=0))
            except:
                pass
    for contact_id in contacts:
        try:
            await Golden(DeleteContactsRequest([InputPeerUser(user_id=contact_id,access_hash=0)]))
        except:
            pass
    await G17.edit(f'**✅ - {len(contacts)}**')
@Golden.on(events.NewMessage(pattern=f'{cs5}'))
async def Golden6(rrrrrF):
    if not await G4(rrrrrF):
        return
    sh1 = 0
    sh2 = 0
    sh3 = 0
    sh4 = 0
    G18 = await rrrrrF.respond('**♻️ - انــــتضر .**')
    async for dialog in Golden.iter_dialogs():
        if dialog.is_channel or dialog.is_group or getattr(dialog.entity,'bot',False):
            try:
                await Golden(LeaveChannelRequest(dialog.entity))
                if dialog.is_channel:
                    sh1 += 1
                elif dialog.is_group:
                    sh2 += 1
                elif getattr(dialog.entity,'bot',False):
                    sh3 += 1
            except:
                pass
        
        if dialog.is_user:
            try:
                await Golden(DeleteHistoryRequest(peer=dialog.entity,max_id=0))
                await Golden(DeleteContactsRequest([InputPeerUser(user_id=dialog.entity.id,access_hash=0)]))
                sh4 += 1
            except:
                pass
    await G18.edit(f'**✅ - تم الــنظيف .\n**الــقنوات - **`{sh1}`\n**الــكروبات -** `{sh2}`\n**البــوتات -** `{sh3}`\n**الــناس -** `{sh4}`**')
@Golden.on(events.NewMessage(pattern=f'{cs6}'))
async def Golden7(rrrrrF):
    if not await G4(rrrrrF):
        return
    G19 = []
    G20 = await rrrrrF.respond('**♻️ - انــــتضر .**')
    async for dialog in Golden.iter_dialogs():
        if dialog.is_channel:
            G21 = dialog.entity.username or dialog.entity.id
            G19.append(f"@{G21}" if dialog.entity.username else f"{G21}")
    await Golden1('قنوات.txt',G19,'تم تخزين القنوات بنجاح',rrrrrF)
@Golden.on(events.NewMessage(pattern=f'{cs7}'))
async def Golden8(rrrrrF):
    if not await G4(rrrrrF):
        return
    G22 = []
    G23 = await rrrrrF.respond('**♻️ - انــــتضر .**')
    async for dialog in Golden.iter_dialogs():
        if dialog.is_group:
            G24 = getattr(dialog.entity,'username',None)
            G25 = dialog.entity.title
            G26 = f"@{G24}" if G24 else f"{G25} (ID: {dialog.entity.id})"
            G22.append(G26)
    await Golden1('كروبات.txt',G22,'**✅ - Done**',rrrrrF)
@Golden.on(events.NewMessage(pattern=f'{cs8}'))
async def Golden9(rrrrrF):
    if not await G4(rrrrrF):
        return
    G27 = []
    G28 = await rrrrrF.respond('**♻️ - انــــتضر .**')
    async for dialog in Golden.iter_dialogs():
        if getattr(dialog.entity,'bot',False):
            G21 = dialog.entity.username or dialog.entity.id
            G27.append(f"@{G21}" if dialog.entity.username else f"{G21}")
    await Golden1('بوتات.txt',G27,'**✅ - Done**',rrrrrF)
@Golden.on(events.NewMessage(pattern=f'{cs9}'))
async def Golden10(rrrrrF):
    if not await G4(rrrrrF):
        return
    G29 = []
    G30 = 0
    G31 = 0
    G32 = 0
    G33 = await rrrrrF.respond('**♻️ - انــــتضر .**')
    async for dialog in Golden.iter_dialogs():
        G34 = getattr(dialog.entity,'username',None)
        G35 = f"@{G34}" if G34 else f"{dialog.entity.id}"
        if dialog.is_channel:
            G29.append(G35)
            G30 += 1
        elif dialog.is_group:
            G25 = dialog.entity.title
            G29.append(f"{G25} - {dialog.entity.id}")
            G31 += 1
        elif getattr(dialog.entity,'bot',False):
            G29.append(G35)
            G32 += 1
    await Golden1('كلشي.txt',G29,'**✅ - Done**',rrrrrF)
Golden.start()
Golden.run_until_disconnected()
