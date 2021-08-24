from discord import client
from discord.ext import commands

class RENAME_ME(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command()
    async def test(self, ctx):
        pass

def setup(client):
    client.add_cog(RENAME_ME(client))