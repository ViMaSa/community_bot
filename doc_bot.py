import os
import discord
from discord.ext import commands

import sorting
import settings

settings.load()
TOKEN = settings.DISCORD_TOKEN

bot = commands.Bot(command_prefix='/')

def checkbotchannel(ctx):
    return ctx.channel.id == 790038053355913226

@bot.event
async def on_ready():
    print('Connected to Discord!')

@bot.command()
@commands.check(checkbotchannel)
async def mv_user(ctx, channel: discord.VoiceChannel, *members: discord.Member):
    for m in members:
        await m.move_to(channel)

@bot.command()
@commands.check(checkbotchannel)
async def sort_users(ctx, channels: commands.Greedy[discord.VoiceChannel], members: commands.Greedy[discord.Member]):
    sorting.shuffle(members)
    buckets, ok = sorting.distribute(len(channels),members)
    if (ok):
        i = 0
        for channel in channels:
            for member in buckets[i]:
                await member.move_to(channel)
            i += 1

bot.run(TOKEN)