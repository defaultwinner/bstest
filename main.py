import os
import discord
import settings
import google
import sqlite3

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')

con = sqlite3.connect('db.sqlite3')

class MyClient(discord.Client):
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
		return ["you tried searching recent keywords"]
	
	def search_google(self, message):
		search_keyword = " ".join(message.content.split()[1:])
		return google.google_results(search_keyword)
	

	async def on_ready(self):
		print('Logged on as {0}!'.format(self.user))

	async def on_message(self, message):
		if str(message.author).split("#")[0]!=settings.discord_bot_name:
			if message.content.split()[0].lower() in self.actions:
				response = self.actions[message.content.split()[0]](message)
				for m in response:
					print(m)
					await message.channel.send(m)

client = MyClient()
client.run(settings.discord_token)