import discord
import os
from keep_alive import keep_alive
import random
client = discord.Client()
from notification import Notification 
#notification bot, takes in chat id and client
notif = Notification(client, 785705961032515614 )
#test 912532987671900180
#test2 791804582442434590
#actual 785705961032515614

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=": ~commands"))
  notif.start()


#if message is recieved
@client.event
async def on_message(message):
  #if bot message, ignore
  if message.author == client.user:
    return
  #if message contains welcome in it, say hi! 
  #if 'welcome' in message.content.lower():
   # await message.channel.send('<:hiya:807336709993529374>')
  if message.content.lower() == "hi rei":
    await message.channel.send('Hey!')
  if "rei you seeing this shit?" in message.content.lower():
    await message.channel.send('<:ReiStare:887162572963475506>')
  #if message.content.startswith('~rei you seeing this shit?'):
    #await message.channel.send('<:ReiStare:887162572963475506>')
  if "hey rei get me the event schedule" in message.content.lower():
    await message.channel.send("here you go!\n https://kenofnz.github.io/priconne-en-event-timer/")
  if "hey rei get me the ue guide" in message.content.lower():
    await message.channel.send("here you go!\n https://docs.google.com/spreadsheets/d/1JXbzIF4dWqzmmBwAxuNp74_v8eSM0tuDehWZtN9-lxY/edit#gid=504351475")
  if "hey rei get me the luna tower guide" in message.content.lower():
    await message.channel.send("here you go!\nhttps://docs.google.com/spreadsheets/d/e/2PACX-1vTcykwbV3NpLBgbVkKkZolfLuzlUJUN1JZW2Tg92l9tpGLmO5NFuNos75ytogpG4xPbl_5r7u4xAFrc/pubhtml")
  if "hey rei get me the gear guide" in message.content.lower():
    await message.channel.send("here you go!\nhttps://docs.google.com/spreadsheets/u/1/d/e/2PACX-1vQf9OgUjhCA8jblffEIFgd7aXDJAzfL6d6GA6wrJY1GUvxLgb4HmNLsNASPgqOJ1Io9yupgHURfNgiz/pubhtml")

  if "rei flip a coin" in message.content.lower():
    outcome = ["tails", "heads"]
    await message.channel.send(message.author.mention + " I flipped: " + random.choice(outcome))
  if message.content.lower() == "i give up":
    await message.channel.send(message.author.mention + ", you're getting stronger and stronger. It looks like you're not nearly at your limit yet... Prove to me that it's true. <:ugotthis:791813802433183784>")
  #ping test code (working)
  if message.content.startswith("pingtestAdmin"):
    await message.channel.send("<@&785703424565051432>, test succeeded")

  if message.content.startswith("~commands"):
    await message.channel.send("Here are my commands!\nrei flip a coin\nhey rei get me the event schedule\nhey rei get me the ue guide\nhey rei get me the luna tower guide\nhey rei get me the gear guide\nguides will always be up to date\nrei you seeing this shit?" )

keep_alive()
client.run(os.environ['TOKEN'])



