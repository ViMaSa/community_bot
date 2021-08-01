from dotenv import load_dotenv
import os

#load: loads the variables from '.env' and stores them into memory

class Settings(object):
    def __init__(self):
        load_dotenv()
        self.GOOGLE_DEVELOPER_KEY = os.getenv('GOOGLE_DEVELOPER_KEY')
        self.PLAYLIST_ID = os.getenv('PLAYLIST_ID')
        self.MAX_RESULTS = int(os.getenv('MAX_RESULTS'))
        self.DISCORD_TOKEN = os.getenv('DISCORD_AUTH_TOKEN')
        self.CHANNEL_ID = int(os.getenv('CHANNEL_ID'))
        self.GUILD_ID = int(os.getenv('GUILD_ID'))
        self.TWITCH_TOKEN = os.getenv('TWITCH_TOKEN')
        self.TWITCH_CLIENT_ID = os.getenv('TWITCH_CLIENT_ID')
        self.TWITCH_USER_ID = os.getenv('TWITCH_USER_ID')
        self.TWITCH_MSG = os.getenv('TWITCH_MSG')
        self.TWITCH_SECRET = os.getenv('TWITCH_SECRET')
        