#SNEHABHI USERTAGGER BOT
#I LOVE YOU SNEHUπ

import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
  level=logging.INFO,
  format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

moment_worker = []

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global moment_worker
  moment_worker.remove(event.chat_id)
  
@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("π·π΄π»π»πΎ πΈ'πΌ ππ½π΄π·π°π±π·πΈ πππ΄πππ°πΆπΆπ΄π π±πΎπ.πΌπ°π³π΄ ππΈππ· π»πΎπ± π±π [ABHI & SNEHU](HTTP://T.ME/SNEHABHI_UPDATES). π½π΄π΄π³ π·π΄π»πΏ /help . π΅πΎπ ππ΄πΏπΎ /repository ",
                    buttons=(
                      [Button.url('π πΆππΎππΏ πΌπ΄ π³π°π» π³π΄ π³π΄πΊπ· πΌπ π₯Ίβ¨', 'https://t.me/SNEHABHI_TAGGERBOT?startgroup=true')],
                      [Button.url('π΅πΎπ π°π½π πΈππππ΄ πΉπΎπΈπ½ πΎππ πππΏπΏπΎππ πΆππΎππΏ', 'https://t.me/SNEHABHI_SERVER')],
                      [Button.url('π΅πΎπ π»π°ππ΄ππ ππΏπ³π°ππ΄π πΉπΎπΈπ½ πΎππ π²π·π°π½π½π΄π»', 'https://t.me/SNEHABHI_UPDATES')]
                      ),
                    link_preview=False
                    )



@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "***ππ½π΄π·π°π±π·πΈ πππ΄πππ°πΆπΆπ΄π π±πΎπ'π π·π΄π»πΏ πΌπ΄π½π**\n\nCommand: /tag \n ππΎπ π²π°π½ πππ΄ ππ·πΈπ π²πΎπΌπΌπ°π½π³ ππΈππ· ππ΄ππ ππΎπ ππ°π½π ππΎ ππ΄π»π» πΎππ·π΄ππ. \n`π΄ππ°πΌπΏπ»π΄: /tag πΆπΎπΎπ³ πΌπΎππ½πΈπ½πΆ!` \nππΎπ π²π°π½ πππ΄ ππ·πΈπ π²πΎπΌπΌπ°π½π³ π°π π°π½ π°π½πππ΄π. π°π½π πΌππΆ π±πΎπ ππΈπ»π» ππ°πΆ πππ΄ππ ππΎ ππ΄πΏπ»πΈπ΄π³ πΌππΆ"
  await event.reply(helptext,
                    buttons=(
                      [Button.url('π πΆππΎππΏ πΌπ΄ π³π°π» π³π΄ π³π΄πΊπ· πΌπ π₯Ίβ¨', 'https://t.me/SNEHABHI_TAGGERBOT?startgroup=true')],
                      [Button.url('π΅πΎπ π°π½π πΈππππ΄ πΉπΎπΈπ½ πΎππ πππΏπΏπΎππ πΆππΎππΏ', 'https://t.me/SNEHABHI_SERVER')],
                      [Button.url('π΅πΎπ π»π°ππ΄ππ ππΏπ³π°ππ΄π πΉπΎπΈπ½ πΎππ π²π·π°π½π½π΄π»', 'https://t.me/SNEHABHI_UPDATES')]
                      ),
                    link_preview=False
                    )
  
@client.on(events.NewMessage(pattern="^/repository$"))
async def repository(event):
  snehabhitext = "**π³π΄πΏπ»πΎπ πΎππ πΎππ½ π±πΎπ**"
  await event.reply(snehabhitext,
                    buttons=(
                      [Button.url('ππ΄πΏπΎππΈππΎππ', 'http://t.me/SNEHABHI_UPDATES')],
                      [Button.url('πΌπ°πππΈ πΆππΎππΏ', 'http://t.me/LIVE_LIFE_LIKE')]
                      ),
                    link_preview=False
                    )
  
#ππ°π°π· π±π·π°πΈπΌππ° π΅ππ»π» πΈπΌπΆπ½πΎππ΄π±π°ππΈ

#π²ππ΄π³πΈπ π³π΄ π³π΄π½π° ππ°ππ½π° πΌπ° π²π·πΎπ³ π³π΄π½πΆπ΄

@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global moment_worker
  if event.is_private:
    return await event.reply("πππ΄ ππ·πΈπ πΈπ½ π²π·π°π½π½π΄π» πΎπ πΆππΎππΏπ!")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.reply("πΎπ½π»π π°π³πΌπΈπ½ π²π°π½ πππ΄ πΈπ.")
    
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.reply("πΈ π²π°π½'π πΌπ΄π½ππΈπΎπ½ πΌπ΄πΌπ±π΄ππ π΅πΎπ πΎπ»π³ πΏπΎππ")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.reply("πΆπΈππ΄ πΌπ΄ π²π°π½ π°π½ π°ππΆππΌπ΄π½π. π΄ππ°πΌπΏπ»π΄: `/tag πΊπ°π·π° πΌπ°π ππ°π·π΄ π·πΎ ππ°π±`")
  else:
    return await event.reply("ππ΄πΏπ»π ππΎ πΌππΆ πΎπ πΆπΈππ΄ ππΎπΌπ΄ ππ΄ππ ππΎ πΌπ΄π½ππΈπΎπ½!")
  if mode == "text_on_cmd":
    moment_worker.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in moment_worker:
        await event.respond("πππΎπΏπΏπ΄π³! πΉπΎπΈπ½ @SNEHABHI_UPDATES.. & @LIVE_LIFE_LIKE..")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
        
  if mode == "text_on_reply":
    moment_worker.append(event.chat_id)
    
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in moment_worker:
        await event.reply("πππΎπΏπΏπ΄π³! πΉπΎπΈπ½ @SNEHABHI_UPDATES")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
        
print("ππ½π΄π·π°π±π·πΈ πππ΄πππ°πΆπΆπ΄π π±πΎπ πΈπ πππ°πππ΄π³")
print("Β―\_(γ)_/Β― π½π΄π΄π³ π·π΄π»πΏ πΉπΎπΈπ½ @SNEHABHI_SERVER")
client.run_until_disconnected()
