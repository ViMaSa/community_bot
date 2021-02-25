from datetime import datetime
from dateutil.parser import parse
from discord.ext import tasks, commands
import time
import requests

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

class YoutubeCog(commands.Cog):
    def __init__(self,bot,settings):
        self.bot = bot
        self.settings = settings
        self.prevTime = datetime.utcnow()
        self.videoChecker.start()

    @tasks.loop(seconds = 60)
    async def videoChecker(self):
        videoID = await self.checkRecentUploads()
        if (len(videoID) > 0):
            url = self.buildUrl(videoID)
            message = f"Shaun posted a new video! Make sure to go check it out!\n{url}"
            await self.sendNotification(message)

    @videoChecker.before_loop
    async def before_videoChecker(self):
        await self.bot.wait_until_ready()

    async def checkRecentUploads(self):
        url = 'https://youtube.googleapis.com/youtube/v3/playlistItems'
        params = {
            'part':'contentDetails',
            'maxResults':str(self.settings.MAX_RESULTS),
            'playlistId':self.settings.PLAYLIST_ID,
            'key':self.settings.GOOGLE_DEVELOPER_KEY
        }
        headers = {
            'Accept':'application/json'
        }
        response = requests.get(url,headers=headers,params=params)
        if (response.status_code == 200):
            #First video is the most recent
            recentVideo = response.json()['items'][0]
            videoDateString = recentVideo['contentDetails']['videoPublishedAt']
            videoDate = parse(videoDateString,ignoretz=True)
            if videoDate > self.prevTime:
                self.prevTime = videoDate
                print(f"New video published on: {videoDate}")
                return recentVideo['contentDetails']['videoId']
            else:
                print(f'Most recent video date: {videoDate}')
        else:
            print(f'Youtube: Received invalid response code: {response.status_code} Body:\n{response.text}')

        return ""

    def buildUrl(self,videoID):
        return f"https://www.youtube.com/watch?v={videoID}"

    async def sendNotification(self,message):
        channel = self.bot.get_channel(self.settings.CHANNEL_ID)
        guild = self.bot.get_guild(self.settings.GUILD_ID)
        role = guild.default_role
        content = f'{role.name} {message}'
        await channel.send(content)