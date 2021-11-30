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
  if message.content == "welcome":
    await message.channel.send('<:hiya:807336709993529374>')
  if message.content.startswith('~hey rei'):
    await message.channel.send('Hey!')
  
  if message.content.startswith('~rei you seeing this shit?'):
    await message.channel.send('<:ReiStare:887162572963475506>')
  
keep_alive()
client.run(os.environ['TOKEN'])


