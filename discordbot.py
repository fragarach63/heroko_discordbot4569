import discord
import googletrans
import time
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
    if message.content == '我好帥喔':
        #然後回傳訊息
        await message.channel.send('不好意思，不要騙人啦')

    elif message.content == '你好':
        #然後回傳訊息
        await message.channel.send('哈囉肥宅')
        
    elif message.content == '哭':
        #然後回傳訊息
        await message.channel.send('不哭不哭眼淚是珍珠~')
        
    elif message.content == '兇':
        #然後回傳訊息
        await message.channel.send('我就兇怎樣')
        
    elif message.content == '.':
        #然後回傳訊息
        await message.channel.send('點屁啊點，只會點點點喔')
        
    elif message.content == '幹':
        #然後回傳訊息
        await message.channel.send('沒事~幹只是語助詞~盡量罵~~')
        
    elif message.content == '召喚':
        #然後回傳訊息
        await message.channel.send('召喚成功，請稍等~')
        
    elif message.content == '@':
        #然後回傳訊息
        await message.channel.send('召喚失敗，跟你一樣~')

    #如果以「說」開頭
    elif message.content.startswith('說'):
      #分割訊息成兩份
      tmp = message.content.split(" ",2)
      #如果分割後串列長度只有1
      if len(tmp) == 1:
        await message.channel.send("你要我說什麼啦？")
      else:
        await message.channel.send(tmp[1])

    elif client.user in message.mentions: # @判定
        translator = googletrans.Translator()
        robotName = client.user.name
        first, space, content = message.clean_content.partition('@'+robotName+' ')

        if content == '':
            content = first
        if translator.detect(content).lang == DSTLanguage:
            return
        if translator.detect(content).lang == SRCLanguage or SRCLanguage == '':
            remessage = translator.translate(content, dest='zh-tw').text
            await message.reply(remessage)



client.run(TOKEN)
