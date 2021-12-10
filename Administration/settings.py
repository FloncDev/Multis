import discord
from discord import colour
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

class settings(commands.Cog):

    def __init__(self, client):
        self.client = client

    @group()
    @commands.has_permissions(manage_channels=True)
    async def config(self, ctx):
        if ctx.invoked_subcommand == None:
            await ctx.send("```diff\n+ Availible config options\n- suggestion_channel\n- upvote\n- downvote\n- economy\n- pin_channel\n- pin_emoji_amount\n- enable_logging```") # [TO-DO] Make this a small help command showing all availible settings

    @config.command()
    @commands.has_permissions(manage_channels=True)
    async def suggestion_channel(self, ctx, channel):
        data, suggestions = await loadJson()
        data[str(ctx.guild.id)]["suggestionChannel"] = channel

        embed=discord.Embed(title=f"Set the suggestion channel to {channel}.", colour=0x00ff00)
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

    @config.command()
    @commands.has_permissions(administrator=True)
    async def enable_logging(self, ctx, setting):
        data, _ = await loadJson()
        if setting.lower() in ["y", "yes", "true",]:
            data[str(ctx.guild.id)]["enableLogs"] = True
            await ctx.send(embed=discord.Embed(title="Enabled logging.", colour=0x00ff00))
        
        elif setting.lower() in ["n", "no", "false",]:
            data[str(ctx.guild.id)]["enableLogs"] = False
            await ctx.send(embed=discord.Embed(title="Disabled logging.", colour=0x00ff00))

        else:
            embed=discord.Embed(title=f"Please enter a valid value. (True/False)", colour=0xff0000)
            await ctx.send(embed=embed)
            return

        await write(data)

def setup(client):
    client.add_cog(settings(client))