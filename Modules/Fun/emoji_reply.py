import discord
from discord.ext import commands
from console import Console
import emoji

console = Console()

class emoji_reply(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot and emoji.is_emoji(message.content):
            await message.channel.send(message.content)

def setup(client):
    client.add_cog(emoji_reply(client))