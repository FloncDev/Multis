# Library Import
import discord
from discord.ext import commands
import os
import json

# Gets all the servers custom prefixes.
def getPrefixes(client, message):
    guild = message.guild.id
    data = json.loads(open("./json/serverConfig.json", "r").read())
    return data[str(guild)]["prefix"]

# Sets prefix, intents and the client variable.
intents = discord.Intents(members=True, guilds=True, emojis=True, messages=True, reactions=True)
client = commands.Bot(command_prefix=getPrefixes, help_command=None, intents=intents)

for filename in os.listdir("./commands"): # Just loads all the commands in the commands folder.
    if filename.endswith(".py"):      # To make your own commands just copy the template file.
        client.load_extension(f"commands.{filename[:-3]}")

client.run("NzkyODAxODIyNTk0MzAxOTUy.X-jAPA.2VV0k9dVgoiUXEBhTMfrBBOP3DE") # Put your own token here (Don't share it!)