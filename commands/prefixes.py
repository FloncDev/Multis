import discord
from discord.ext import commands
import json

class cog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group()
    async def prefix(self, ctx):
        pass

    @prefix.command()
    async def list(self, ctx):
        data = json.load(open("json/serverConfig.json", "r"))
        output = ""

        for prefix in data[str(ctx.guild.id)]["prefix"]:
            output += f"{prefix}\n"

        await ctx.send(f"```{output}```")

    @prefix.command()
    async def add(self, ctx, prefix: str=None):
        if prefix != None:
            data = json.load(open("json/serverConfig.json", "r"))

            data[str(ctx.guild.id)]["prefix"].append(prefix)

            with open("json/serverConfig.json", "w") as output:
                json.dump(data, output, indent=2)

            await ctx.send(f"Added `{prefix}` as a prefix.")

        else:
            await ctx.send("Please enter a prefix.")

    @prefix.command()
    async def remove(self, ctx, prefix: str=None):
        if prefix != None:
            data = json.load(open("json/serverConfig.json", "r"))

            data[str(ctx.guild.id)]["prefix"].pop(data[str(ctx.guild.id)]["prefix"].index(prefix))

            with open("json/serverConfig.json", "w") as output:
                json.dump(data, output, indent=2)

            await ctx.send(f"Removed `{prefix}` as a prefix.")

        else:
            await ctx.send("Please enter a prefix.")


    # Events, remove and add guilds from the json file.
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        data = json.load(open("json/serverConfig.json", "r"))

        data[guild.id] = {
            "prefix": ["!"],
            "suggestionChannel": None,
            "upvoteEmoji": None,
            "downvoteEmoji": None
        }

        with open("json/serverConfig.json", "w") as output:
            json.dump(data, output, indent=2)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        data = json.load(open("json/serverConfig.json", "r"))

        with open("json/serverConfig.json", "w") as output:
            json.dump(data, output, indent=2)

def setup(client):
    client.add_cog(cog(client))