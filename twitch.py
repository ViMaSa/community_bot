import requests
import os

from dotenv import load_dotenv
from dateutil.parser import parse
from discord.ext import tasks, commands
from datetime import datetime

class TwitchCog(commands.Cog):
    def __init__(self,bot,settings):
        self.bot = bot
        self.settings = settings
        self.prevTime = datetime.utcnow()
        self.first = True
        self.checkStreaming.start()
    
    @tasks.loop(seconds = 60)
    async def checkStreaming(self):
        url = 'https://api.twitch.tv/helix/streams'
        headers = {'Authorization': 'Bearer {}'.format(self.settings.TWITCH_TOKEN), 'Client-Id': self.settings.TWITCH_CLIENT_ID}
        queryParams = {'user_id': self.settings.TWITCH_USER_ID}

        response = requests.get(url,params=queryParams,headers=headers)
        ok = response.status_code == 200

        if ok and len(response.json()['data']) > 0:
            values = response.json()['data'][0]
            streamType = values['type']
            startedAt = values['started_at']
            startedAt = parse(startedAt,ignoretz=True)
            if (streamType == 'live' and (startedAt > self.prevTime or self.first)):
                self.first = False
                self.prevTime = startedAt
                name = values['user_login']
                url = f'https://www.twitch.tv/{name}'
                message = f'{self.settings.TWITCH_MSG}\n{url}'
                await self.sendNotification(message)

        print(f"Last twitch status: {response.status_code}")
        if not ok:
            print(f'Body: {response.text}')


    @checkStreaming.before_loop
    async def before_checkStreaming(self):
        await self.bot.wait_until_ready()

    async def sendNotification(self,message):
        channel = self.bot.get_channel(self.settings.CHANNEL_ID)
        guild = self.bot.get_guild(self.settings.GUILD_ID)
        role = guild.default_role
        content = f'{role.name}\n{message}'
        await channel.send(content)

