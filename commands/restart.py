import discord
from discord.ext import commands

class cog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def restart(self, ctx):
        await self.client.logout()
        await self.client.login()

def setup(client):
    client.add_cog(cog(client))
