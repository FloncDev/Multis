import discord
from discord.ext import commands
from discord.commands import slash_command, Option
from console import Console

console = Console(True)

class deleted_messages(commands.Cog):

    def __init__(self, client):
        self.client = client
 
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        console.log(f"{message.author}({message.author.id}) deleted message({message.id}): {message.content}")

def setup(client):
    client.add_cog(deleted_messages(client))