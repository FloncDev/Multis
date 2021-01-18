import discord
from discord.ext import commands
from discord.ext.commands.core import group
import json

async def loadJson():
        data = json.loads(open("json/serverConfig.json", "r").read())
        suggestions = json.loads(open("json/suggestions.json", "r").read())

        return data, suggestions

async def write(data):
    with open("json/serverConfig.json", "w") as output:
        json.dump(data, output, indent=2)

class cog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @group()
    @commands.has_permissions(manage_channels=True)
    async def settings(self, ctx):
        pass # [TO-DO] Make this a small help command showing all availible settings

    @settings.command()
    @commands.has_permissions(manage_channels=True)
    async def suggestion_channel(self, ctx, channel):
        data, suggestions = await loadJson()
        data[str(ctx.guild.id)]["suggestionChannel"] = int(channel[2:-1])
        channel = self.client.get_channel(int(channel[2:-1]))

        embed=discord.Embed(title=f"Set the suggestion channel to {channel.mention}.", color=0x00ff00)
        await ctx.send(embed=embed)

        await write(data)

    @settings.command()
    @commands.has_permissions(manage_channels=True)
    async def upvote(self, ctx, emoji):
        data, suggestions = await loadJson()
        if len(emoji) == 1:
            data[str(ctx.guild.id)]["upvoteEmoji"] = emoji

        elif str(emoji[0]) == "<" and str(emoji[-1]) == ">":
            data[str(ctx.guild.id)]["upvoteEmoji"] = emoji[1:-1]

        else:
            embed=discord.Embed(title=f"Please enter a valid emoji.", color=0x00ff00)
            await ctx.send(embed=embed)
            return       

        embed=discord.Embed(title=f"Set upvote emoji to {emoji}.", color=0x00ff00)
        await ctx.send(embed=embed)

        await write(data)

    @settings.command()
    @commands.has_permissions(manage_channels=True)
    async def downvote(self, ctx, emoji):
        data, suggestions = await loadJson()
        if len(emoji) == 1:
            data[str(ctx.guild.id)]["downvoteEmoji"] = emoji

        elif str(emoji[0]) == "<" and str(emoji[-1]) == ">":
            data[str(ctx.guild.id)]["downvoteEmoji"] = emoji[1:-1]

        else:
            embed=discord.Embed(title=f"Please enter a valid emoji.", color=0x00ff00)
            await ctx.send(embed=embed)
            return       

        embed=discord.Embed(title=f"Set downvote emoji to {emoji}.", color=0x00ff00)
        await ctx.send(embed=embed)

        await write(data)

    @settings.command()
    @commands.has_permissions(administrator=True)
    async def economy(self, ctx, setting: str):
        data, suggestions = await loadJson()

        setting = setting.lower()

        if setting == "false":
            data[str(ctx.guild.id)]["economy"] = False

        elif setting == "true":
            data[str(ctx.guild.id)]["economy"] = True

        else:
            embed=discord.Embed(title=f"Please enter a valid value. (True/False)", color=0x00ff00)
            await ctx.send(embed=embed)
            return

        embed=discord.Embed(title=f"Set economy to {setting}.", color=0x00ff00)
        await ctx.send(embed=embed)

        await write(data)

def setup(client):
    client.add_cog(cog(client))