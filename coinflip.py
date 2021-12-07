import random
import main
from random import choice


determine_flip = [1, 0]

@client.commands()
async def coinflip(ctx):
    if random.choice(determine_flip) == 1:
        embed = discord.Embed(title="Coinflip | (Bot Name)", description=f"{ctx.author.mention} Flipped coin, we got **Heads**!")
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title="Coinflip | (Bot Name)", description=f"{ctx.author.mention} Flipped coin, we got **Tails**!")
        await ctx.send(embed=embed)