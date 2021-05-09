import discord
from discord.ext import commands
import json

def loadJson():
        data = json.loads(open("json/serverConfig.json", "r").read())
        return data

class cog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group()
    async def prefix(self, ctx):
        if ctx.invoked_subcommand == None:
            await ctx.send("```diff\n+ Availible sub-commands\n- list\n- add\n- remove```")

    @prefix.command()
    @commands.has_permissions(administrator=True)
    async def list(self, ctx):
        data = loadJson()
        output = ""

        for prefix in data[str(ctx.guild.id)]["prefix"]:
            output += f"{prefix}\n"

        await ctx.send(f"```{output}```")

    @prefix.command()
    @commands.has_permissions(administrator=True)
    async def add(self, ctx, prefix: str=None):
        if prefix != None:
            data = loadJson()

            data[str(ctx.guild.id)]["prefix"].append(prefix)

            with open("json/serverConfig.json", "w") as output:
                json.dump(data, output, indent=2)

            await ctx.send(f"Added `{prefix}` as a prefix.")

        else:
            await ctx.send("Please enter a prefix.")

    @prefix.command()
    @commands.has_permissions(administrator=True)
    async def remove(self, ctx, prefix: str=None):
        if prefix != None:
            data = loadJson()

            data[str(ctx.guild.id)]["prefix"].pop(data[str(ctx.guild.id)]["prefix"].index(prefix))

            with open("json/serverConfig.json", "w") as output:
                json.dump(data, output, indent=2)

            await ctx.send(f"Removed `{prefix}` as a prefix.")

        else:
            await ctx.send("Please enter a prefix.")


    # Events, remove and add guilds from the json file.
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        data = loadJson()

        with open("json/suggestions.json", "w") as file:
            suggestions = json.load(file)

        with open("json/economy.json", "w") as file:
            eco = json.load(file)

        data[guild.id] = {
            "prefix": ["!"],
            "suggestionChannel": None,
            "upvoteEmoji": None,
            "downvoteEmoji": None,
            "economy": False,
            "pinChannel": None,
            "pinAmount": None
        }

        suggestions[guild.id] = {}
        eco[str(guild.id)] = {}

        with open("json/serverConfig.json", "w") as output:
            json.dump(data, output, indent=2)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        data = loadJson()

        with open("json/serverConfig.json", "w") as output:
            json.dump(data, output, indent=2)

def setup(client):
    client.add_cog(cog(client))