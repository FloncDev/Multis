import discord
from discord.ext import commands
from discord.commands import slash_command, Option
import json

with open('config.json') as f:
    config = json.load(f)

class RENAME_SLASH(commands.Cog):

    def __init__(self, client):
        self.client = client
 
    @slash_command()
    async def slash(self, ctx):
        pass

def setup(client):
    client.add_cog(RENAME_SLASH(client))