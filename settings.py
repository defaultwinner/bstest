import os
from dotenv import load_dotenv

load_dotenv()

discord_bot_name="bs_test"
discord_client_id = "650796075887624205"
discord_client_secret = "4XLvzF12eQL0Vb-hLgucsIhX2EoYJZbC"
discord_token = os.environ['DISCORD_TOKEN']
discord_guild = "https://discord.gg/zuPbPVf"
GOOGLE_SEARCH_API_KEY = os.environ['GOOGLE_API_KEY']


GOOGLE_API = "https://www.googleapis.com/customsearch/v1?key={}&cx=000637338422175236148:qau5q9golx0".format(GOOGLE_SEARCH_API_KEY)

REDIS_URL="redis://h:p8f8d8c871ce1bd2017ac0a29d51c3b03b61f94ef0e066ca38550e5c5e09f4b2e@ec2-3-234-194-184.compute-1.amazonaws.com:10349"
