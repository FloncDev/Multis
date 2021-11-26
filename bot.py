import discord
from discord.ext import commands
from console import Console
import os
import json

with open('config.json') as f:
    config = json.load(f)
console = Console(True)
client = commands.Bot(command_prefix=config["prefixes"], case_insensitive=True, intents=discord.Intents.all())

for module in os.listdir("Modules"):
    for filename in os.listdir(f"Modules/{module}"):
        if filename.endswith(".py"):
            console.log(f"Loading {module}/{filename}")
            client.load_extension(f"Modules.{module}.{filename[:-3]}")

try:
    client.run(config["token"])
except discord.errors.ClientException:
    console.error("Invalid Token - Please make a '.env' file and put the token in there with the key 'TOKEN'")