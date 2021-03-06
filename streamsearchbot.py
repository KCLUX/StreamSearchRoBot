import requests
from youtubesearchpython import SearchVideos
from telegraph import Telegraph
from telethon.tl.types import InputWebDocument
from telethon import TelegramClient, events
from telethon import custom, events, Button
import re
import urllib
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from Configs import Config
from loggers import logging
import os
import re
from math import ceil
import requests
import telethon
from telethon import Button, custom, events, functions
bot = TelegramClient("bot", api_id=Config.API_ID, api_hash=Config.API_HASH)
torrentbot = bot.start(bot_token=Config.BOT_TOKEN)


@torrentbot.on(events.NewMessage(pattern="^/start$"))
async def search(event):
    replied_user = await event.client(GetFullUserRequest(event.sender_id))
    firstname = replied_user.user.first_name
    await event.reply(message=f"Hai, **{firstname}**, Selamat datang dan selamat menggunakan YtMagnet Search Bot untuk MirrorGroup.",
                      buttons=[
                      [Button.switch_inline("Video Youtube", query="yt ", same_peer=True)],
                      [Button.switch_inline("MP3 Youtube", query="ytmp3 ", same_peer=True)],
                      [Button.switch_inline("Magnet Torrent", query="torrent ", same_peer=True)],
                      [Button.url("Grup MVPL", f"t.me/idmvpl")],
                              ]
                     )
@torrentbot.on(events.NewMessage(pattern="^/mvpl$"))
async def search(event):
    await event.reply('**Saluran Kami:**\nš @movieplaylist (stream - off)\nš @newmvpl (raw&4k - on)\nš @idmvpl (groups gateway - on)\nš @mvplbackup (gdl - on)\nš @open_signup (pt open signup - on)\nš @mvplid (whatson - idle)', parse_mode="HTML") torrentbot.on(events.NewMessage(pattern="^/donasi$"))
async def search(event):
    await event.reply('Silahkan PM ke @memeriksausername', parse_mode="HTML")
      
@torrentbot.on(events.InlineQuery(pattern=r"torrent (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    testinput = event.pattern_match.group(1)
    starkisnub = urllib.parse.quote_plus(testinput)
    results = []
    sedlyf = "https://api.sumanjay.cf/torrent/?query=" + starkisnub
    try:
        okpro = requests.get(url=sedlyf, timeout=10).json()
    except:
        pass
    sed = len(okpro)
    if sed == 0:
        resultm = builder.article(
                title="Tidak menemukan apapun",
                description="Cek ejaan atau gunakan kata kunci lain",
                text="**Silahkan dicoba lagi dengan kata kunci yang tepat**",
                buttons=[
                      [Button.switch_inline("Cari lagi", query="torrent ", same_peer=True)],
                      [Button.switch_inline("Video Youtube", query="yt ", same_peer=True)],
                      [Button.switch_inline("MP3 Youtube", query="ytmp3 ", same_peer=True)],
                      [Button.switch_inline("Magnet Torrent", query="torrent ", same_peer=True)],
                      [Button.url("Grup MVPL", f"t.me/idmvpl")],
                              
                      ]
            )
        await event.answer([resultm])
        return
    if sed > 30:
        for i in range(30):
            seds = okpro[i]["age"]
            okpros = okpro[i]["leecher"]
            sadstark = okpro[i]["magnet"]
            okiknow = okpro[i]["name"]
            starksize = okpro[i]["size"]
            starky = okpro[i]["type"]
            seeders = okpro[i]["seeder"]
            okayz = (f"/mirror {sadstark}")
            sedme = f"Size : {starksize} Type : {starky} Age : {seds}"
            results.append(await event.builder.article(
                title=okiknow,
                description=sedme,
                text=okayz,
                buttons=[
                [Button.switch_inline("Cari lagi", query="torrent ", same_peer=True)],
                [Button.switch_inline("Video Youtube", query="yt ", same_peer=True)],
                [Button.switch_inline("MP3 Youtube", query="ytmp3 ", same_peer=True)],
                [Button.switch_inline("Magnet Torrent", query="torrent ", same_peer=True)],
                [Button.url("Grup MVPL", f"t.me/idmvpl")],
                ]
            )
                               )
    else:
        for sedz in okpro:
            seds = sedz["age"]
            okpros = sedz["leecher"]
            sadstark = sedz["magnet"]
            okiknow = sedz["name"]
            starksize = sedz["size"]
            starky = sedz["type"]
            seeders = sedz["seeder"]
            okayz = (f"/mirror {sadstark}")
            sedme = f"Size : {starksize} Type : {starky} Age : {seds}"
            results.append(await event.builder.article(
                title=okiknow,
                description=sedme,
                text=okayz,
                buttons= [
                  [Button.switch_inline("Cari lagi", query="torrent ", same_peer=True)],
                  [Button.switch_inline("Video Youtube", query="yt ", same_peer=True)],
                  [Button.switch_inline("MP3 Youtube", query="ytmp3 ", same_peer=True)],
                  [Button.switch_inline("Magnet Torrent", query="torrent ", same_peer=True)],
                  [Button.url("Grup MVPL", f"t.me/idmvpl")],
                              ]
            ))
    await event.answer(results)


@torrentbot.on(events.InlineQuery(pattern=r"yt (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    testinput = event.pattern_match.group(1)
    starkisnub = urllib.parse.quote_plus(testinput)
    results = []
    search = SearchVideos(f"{testinput}", offset=1, mode="dict", max_results=20)
    mi = search.result()
    moi = mi["search_result"]
    if search == None:
        resultm = builder.article(
        		title="Tidak menemukan apapun",
                description="Cek ejaan atau gunakan kata kunci lain",
                text="**Silahkan dicoba lagi dengan kata kunci yang tepat**",
                buttons=[
                      [Button.switch_inline("Cari lagi", query="yt ", same_peer=True)],
                      [Button.switch_inline("Video Youtube", query="yt ", same_peer=True)],
                      [Button.switch_inline("MP3 Youtube", query="ytmp3 ", same_peer=True)],
                      [Button.switch_inline("Magnet Torrent", query="torrent ", same_peer=True)],
                      [Button.url("Grup MVPL", f"t.me/idmvpl")],
                              ]
            )
        await event.answer([resultm])
        return
    for mio in moi:
        mo = mio["link"]
        thum = mio["title"]
        fridayz = mio["id"]
        thums = mio["channel"]
        td = mio["duration"]
        tw = mio["views"]
        kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
        okayz = (f"/watch {mo}")
        hmmkek = f'Channel : {thums} \nDuration : {td} \nViews : {tw}'
        results.append(await event.builder.article(
                title=thum,
                description=hmmkek,
                text=okayz,
                buttons= [
                [Button.switch_inline("Cari lagi", query="torrent ", same_peer=True)],
                [Button.switch_inline("Video Youtube", query="yt ", same_peer=True)],
                [Button.switch_inline("MP3 Youtube", query="ytmp3 ", same_peer=True)],
                [Button.switch_inline("Magnet Torrent", query="torrent ", same_peer=True)],
                [Button.url("Grup MVPL", f"t.me/idmvpl")],
                              ]
            )
                               )
    await event.answer(results)

@torrentbot.on(events.InlineQuery(pattern=r"ytmp3 (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    testinput = event.pattern_match.group(1)
    starkisnub = urllib.parse.quote_plus(testinput)
    results = []
    search = SearchVideos(f"{testinput}", offset=1, mode="dict", max_results=20)
    mi = search.result()
    moi = mi["search_result"]
    if search == None:
        resultm = builder.article(
        		title="Tidak menemukan apapun",
                description="Cek ejaan atau gunakan kata kunci lain",
                text="**Silahkan dicoba lagi dengan kata kunci yang tepat**",
                buttons=[
                      [Button.switch_inline("Cari lagi", query="ytmp3 ", same_peer=True)],
                      [Button.switch_inline("Video Youtube", query="yt ", same_peer=True)],
                      [Button.switch_inline("MP3 Youtube", query="ytmp3 ", same_peer=True)],
                      [Button.switch_inline("Magnet Torrent", query="torrent ", same_peer=True)],
                      [Button.url("Grup MVPL", f"t.me/idmvpl")],
                              ]
            )
        await event.answer([resultm])
        return
    for mio in moi:
        mo = mio["link"]
        thum = mio["title"]
        fridayz = mio["id"]
        thums = mio["channel"]
        td = mio["duration"]
        tw = mio["views"]
        kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
        okayz = (f"/watch {mo} audio")
        hmmkek = f'Channel : {thums} \nDuration : {td} \nViews : {tw}'
        results.append(await event.builder.article(
                title=thum,
                description=hmmkek,
                text=okayz,
                buttons= [
                  [Button.switch_inline("Cari lagi", query="ytmp3 ", same_peer=True)],
                  [Button.switch_inline("Video Youtube", query="yt ", same_peer=True)],
                  [Button.switch_inline("MP3 Youtube", query="ytmp3 ", same_peer=True)],
                  [Button.switch_inline("Magnet Torrent", query="torrent ", same_peer=True)],
                  [Button.url("Grup MVPL", f"t.me/idmvpl")],
                                  ]
            )
                               )
    await event.answer(results)
 
    
@torrentbot.on(events.InlineQuery)  # pylint:disable=E0602
async def inline_handler(event):
        builder = event.builder
        query = event.text
        replied_user = await torrentbot.get_me()
        firstname = replied_user.username
        if query == None or " ": 
            resulte = builder.article(
                title="Turoial cara menggunakan BOT",
                description="2021 Ā© MVPL",
                text=f"**Bagaimana cara menggunakannya?** \n**š Youtube:**\n `@{firstname} yt <kata kunci>` \n**Contoh :** `@{firstname} yt lagu indonesia raya` \n\nš **MP3 Youtube:**\n `@{firstname} ytmp3 <kata kunci>` \n**Contoh :**\n `@{firstname} ytmp3 lagu indonesia raya` \n\nš **Torrent: **\n `@{firstname} torrent <kata kunci>` \n**Contoh :** `@{firstname} torrent the raid`",
                buttons=[
                      [Button.url("Grup MVPL", f"t.me/idmvpl")],
                      [Button.switch_inline("Cari Video Youtube", query="yt ", same_peer=True)],
                      [Button.switch_inline("Cari MP3 Youtube", query="ytmp3 ", same_peer=True)],
                      [Button.switch_inline("Cari Magnet Torrent", query="torrent ", same_peer=True)]
                ]
                             
            )
            await event.answer([resulte])
print("Bot berfungsi!")
def startbot():
    torrentbot.run_until_disconnected()


if __name__ == "__main__":
    startbot()
