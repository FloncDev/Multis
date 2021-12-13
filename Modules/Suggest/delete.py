import discord
from discord.ext import commands
import sql
from console import Console
import json

console = Console(True)

class delete(commands.Cog):

    def __init__(self, client):
        self.client = client
        with open("config.json", "r") as f:
            self.config = json.load(f)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.user_id == self.client.user.id: return
        author = sql.get_author(payload.message_id)
        guild = self.client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        channel = self.client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)

        if str(payload.emoji) == self.config.get("delete_emoji"):
            if payload.user_id == author or member.guild_permissions.manage_messages:

                await message.delete()
                sql.delete_suggestion(payload.message_id)
                console.log(f"{member}({member.id}) Deleted suggestion {message.id}.")

            else:
                await message.remove_reaction(payload.emoji, member)

def setup(client):
    client.add_cog(delete(client))