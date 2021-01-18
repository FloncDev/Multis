import discord
from discord.ext import commands

class cog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def print(self, ctx, *, thing):
        print(thing)

    @commands.command()
    async def eval(self, ctx, *, thing):
        eval(thing)

def setup(client):
    client.add_cog(cog(client))
