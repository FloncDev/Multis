import discord
from discord.ext import commands
from console import Console

console = Console(True)

class message_edit(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if not after.author.bot:
            console.info(f"{after.author}({after.author.id}) edited their message in {after.channel.name}.\n{before.content} -> {after.content}")

def setup(client):
    client.add_cog(message_edit(client))