import discord
from discord.ext import commands
from discord.ext.commands.core import group
import json

def loadJson():
        data = json.loads(open("json/serverConfig.json", "r").read())
        suggestions = json.loads(open("json/suggestions.json", "r").read())

        return data, suggestions

class cog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @group()
    async def suggest(self, ctx, suggestion):
        data, suggestions = loadJson()

        if data[str(ctx.guild.id)]["suggestionChannel"] == None or data[str(ctx.guild.id)]["downvoteEmoji"] == None or data[str(ctx.guild.id)]["upvoteEmoji"] == None:

            embed=discord.Embed(description=suggestion)
            embed.set_author(name=ctx.author, url=ctx.author.avatar_url)
            embed.set_footer(text="ID:")

            message = await ctx.send(embed=embed)

            message.add

    @suggest.command()
    async def edit(self, ctx):
         data, suggestions = loadJson()

    @suggest.command()
    async def respond(self, ctx):
        data, suggestions = loadJson()
    
    @suggest.group()
    @commands.has_permissions(manage_channels=True)
    async def setup(self, ctx, channel):
        data, suggestions = loadJson()
        data[str(ctx.guild.id)]["suggestionChannel"] = int(channel[2:-1])
        channel = self.client.get_channel(int(channel[2:-1]))

        await ctx.send(f"Set {channel.mention} as the suggestion channel")

        with open("json/serverConfig.json", "w") as output:
            json.dump(data, output, indent=2)

    @setup.command()
    async def upvote(self, ctx, emoji):
        pass

def setup(client):
    client.add_cog(cog(client))
