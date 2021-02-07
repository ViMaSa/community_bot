from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime
from dateutil.parser import parse
from discord.ext import tasks, commands
import time

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

class YoutubeCog(commands.Cog):
    def __init__(self,bot,settings):
        self.bot = bot
        self.settings = settings
        self.prevTime = datetime.utcnow()
        self.service = build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,
            developerKey=self.settings.GOOGLE_DEVELOPER_KEY)
        self.collection = self.service.playlistItems()
        self.playlistRequest = self.collection.list(part="contentDetails",
            playlistId=self.settings.PLAYLIST_ID,
            maxResults=self.settings.MAX_RESULTS)
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

    @videoChecker.after_loop
    async def after_videoChecker(self):
        self.service.close()

    async def checkRecentUploads(self):
        try:
            response = self.playlistRequest.execute()
            #First video is the most recent
            recentVideo = response['items'][0]
            videoDateString = recentVideo['contentDetails']['videoPublishedAt']
            videoDate = parse(videoDateString,ignoretz=True)
            print(f'Most recent video date: {videoDate}')
            if videoDate > self.prevTime:
                self.prevTime = videoDate
                print(f"New video published on: {videoDate}")
                return recentVideo['contentDetails']['videoId']
        except HttpError as e:
            print(e.content)

        return ""

    def buildUrl(self,videoID):
        return f"https://www.youtube.com/watch?v={videoID}"

    async def sendNotification(self,message):
        channel = self.bot.get_channel(790038053355913226)
        guild = self.bot.get_guild(708614576123543632)
        # Leaving this here for testing purposes. When ready, just use the guild.default_role property.
        # role = guild.default_role
        # Using admin role as test
        role = guild.get_role(710946375457701949)
        content = f'{role.mention} {message}'
        await channel.send(content)