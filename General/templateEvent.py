import discord
from discord.ext import commands
import json

class RENAME_ME_EVENT(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        pass

def setup(client):
    client.add_cog(RENAME_ME_EVENT(client))