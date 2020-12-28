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

    @commands.command()
    async def suggest(self, ctx, *, suggestion):
        data, suggestions = loadJson()

        if data[str(ctx.guild.id)]["suggestionChannel"] != None and data[str(ctx.guild.id)]["downvoteEmoji"] != None and data[str(ctx.guild.id)]["upvoteEmoji"] != None:

            suggestionChannel = self.client.get_channel(data[str(ctx.guild.id)]["suggestionChannel"])
            member = ctx.guild.get_member(ctx.author.id)

            embed=discord.Embed(description=suggestion, colour=member.color)
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            embed.set_footer(text="ID:")

            message = await suggestionChannel.send(embed=embed)

            await message.add_reaction(data[str(ctx.guild.id)]["upvoteEmoji"])
            await message.add_reaction(data[str(ctx.guild.id)]["downvoteEmoji"])
            await message.add_reaction("🚫")

            embed.set_footer(text=f"Message id: {message.id}")

            await message.edit(embed=embed)

        else:
            await ctx.send("Please setup a suggestion channel, upvote emoji and downvote emoji.")

    @group()
    async def suggestions(self, ctx):
        pass

    @suggestions.command()
    async def edit(self, ctx):
         data, suggestions = loadJson()

    @suggestions.command()
    async def respond(self, ctx, id, *, response):
        data, suggestions = loadJson()
    
    @group()
    @commands.has_permissions(manage_channels=True)
    async def setup(self, ctx):
        await ctx.send("PleASe")

    @setup.command()
    @commands.has_permissions(manage_channels=True)
    async def suggestion_channel(self, ctx, channel):
        data, suggestions = loadJson()
        data[str(ctx.guild.id)]["suggestionChannel"] = int(channel[2:-1])
        channel = self.client.get_channel(int(channel[2:-1]))

        await ctx.send(f"Set {channel.mention} as the suggestion channel")

        with open("json/serverConfig.json", "w") as output:
            json.dump(data, output, indent=2)

    @setup.command()
    @commands.has_permissions(manage_channels=True)
    async def suggestion_upvote(self, ctx, emoji):
        data, suggestions = loadJson()
        if len(emoji) == 1:
            data[str(ctx.guild.id)]["upvoteEmoji"] = emoji

        else:
            data[str(ctx.guild.id)]["upvoteEmoji"] = emoji[1:-1]

        await ctx.send(f"Set {emoji} as the upvote emoji")

        with open("json/serverConfig.json", "w") as output:
            json.dump(data, output, indent=2)

    @setup.command()
    @commands.has_permissions(manage_channels=True)
    async def suggestion_downvote(self, ctx, emoji):
        data, suggestions = loadJson()
        if len(emoji) == 1:
            data[str(ctx.guild.id)]["downvoteEmoji"] = emoji

        else:
            data[str(ctx.guild.id)]["downvoteEmoji"] = emoji[1:-1]

        await ctx.send(f"Set {emoji} as the downvote emoji")

        with open("json/serverConfig.json", "w") as output:
            json.dump(data, output, indent=2)

def setup(client):
    client.add_cog(cog(client))