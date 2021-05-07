import asyncio
import discord
from discord.ext import commands
from discord.ext.commands.core import has_permissions

class cog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @has_permissions(ban_members=True)
    async def kick(self, ctx, member, reason=None):
        try:
            member = ctx.message.mentions[0]
        except:
            message = await ctx.send(embed=discord.Embed(title="Please ping a valid user.", color=0xff0000))
            asyncio.sleep(2)
            await message.delete()
        
        await member.kick(reason=f"Kicked by command by {ctx.author} for reason: {reason}")

def setup(client):
    client.add_cog(cog(client))
