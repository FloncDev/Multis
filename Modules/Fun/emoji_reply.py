import discord
from discord.ext import commands, tasks
from console import Console
import emoji

console = Console(True)

class emoji_reply(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.emoji = False
        self.clear_emojis.start()

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot and emoji.is_emoji(message.content) and not self.emoji:
            await message.channel.send(message.content)
            console.log("Emoji reset")
            self.emoji = True

    @tasks.loop(hours=1)
    async def clear_emojis(self):
        self.emoji = False

def setup(client):
    client.add_cog(emoji_reply(client))