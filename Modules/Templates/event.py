import discord
from discord.ext import commands

class RENAMEME(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        pass

def setup(client):
    client.add_cog(RENAMEME(client))