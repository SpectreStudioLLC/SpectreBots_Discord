# SpectreBots_Discord
Bots for Discord written in Python
All of these bots are up to date using Discord.py 1.51

These bots are design to use config.env as a config file. Any variables will be defined there including your token.

Your must use your custom token from: https://discord.com/developers/applications/

Be sure to enable SERVER MEMBERS INTENT and PRESENCE INTENT.

The server you host these bots on must have discord.py 1.51, install by using: python3 -m pip install -U discord.py

The server must also have dotenv: $ pip install -U python-dotenv

Current files:

confing.env - custom variable for your server including your bot token

welcome-bot.py - A welcome bot that messages members and assigns roles as they join

dm-bot.py - A simple bot that allow a specified Admin_Role send DM's to users based on role. Command: $dm @role message
