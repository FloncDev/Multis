import discord
from discord.ext import commands
from console import Console

console = Console(True)

class reaction_add(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if not user.bot:
            console.info(f"{reaction.emoji} was added to message {reaction.message.id} by {user}({user.id})")

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        if not user.bot:
            console.info(f"{reaction.emoji} was removed from message {reaction.message.id} by {user}({user.id})")

def setup(client):
    client.add_cog(reaction_add(client))