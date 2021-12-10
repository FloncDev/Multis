import discord
from discord.ext import commands

class ready(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("-=-=-=-=-=-=-=-")
        print("Logged in as")
        print(f"Bot Name: {self.client.user.name}")
        print(f"Bot ID: {self.client.user.id}")
        print(f"Discord.py version: {discord.__version__}")
        print("-=-=-=-=-=-=-=-")

        # owner = self.client.get_user(275709752875548674)
        # await owner.send("Bot is online - v2 BETA")

def setup(client):
    client.add_cog(ready(client))