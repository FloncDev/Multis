import discord
from discord.ext import commands
import json

async def loadJSON():
    return json.loads(open("json/userConfig.json", "r").read())

class Cog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        data = await loadJSON()

        for guild in self.client.guilds:
            for member in guild.members:
                try:
                    balance = data[str(member.id)]["balance"]
                except:
                    data[str(member.id)] = {
                        "balance": 100
                    }
        

        with open("json/userConfig.json", "w") as output:
            json.dump(data, output, indent=2)

def setup(client):
    client.add_cog(Cog(client))