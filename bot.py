import discord
from discord.ext import commands
from console import Console
import os
import json

with open("config.json", "r") as f:
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
except discord.errors.ClientException as e:
    console.error(f"Invalid Token - Please check the config.json file. {str(e)}")