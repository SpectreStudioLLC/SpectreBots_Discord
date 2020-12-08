# bot.py
#Do all imports first
import os
import discord
import asyncio
from discord.utils import get
from discord.ext import commands
from dotenv import load_dotenv

#Grab variables from config
load_dotenv('config.env')
TOKEN = os.getenv('DISCORD_TOKEN')
welcomeMsg = os.getenv('WELCOME_MSG')

#set intents
intents = discord.Intents(members=True, messages=True, guilds=True)
client = discord.Client(intents=intents)

#Sends message to the terminal that the bot has connected
@client.event
async def on_ready():

	print(
		f'{client.user.name} has connected!\n')

#Message user when they join your server. This welcome message is defined in config.env
@client.event
async def on_member_join(member):
	
	print("Recognised that a member called " + member.name + " joined")
	try: 
		await member.create_dm()
		await member.dm_channel.send(f'{member.name},\n' + welcomeMsg)
		print("Sent message to " + member.name)


#Code to add custom roles to new members as they join by role ID
#These blocks of code can be removed if you don't want to assign roles as users join.
#You can do as many or as few of these as you like.

		try:
			role = member.guild.get_role(784808202897326130)	#Your roleID should go here
		except:
			print("Couldn't find role")
		try:
			await member.add_roles(role)
			print("Role added to " + member.name)
		except:
			print("Couldn't add role.")


		try:
			role = member.guild.get_role(784813366782328884)	#Your roleID should go here
		except:
			print("Couldn't find role")
		try:
			await member.add_roles(role)
			print("Role added to " + member.name)
		except:
			print("Couldn't add role.")


		try:
			role = member.guild.get_role(784813524047233065)	#Your roleID should go here
		except:
			print("Couldn't find role")
		try:
			await member.add_roles(role)
			print("Role added to " + member.name)
		except:
			print("Couldn't add role.")

	except:
		print("Couldn't message " + member.name)



#RUN client
client.run(TOKEN)