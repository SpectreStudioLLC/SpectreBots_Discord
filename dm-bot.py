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
Admin_Role = os.getenv('ADMIN_ROLE')

#set intents/bot
intents = discord.Intents(members=True, messages=True, guilds=True)
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
	print('DM-Bot has connected!\n')

#DM Members of specific role - ADMIN ONLY!
@bot.command(pass_context=True)
@commands.has_role(Admin_Role)
async def dm(ctx, role: discord.Role, *, msg):
	count = 0
	global members
	members = [m for m in ctx.guild.members if role in m.roles]

	await ctx.send('Starting to send DMs.')
	
	for m in members:
		try:
			await m.create_dm()
			await m.dm_channel.send(msg)
			await ctx.send('Message to {}'.format(m.name))
			count = count + 1
		except:
			await ctx.send('Failed to send message to {}'.format(m.name))
	
	await ctx.send("Done messaging the members. Sent out to {} members!".format(count))


#Error Handling
@dm.error
async def dm_error(ctx, error):
	if isinstance(error, commands.RoleNotFound):
		await ctx.send(error)
	elif isinstance(error, commands.CommandInvokeError):
		await ctx.send(error)
	else:
		await ctx.send(error)
		await ctx.send('Error: Check the vps logs for error')

bot.run(TOKEN)