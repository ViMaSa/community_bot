import os

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='/')

@bot.command(name='mv_user')
async def moveUser(ctx, destination, *args)
    if (ctx.channel.name != "bot_commands"):
        return

    for u in args:
        bot.move_user(u,destination)

