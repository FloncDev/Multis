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
    async def config(self, ctx):
        pass # [TO-DO] Make this a small help command showing all availible settings

    @config.command()
    @commands.has_permissions(manage_channels=True)
    async def suggestion_channel(self, ctx, channel):
        data, suggestions = await loadJson()
        data[str(ctx.guild.id)]["suggestionChannel"] = int(channel[2:-1])
        channel = self.client.get_channel(int(channel[2:-1]))

        embed=discord.Embed(title=f"Set the suggestion channel to {channel.mention}.", colour=0x00ff00)
        await ctx.send(embed=embed)

        await write(data)

    @config.command()
    @commands.has_permissions(manage_channels=True)
    async def upvote(self, ctx, emoji):
        data, suggestions = await loadJson()
        if len(emoji) == 1:
            data[str(ctx.guild.id)]["upvoteEmoji"] = emoji

        elif str(emoji[0]) == "<" and str(emoji[-1]) == ">":
            data[str(ctx.guild.id)]["upvoteEmoji"] = emoji[1:-1]

        else:
            embed=discord.Embed(title=f"Please enter a valid emoji.", colour=0x00ff00)
            await ctx.send(embed=embed)
            return       

        embed=discord.Embed(title=f"Set upvote emoji to {emoji}.", colour=0x00ff00)
        await ctx.send(embed=embed)

        await write(data)

    @config.command()
    @commands.has_permissions(manage_channels=True)
    async def downvote(self, ctx, emoji):
        data, suggestions = await loadJson()
        if len(emoji) == 1:
            data[str(ctx.guild.id)]["downvoteEmoji"] = emoji

        elif str(emoji[0]) == "<" and str(emoji[-1]) == ">":
            data[str(ctx.guild.id)]["downvoteEmoji"] = emoji[1:-1]

        else:
            embed=discord.Embed(title=f"Please enter a valid emoji.", colour=0x00ff00)
            await ctx.send(embed=embed)
            return       

        embed=discord.Embed(title=f"Set downvote emoji to {emoji}.", colour=0x00ff00)
        await ctx.send(embed=embed)

        await write(data)

    @config.command()
    @commands.has_permissions(administrator=True)
    async def economy(self, ctx, setting: str):
        data, suggestions = await loadJson()

        setting = setting.lower()

        if setting == "false":
            data[str(ctx.guild.id)]["economy"] = False

        elif setting == "true":
            data[str(ctx.guild.id)]["economy"] = True

        else:
            embed=discord.Embed(title=f"Please enter a valid value. (True/False)", colour=0xff0000)
            await ctx.send(embed=embed)
            return

        embed=discord.Embed(title=f"Set economy to {setting}.", colour=0x00ff00)
        await ctx.send(embed=embed)

        await write(data)

    @config.command()
    @commands.has_permissions(manage_channels=True)
    async def pin_channel(self, ctx, channel):
        data, suggestions = await loadJson()
        data[str(ctx.guild.id)]["pinChannel"] = channel
        await write(data)
        await ctx.send(embed=discord.Embed(title=f"Set pin channel to {channel}", colour=0x00ff00))

    @config.command()
    @commands.has_permissions(manage_channels=True)
    async def pin_emoji_amount(self, ctx, amount: int):
        data, suggestions = await loadJson()
        data[str(ctx.guild.id)]["pinAmount"] = amount
        await write(data)
        await ctx.send(embed=discord.Embed(title=f"Set pin emoji amount to {amount}", colour=0x00ff00))

def setup(client):
    client.add_cog(cog(client))