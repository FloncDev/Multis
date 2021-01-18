from os import error
from Administration.settings import loadJson
import discord
from discord.ext import commands
from discord.ext.commands.core import group, has_permissions
import json
import asyncio

def loadJSON():
    return json.loads(open("json/userConfig.json", "r").read())

def writeJSON(data):
    with open("json/userConfig.json", "w") as output:
        json.dump(data, output, indent=2)

class cog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @group(aliases=["eco"])
    async def economy(self, ctx):
        embed = discord.Embed(title="Available commands.", description="")

    @economy.command(aliases=["bal"])
    async def balance(self, ctx, user=None):
        data = loadJSON()

        if user != None:
            user = ctx.message.mentions[0].id
            pronoun = f"{ctx.message.mentions[0]}'s"

        else:
            user = ctx.author.id
            pronoun = "Your"

        balance = data[str(user)]["balance"]

        embed=discord.Embed(title=f"{pronoun} balance is: {balance}", color=0xffff00)
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @economy.command()
    @has_permissions(manage_channels=True)
    async def set(self, ctx, user=None, amount=None):
        data = loadJSON()

        if user == None or amount == None:
            embed=discord.Embed(title="Please ping a valid user and enter a amount.", color=0xff0000)
            await ctx.send(embed=embed)
            return

        else:
            amount = int(amount)

        try:
            user = ctx.message.mentions[0]

            if user == None:
                raise Exception("No user found")

        except:
            embed=discord.Embed(title="Please ping a valid user.", color=0xff0000)
            await ctx.send(embed=embed)
            return

        data[str(user.id)]["balance"] = amount

        writeJSON(data)
        message = await ctx.send(f"Set the balance of {user} to {amount}")
        await asyncio.sleep(2)
        await message.delete()

    @economy.command(aliases=["+"])
    @has_permissions(manage_channels=True)
    async def add(self, ctx, user=None, amount=None):
        data = loadJSON()

        if user == None or amount == None:
            embed=discord.Embed(title="Please ping a valid user and enter a amount.", color=0xff0000)
            await ctx.send(embed=embed)
            return

        else:
            amount = int(amount)
        
        try:
            user = ctx.message.mentions[0]

            if user == None:
                raise Exception("No user found")

        except:
            embed=discord.Embed(title="Please ping a valid user.", color=0xff0000)
            await ctx.send(embed=embed)
            return

        data[str(user.id)]["balance"] = data[str(user.id)]["balance"] + amount

        writeJSON(data)
        message = await ctx.send(f"Added {amount} to {user}'s balance.")
        await asyncio.sleep(2)
        await message.delete()

    @economy.command(aliases=["-"])
    @has_permissions(manage_channels=True)
    async def remove(self, ctx, user=None, amount=None):
        data = loadJSON()
        
        if user == None or amount == None:
            embed=discord.Embed(title="Please ping a valid user and enter a amount.", color=0xff0000)
            await ctx.send(embed=embed)
            return

        else:
            amount = int(amount)

        try:
            user = ctx.message.mentions[0]

            if user == None:
                raise Exception("No user found")

        except:
            embed=discord.Embed(title="Please ping a valid user.", color=0xff0000)
            await ctx.send(embed=embed)
            return

        data[str(user.id)]["balance"] = data[str(user.id)]["balance"] - amount

        writeJSON(data)
        message = await ctx.send(f"Removed {amount} to {user}'s balance.")
        await asyncio.sleep(2)
        await message.delete()

def setup(client):
    client.add_cog(cog(client))
