import discord
from discord.ext import commands

import sorting
from settings import Settings
from youtube import YoutubeCog

settings = Settings()
TOKEN = settings.DISCORD_TOKEN

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print('Connected to Discord!')

@bot.command()
async def mv_user(ctx, channel: discord.VoiceChannel, *members: discord.Member):
    for m in members:
        await m.move_to(channel)

@bot.command()
async def sort_users(ctx, channels: commands.Greedy[discord.VoiceChannel], members: commands.Greedy[discord.Member]):
    sorting.shuffle(members)
    buckets, ok = sorting.distribute(len(channels),members)
    if (ok):
        i = 0
        for channel in channels:
            for member in buckets[i]:
                await member.move_to(channel)
            i += 1

bot.add_cog(YoutubeCog(bot,settings))
bot.run(TOKEN)