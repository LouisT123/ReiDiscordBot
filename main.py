import discord
import os
#from keep_alive import keep_alive
import random
from dotenv import load_dotenv
#client = discord.Client()
# 3/15 replacing above to add intents to see if can find member
intents = discord.Intents.all()
client = discord.Client(intents = intents)
from notification import Notification 
#notification bot, takes in chat id and client
notif = Notification(client, 785705961032515614 )
#test 912532987671900180
#test2 791804582442434590
#actual 785705961032515614

load_dotenv()

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

#Working! 3/15 boss ping
@client.event
#add the roles
async def on_raw_reaction_add(payload):
  message_id = payload.message_id
  #if user reacts to the specific select roles message on discord
  if message_id == 953428332530245632:
    #grab guild id 
    guild_id = payload.guild_id
    #search for all the guilds to find matching one
    guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
    #get role
    if payload.emoji.name == 'yabaidesune':
      role = discord.utils.get(guild.roles, name='b1')
    elif payload.emoji.name == 'kyaru':
      role = discord.utils.get(guild.roles, name='b2')
    elif payload.emoji.name == 'disturbed':
      role = discord.utils.get(guild.roles, name='b3')
    elif payload.emoji.name == 'criyaru':
      role = discord.utils.get(guild.roles, name='b4')
    elif payload.emoji.name == 'yamete':
      role = discord.utils.get(guild.roles, name='b5')
    else:
      role = discord.utils.get(guild.roles, name=payload.emoji.name)

    #if we got the role, attach it to the user
    if role is not None:
      member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
      #if valid add the role
      if member is not None:
        await member.add_roles(role)
        print("role is added ")
      else:
        print("member not found")
    else:
      print("Role not found")


@client.event
#remove the roles
async def on_raw_reaction_remove(payload):
  message_id = payload.message_id
  #if message is :one:
  if message_id == 953428332530245632:
    #grab guild id 
    guild_id = payload.guild_id
    #search for all the guilds to find matching one
    guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
    #get role
    if payload.emoji.name == 'yabaidesune':
      role = discord.utils.get(guild.roles, name='b1')
    elif payload.emoji.name == 'kyaru':
      role = discord.utils.get(guild.roles, name='b2')
    elif payload.emoji.name == 'disturbed':
      role = discord.utils.get(guild.roles, name='b3')
    elif payload.emoji.name == 'criyaru':
      role = discord.utils.get(guild.roles, name='b4')
    elif payload.emoji.name == 'yamete':
      role = discord.utils.get(guild.roles, name='b5')
    else:
      role = discord.utils.get(guild.roles, name=payload.emoji.name)

    #if we got the role, attach it to the user
    if role is not None:
      member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
      #if valid remove the role
      if member is not None:
        await member.remove_roles(role)
        print("role is removed ")
      else:
        print("member not found")
    else:
      print("Role not found")

#keep_alive()

client.run(os.environ['TOKEN'])



