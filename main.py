import discord
import os
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))

#if message is recieved
@client.event
async def on_message(message):
  #if bot message, ignore
  if message.author == client.user:
    return
  #if message contains welcome in it, say hi! 
  if 'welcome' in message.content.lower():
    await message.channel.send('<:hiya:807336709993529374>')
  if message.content.startswith('~hey rei'):
    await message.channel.send('Hey!')
  if "rei you seeing this shit?" in message.content:
    await message.channel.send('<:ReiStare:887162572963475506>')
  #if message.content.startswith('~rei you seeing this shit?'):
    #await message.channel.send('<:ReiStare:887162572963475506>')
  if "hey rei, get me the event schedule" in message.content:
    await message.channel.send("here you go! https://kenofnz.github.io/priconne-en-event-timer/")
  if "hey rei, get me the ue spreadsheet" in message.content:
    await message.channel.send("here you go! https://docs.google.com/spreadsheets/d/1JXbzIF4dWqzmmBwAxuNp74_v8eSM0tuDehWZtN9-lxY/edit#gid=504351475")
  #if "hey rei, flip a coin" in message.content:
    
keep_alive()
client.run(os.environ['TOKEN'])


