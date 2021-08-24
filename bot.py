import discord
from discord.ext import commands
from console import Console
from dotenv import load_dotenv
import os


def get_prefix(client, message):
    return "!"


console = Console()
client = commands.Bot(command_prefix=get_prefix, case_insensitive=True, intents=discord.Intents.all())


def loadModule(module):
    for filename in os.listdir(f"Modules/{module}"):
        if filename.endswith(".py"):
            client.load_extension(f"Modules.{module}.{filename[:-3]}")

def unloadModule(module):
    for filename in os.listdir(f"Modules/{module}"):
        if filename.endswith(".py"):
            client.unload_extension(f"Modules.{module}.{filename[:-3]}")


@client.command()
async def reload(ctx):
    for i in os.listdir("Modules"):
        try:
            unloadModule(i)
            loadModule(i)
        except Exception as e:
            console.error(f"There was an error reloading {i}.\n{e}")

    console.info("Reload Success.")

for i in os.listdir("Modules"):
    loadModule(i)

try:
    load_dotenv()
    client.run(os.environ.get("TOKEN"))
except discord.errors.ClientException:
    console.error("Invalid Token - Please make a '.env' file and put the token in there with the key 'TOKEN'")