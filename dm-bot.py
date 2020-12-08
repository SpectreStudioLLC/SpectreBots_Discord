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
	server = ctx.message.guild
	global members
	members = [m for m in ctx.guild.members if role in m.roles]

	for m in members:
		await m.create_dm()
		await m.dm_channel.send(msg)
		count = count + 1
	
	await ctx.send("Done messaging the members. Sent out to {} members!".format(count))

bot.run(TOKEN)