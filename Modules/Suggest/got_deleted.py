import discord
from discord.ext import commands
import sql
from console import Console
import json

console = Console()

class got_deleted(commands.Cog):

    def __init__(self, client):
        self.client = client
        with open("config.json", "r") as f:
            self.config = json.load(f)

    @commands.Cog.listener()
    async def on_raw_message_delete(self, payload):
        if not sql.is_deleted(payload.message_id):
            guild = self.client.get_guild(payload.guild_id)
            channel = guild.get_channel(payload.channel_id)

            if payload.channel_id == self.config.get("suggestion_channel"):
                sql.delete_suggestion(payload.message_id)
                console.log(f"Suggestion deleted by force: {payload.message_id}.")

def setup(client):
    client.add_cog(got_deleted(client))