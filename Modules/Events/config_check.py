import discord
from discord.ext import commands
import json
from console import Console

console = Console(True)

class config_check(commands.Cog):

    def __init__(self, client):
        self.client = client
        with open("config.json", "r") as f:
            self.config = json.load(f)

    @commands.Cog.listener()
    async def on_ready(self):
        keys = []
        for key in self.config:
            if not self.config.get(key):
                keys.append(key)

        if len(keys) == 1:
            console.error(f"{key} is not set in config.json")
            await self.client.close()

        elif len(keys) > 1:
            console.error(", ".join(keys) + " are not set in config.json")

def setup(client):
    client.add_cog(config_check(client))