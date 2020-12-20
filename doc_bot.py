import os
import discord

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print('Connected to Discord!')

@bot.command()
async def mv_user(ctx, channel: discord.VoiceChannel, *members: discord.Member):
    for m in members:
        await m.move_to(channel)

bot.run(TOKEN)