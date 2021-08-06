import discord
import googletrans
import os
from pprint import pprint
# 輸入自己Bot的TOKEN碼
TOKEN = os.environ['TOKEN']
SRCLanguage=os.environ['SRC']
DSTLanguage=os.environ['DST']

client = discord.Client()

# 起動時呼叫
@client.event
async def on_ready():
    print('成功登入')

# 收到訊息時呼叫
@client.event
async def on_message(message):
    # 送信者為Bot時無視
    
if message.author == client.user:
        return
    #如果以「說」開頭
    if message.content.startswith('說'):
      #分割訊息成兩份
      tmp = message.content.split(" ",2)
      #如果分割後串列長度只有1
      if len(tmp) == 1:
        await message.channel.send("你要我說什麼啦？")
      else:
        await message.channel.send(tmp[1])
    
     
    
            
client.run(TOKEN)
