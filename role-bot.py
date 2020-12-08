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
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

#List members of a specified role - ADMIN ONLY!
@bot.command(pass_context=True)
@commands.has_role(Admin_Role)
async def listMembersOfRole(ctx, role: discord.Role):
	count = 0
	global members
	members = [m for m in ctx.guild.members if role in m.roles]

	for member in members:
		await ctx.send(f"{member.display_name} - {member.id}")
		count = count + 1
	
	await ctx.send("The following role {} has {} members!".format(role, count))

#Add role to members - ADMIN ONLY!
@bot.command(pass_context=True)
@commands.has_role(Admin_Role)
async def addRoleToAllMembers(ctx, role: discord.Role):
	count = 0
	for member in server.members:
		if role in member.roles:
			pass
		else:
			await member.add_roles(role)
			await ctx.send("Added role to " + member.name)
			count = count + 1
	await ctx.send("The following role {} has been applied to {} members!".format(role, count))

bot.run(TOKEN)