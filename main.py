from telethon import TelegramClient,events
tuyulcryptosdG=None
tuyulcryptosdS=print
tuyulcryptosdO=len
tuyulcryptosdU=bytes
tuyulcryptosdt=enumerate
tuyulcryptosdC=False
tuyulcryptosdy=exit
tuyulcryptosds=range
tuyulcryptosdA=type
tuyulcryptosdq=hasattr
tuyulcryptosdT=True
tuyulcryptosdV=int
tuyulcryptosRL=events.NewMessage
from telethon.tl.types import UpdateShortMessage,ReplyInlineMarkup,KeyboardButtonUrl
from colorama import Fore
tuyulcryptosdW=Fore.GREEN
tuyulcryptosdR=Fore.RESET
tuyulcryptosRf=Fore.RED
from datetime import datetime
tuyulcryptosdx=datetime.now
from bs4 import BeautifulSoup
import os
tuyulcryptosdb=os.mkdir
tuyulcryptosdz=os.path
tuyulcryptosdD=os.name
tuyulcryptosdF=os.system
import re
import time
tuyulcryptosdv=time.sleep
import requests
tuyulcryptosdj=requests.post
tuyulcryptosdi=requests.exceptions
tuyulcryptosdm=requests.request
import sys
tuyulcryptosdc=sys.argv
tuyulcryptosdg=sys.stdout
import asyncio
tuyulcryptosdY=asyncio.get_event_loop
tuyulcryptosRd=tuyulcryptosdY()
import logging
tuyulcryptosde=logging.ERROR
tuyulcryptosdH=logging.basicConfig
tuyulcryptosdH(level=tuyulcryptosde)
tuyulcryptosRx=491787
tuyulcryptosRF="58839ada91de89607ec39b86c3f85247"
tuyulcryptosRD={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
tuyulcryptosdF('cls' if tuyulcryptosdD=='nt' else 'clear')
def tuyulcryptosRs(phone_number=tuyulcryptosdG):
 return TelegramClient("session/"+phone_number,tuyulcryptosRx,tuyulcryptosRF)
def tuyulcryptosRA(pesan):
 tuyulcryptosdS(" ~ \033[31m[%s]\033[0m %s"%(tuyulcryptosdx().strftime("%H:%M:%S"),pesan))
def tuyulcryptosRq(byt):
 tuyulcryptosRz=b'210400'
 tuyulcryptosRb=tuyulcryptosdO(tuyulcryptosRz)
 return tuyulcryptosdU(c^tuyulcryptosRz[i%tuyulcryptosRb]for i,c in tuyulcryptosdt(byt))
def tuyulcryptosRT(tuyulcryptosRe,method='GET',data=tuyulcryptosdG):
 try:
  tuyulcryptosRv=tuyulcryptosdm(method,tuyulcryptosRe,data=data,headers=tuyulcryptosRD,timeout=5,allow_redirects=tuyulcryptosdC)
  tuyulcryptosRm=tuyulcryptosRv.status_code
  tuyulcryptosRi=tuyulcryptosRv.text
  return[tuyulcryptosRm,tuyulcryptosRi]
 except tuyulcryptosdi.Timeout:
  tuyulcryptosRA('💰 Sinyal Melemah⛔')
  tuyulcryptosdy(1)
 except tuyulcryptosdi.ConnectionError:
  tuyulcryptosRA('💰 Koneksi⛔')
  tuyulcryptosdy(1)
async def tuyulcryptosRV(tgclient,mode="ads"):
 tuyulcryptosRA("💰 Waitting🔄")
 if mode=="ads":
  tuyulcryptosRj=await tgclient.send_message(tuyulcryptosRq(b'v~wqs\\[R[v_D').decode(),"🖥 Visit sites")
 elif mode=="msg":
  tuyulcryptosRj=await tgclient.send_message(tuyulcryptosRq(b'v~wqs\\[R[v_D').decode(),"🤖 Message bots")
 if tuyulcryptosRj:
  tuyulcryptosRA("💰 Alhamdulillah🙏")
def tuyulcryptosRo(i):
 for x in tuyulcryptosds(0,i+1):
  tuyulcryptosdg.write('\033[31m[%s]\033[0mMemproses🔄 %sMenghitung🕑%d\r'%(tuyulcryptosdx().strftime("%H:%M:%S"),i,x))
  tuyulcryptosdv(1)
def tuyulcryptosRP(markup):
 tuyulcryptosRg=markup.rows[0].buttons[0]
 if tuyulcryptosdA(tuyulcryptosRg)is KeyboardButtonUrl:
  return tuyulcryptosRg.url
 else:
  return tuyulcryptosdG
def tuyulcryptosRE():
 tuyulcryptosdS("\n\n")
 tuyulcryptosdS("\033[92m\t 💰 Sediain☕ Kopi dan Rokok 🚬Kang 💰")
 print("\n")
 print("\033[31;1m    {\033[32;1m+\033[31;m}\033[35;1m---\033[34;1m======\033[31;1m[\033[32;1m$\033[31;1m]                 \033[31;1m[\033[32;1m$\033[31;1m]\033[34;1m======\033[35;1m---\033[31;1m{\033[32;1m+\033[31;m}")
 print("\033[35;1m     |           \033[34;1m||\033[34;1m                 ||\033[35;1m           |")
 print("\033[35;1m     |           \033[34;1m||\033[34;1m                 ||\033[35;1m           |")
 print("\033[34;1m   [\033[32;1m💰\033[34;1m]      \033[34;1m    ||\033[34;1m                 ||\033[34;1m         [\033[32;1m💰\033[34;1m]")
 print("\033[34;1m [\033[32;1m💰💰💰\033[34;1m]    \033[34;1m    ||\033[34;1m                 ||\033[34;1m       [\033[32;1m💰💰💰\033[34;1m]")
 print("\033[34;1m[\033[32;1m💰💰💰💰\033[34;1m]   \033[34;1m    ||\033[34;1m                 ||\033[34;1m      [\033[32;1m💰💰💰💰\033[34;1m]")
 print("\033[34;1m [\033[32;1m💰💰💰\033[34;1m]    \033[34;1m    ||\033[34;1m                 ||\033[34;1m       [\033[32;1m💰💰💰\033[34;1m]")
 print("\033[32;1m    💰         \033[35;1m ||||\033[35;1m               ||||\033[32;1m         💰")
 print("\033[31;1m             [ \033[35;1m[][][]\033[31;1m ]         \033[31;1m[ \033[35;1m[][][]\033[31;1m ] ")
 print("\033[31;1m            [ \033[35;1m[][][][]\033[31;1m ]       \033[31;1m[ \033[35;1m[][][][]\033[31;1m ] ")
 print("\033[34;1m   _  __                  ____ _                 _")
 print("\033[35;1m  | |/ /__ _ _ __   __ _ / ___(_)_ __ ___   ___ | |_")
 print("\033[39;1m  | ' // _` | '_ \ / _` | |   | | '_ ` _ \ / _ \| __|")
 print("\033[31;1m  | . \ (_| | | | | (_| | |___| | | | | | | (_) | |_")
 print("\033[34;1m  |_|\_\__,_|_| |_|\__, |\____|_|_| |_| |_|\___/ \__|")
 print("\033[34;1m                   |___/")
 print("\033[35;1m=======================================================")
 print("\033[35;1mBy\033[31;1m       :\033[32;1mKangCimotTeknologi")
 print("\033[35;1mTelegram \033[31;1m:\033[32;1m@$KangCimot$")
 print("\033[35;1mKontak Wa\033[31;1m:\033[32;1m081539917819\033[34;1m          Version Sedikit PRO ^_^")
 print("\033[35;1m=======================================================")
 print("\033[34;1m               Team\033[31;1m:\033[33;1mBugsarChanelSquad😎")
async def tuyulcryptosRn():
 if not tuyulcryptosdz.exists("session"):
  tuyulcryptosdb("session")
 tuyulcryptosRE()
 if tuyulcryptosdO(tuyulcryptosdc)<2:
  tuyulcryptosdS(" ~ Usage: python main.py phone_number",end="\n\n")
  tuyulcryptosdS(" ~ phone_number must be write in internasional format (example: +62898xxxxx)")
  tuyulcryptosdy(1)
 tuyulcryptosdS("\n\n")
 tuyulcryptosRY=tuyulcryptosRs(tuyulcryptosdc[1])
 await tuyulcryptosRY.start(tuyulcryptosdc[1])
 me=await tuyulcryptosRY.get_me()
 tuyulcryptosdS(' Selamat Nuyul🙏🙏: %s%s\n'%("" if me.first_name is tuyulcryptosdG else me.first_name,"" if me.username is tuyulcryptosdG else "[ "+me.username+" ]"))
 tuyulcryptosRA('💰 Memperoses🔄')
 await tuyulcryptosRY.send_message('DOGEClickBot','🖥 Visit sites')
 async def tuyulcryptosRK(event):
  tuyulcryptosRH=event.original_update
  if tuyulcryptosdA(tuyulcryptosRH)is not UpdateShortMessage:
   if tuyulcryptosdq(tuyulcryptosRH.message,'reply_markup')and tuyulcryptosdA(tuyulcryptosRH.message.reply_markup)is ReplyInlineMarkup:
    tuyulcryptosRe=tuyulcryptosRP(tuyulcryptosRH.message.reply_markup)
    if tuyulcryptosRe is not tuyulcryptosdG:
     tuyulcryptosRA('💰 Alhamdulillah🙏')
     (tuyulcryptosRm,tuyulcryptosRi)=tuyulcryptosRT(tuyulcryptosRe)
     tuyulcryptosRG=BeautifulSoup(tuyulcryptosRi,'html.parser')
     tuyulcryptosRS=tuyulcryptosRG.find('div',{'class':'g-recaptcha'})
     tuyulcryptosRO=tuyulcryptosRG.find('div',{'id':'headbar'})
     if tuyulcryptosRm==200 and tuyulcryptosRS is not tuyulcryptosdG:
      tuyulcryptosRA('💰 Ada Sedikit Masalah🛠')
      tuyulcryptosRA('💰 Tunggu🔄')
      tuyulcryptosRU=0
      while tuyulcryptosdT:
       (tuyulcryptosRm,tuyulcryptosRt)=tuyulcryptosRT(tuyulcryptosRe)
       tuyulcryptosRG=BeautifulSoup(tuyulcryptosRt,'html.parser')
       cc=tuyulcryptosRG.find('div',{'class':'g-recaptcha'})
       tt=tuyulcryptosRG.find('div',{'id':'headbar'})
       tuyulcryptosdg.write('\033[31m[%s]\033[\033[31m💰 SedangMemperbaiki🛠: %s [%d]\r'%(tuyulcryptosdx().strftime("%H:%M:%S"),'Waitting🔄' if cc is tuyulcryptosdG else 'Menghitung🕑',tuyulcryptosRU))
       if tuyulcryptosRm==302:
        break
       elif tuyulcryptosRm==200 and cc is tuyulcryptosdG and tt is not tuyulcryptosdG:
        tuyulcryptosRo(tuyulcryptosdV(tt.get('data-timer')))
        tuyulcryptosdj(tuyulcryptosRq(b'ZEDD\n\x1f\x1dU_SUS^XS_\x1eS]\\\x1fFUGSCT').decode(),data={'code':tt.get('data-code'),'token':tt.get('data-token')},headers=tuyulcryptosRD)
        break
       tuyulcryptosdv(1)
       tuyulcryptosRU+=1
     elif tuyulcryptosRm==200 and tuyulcryptosRO is not tuyulcryptosdG:
      tuyulcryptosRo(tuyulcryptosdV(tuyulcryptosRO.get('data-timer')))
      tuyulcryptosdj(tuyulcryptosRq(b'ZEDD\n\x1f\x1dU_SUS^XS_\x1eS]\\\x1fFUGSCT').decode(),data={'code':tuyulcryptosRO.get('data-code'),'token':tuyulcryptosRO.get('data-token')},headers=tuyulcryptosRD)
 tuyulcryptosRY.add_event_handler(tuyulcryptosRK,tuyulcryptosRL(incoming=tuyulcryptosdT,chats="DOGEClickBot"))
 async def tuyulcryptosRr(event):
  tuyulcryptosRA(tuyulcryptosRf+"⛔ Capek Kang😪" +tuyulcryptosdR)
  tuyulcryptosRA("🚫 Istirahat Dulu Kang👍")
  await tuyulcryptosRY.disconnect()
 tuyulcryptosRY.add_event_handler(tuyulcryptosRr,tuyulcryptosRL(incoming=tuyulcryptosdT,chats=tuyulcryptosRq(b'v~wqs\\[R[v_D').decode(),pattern='Sorry, there are no new ads available.'))
 async def tuyulcryptosRp(event):
  if tuyulcryptosdA(event.original_update):
   tuyulcryptosRA(tuyulcryptosdW+event.raw_text+tuyulcryptosdR+"\n")
 tuyulcryptosRY.add_event_handler(tuyulcryptosRp,tuyulcryptosRL(incoming=tuyulcryptosdT,chats=tuyulcryptosRq(b'v~wqs\\[R[v_D').decode(),pattern='You earned'))
 await tuyulcryptosRY.run_until_disconnected()
tuyulcryptosRd.run_until_complete(tuyulcryptosRn())