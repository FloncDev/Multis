# Library Import
import discord
from discord.ext import commands
import os
from token import get_token

# Sets prefix, intents and the client variable.
prefix = [","] # To change the prefix or add multiple just add them to the list.
intents = discord.Intents(members=True, guilds=True, emojis=True, messages=True, reactions=True)
client = commands.Bot(command_prefix=prefix, help_command=None, intents=intents)

for filename in os.listdir("./cogs"): # Just loads all the commands in the cogs folder.
    if filename.endswith(".py"):      # To make your own commands just copy the template file.
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(get_token()) # Put your own token here (Don't share it!)