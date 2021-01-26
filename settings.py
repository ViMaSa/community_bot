from dotenv import load_dotenv
import os

#load: loads the variables from '.env' and stores them into memory
def load():
    load_dotenv()
    global DEVELOPER_KEY
    global PLAYLIST_ID
    global MAX_RESULTS
    global DISCORD_TOKEN

    DEVELOPER_KEY = os.getenv('DEVELOPER_KEY')
    PLAYLIST_ID = os.getenv('PLAYLIST_ID')
    MAX_RESULTS = int(os.getenv('MAX_RESULTS'))
    DISCORD_TOKEN = os.getenv('DT')