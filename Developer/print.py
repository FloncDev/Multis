import discord, json
from discord.ext import commands

def getJson():
    with open("json/config.json", "r") as file:
        return json.load(file)

class cog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def print(self, ctx, *, thing):
        if ctx.author.id in getJson()["developersIds"]:
            print(thing)

    @commands.command()
    async def eval(self, ctx, *, thing):
        if ctx.author.id in getJson()["developersIds"]:
            eval(thing)

def setup(client):
    client.add_cog(cog(client))
