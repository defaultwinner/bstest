import os
import discord
import settings
import google
import sqlite3
import redis

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')

con = sqlite3.connect('db.sqlite3')

r = redis.from_url(settings.REDIS_URL)

class DiscordClient(discord.Client):
	def __init__(self, *args, **kwargs):
		self.actions = {
		"!google": self.search_google,
		"!recent": self.get_recent,
		"hi": self.say_hey
	}
		super().__init__(*args, **kwargs)

	def say_hey(self, message):
		return ["Hey"]

	def get_recent(self, message):
		''' Return Recent searches by the user 
		 '''
		search_keyword = " ".join(message.content.split()[1:])
		recent_list = list(r.lrange(str(message.author),0, 10))
		recent_search = [str(s) for s in recent_list if search_keyword in str(s)]
		return recent_search
	
	def search_google(self, message):
		search_keyword = " ".join(message.content.split()[1:])
		r.lpush(str(message.author), search_keyword)
		r.ltrim(str(message.author),0, 20)
		return google.google_results(search_keyword)
	

	async def on_ready(self):
		print('Logged on as {0}!'.format(self.user))

	async def on_message(self, message):
		if (str(message.author).split("#")[0]!=settings.discord_bot_name and 
		message.content.split()[0].lower() in self.actions):
			response = self.actions[message.content.split()[0]](message)
			for m in response:
				await message.channel.send(str(m))

client = DiscordClient()
client.run(settings.discord_token)