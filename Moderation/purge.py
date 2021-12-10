import asyncio
import discord
from discord.ext import commands
from discord.ext.commands.core import has_permissions

class purge(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["clear"])
    @has_permissions(ban_members=True)
    async def purge(self, ctx, count):
        await ctx.channel.purge(limit=count+1)

        message = await ctx.send(f"Deleted {count} messages.")
        asyncio.sleep(2)
        await message.delete()

def setup(client):
    client.add_cog(purge(client))
