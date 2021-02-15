# doc_bot

## Initial Setup

### Virtual Environment (optional)
    python -m venv docbot-env

### Install Dependencies
    pip install -r requirements.txt

### Input Variables
doc_bot requires some values from a **.env** file such as the Google API key and Discord authentication token.  
Copy **settings.txt** to a new file named **.env** and fill in all the values.

    cp settings.txt .env
    
### Launching doc_bot
When the environment is setup, run doc_bot with the following:

    python doc_bot.py

If successfull, the console will display:

    "Connected to Discord!"

### Deploying to Heroku
Instead of using a .env file, create a "config var" on the heroku project for each setting in settings.txt.