import discord
from discord.ext import commands
from discord.commands import slash_command, Option

class RENAME_SLASH(commands.Cog):

    def __init__(self, client):
        self.client = client
 
    @slash_command(guild_ids=[716611500256657469])
    async def slash(self, ctx):
        pass

def setup(client):
    client.add_cog(RENAME_SLASH(client))