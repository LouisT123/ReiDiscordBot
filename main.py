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
  
  if message.content.startswith('~hey rei'):
    await message.channel.send('Hey!')
keep_alive()
client.run(os.environ['TOKEN'])


