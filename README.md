# doc_bot

## Initial Setup
    pip install -U discord.py
    pip install -U google-api-python-client
    pip install -U python-dotenv
    pip install -U python-dateutil

doc_bot requires some values from a **.env** file such as the Google API key and Discord authentication token.  
Copy **settings.txt** to a new file named **.env** and fill in all the values.

    cp settings.txt .env
    

When the environment is setup, run doc_bot with the following:

    python doc_bot.py

If successfull, the console will display:

    "Connected to Discord!"