import discord
from discord.ext import commands
import json

async def loadJSON():
    with open("json/economy.json", "r") as file:
        return json.load(file)

class Cog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        data = await loadJSON()

        for guild in self.client.guilds:
            guild = data[str(guild.id)]
            for member in guild.members:
                if not guild[str(member.id)]:
                    guild[str(member.id)] = {
                        "balance": 100
                    }
        

        with open("json/userConfig.json", "w") as output:
            json.dump(data, output)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        pass

def setup(client):
    client.add_cog(Cog(client))