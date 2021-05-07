import asyncio
import discord
from discord import message
from discord.ext import commands
from discord.ext.commands.core import has_permissions

class cog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["info"])
    async def probe(self, ctx, user=None):
        if user == None:
            user = ctx.author
        else:
            try:
                user = await self.client.fetch_user(int(user))

            except:
                
                user = ctx.message.mentions[0]

        if user == None:
            await ctx.send("Cannot find the user.")
            return

        embed = discord.Embed(description=f"Mention: {user.mention}\nName: {user.display_name}#{user.discriminator}\nID: {user.id}\nIs Bot: {user.bot}\nCreated at: {user.created_at}")
        embed.set_image(url=user.avatar_url)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(cog(client))
