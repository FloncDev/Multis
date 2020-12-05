import discord
from discord.ext import commands
import json

class cog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def prefixList(self, ctx):
        data = json.load(open("json/serverConfig.json", "r"))
        output = ""

        for prefix in data[str(ctx.guild.id)]["prefix"]:
            output += f"{prefix}\n"

        await ctx.send(f"```{output}```")

    @commands.command()
    async def prefixAdd(self, ctx, prefix: str=None):
        if prefix != None:
            data = json.load(open("json/serverConfig.json", "r"))

            data[str(ctx.guild.id)]["prefix"].append(prefix)

            with open("json/serverConfig.json", "r") as output:
                json.dump(data, output, indent=2)

            await ctx.send(f"Added {prefix} as a prefix.")

        else:
            await ctx.send("Please enter a prefix.")

    @commands.command()
    async def prefixRemove(self, ctx, prefix: str=None):
        if prefix != None:
            data = json.load(open("json/serverConfig.json", "r"))

            data[str(ctx.guild.id)]["prefix"].pop(data[str(ctx.guild.id)]["prefix"].index(prefix))

            with open("json/serverConfig.json", "r") as output:
                json.dump(data, output, indent=2)

            await ctx.send(f"Removed {prefix} as a prefix.")

        else:
            await ctx.send("Please enter a prefix.")


    # Events, remove and add guilds from the json file.
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        data = json.load(open("json/serverConfig.json", "r"))

        data.append({
            "prefix": "!",
            "suggestionChannel": None
        })

        with open("json/serverConfig.json", "r") as output:
            json.dump(data, output, indent=2)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        data = json.load(open("json/serverConfig.json", "r"))

        with open("json/serverConfig.json", "r") as output:
            json.dump(data, output, indent=2)

def setup(client):
    client.add_cog(cog(client))