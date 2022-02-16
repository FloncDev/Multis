import discord
from discord.ext import commands
from discord.commands import slash_command, Option
import json
from console import Console
import sql
# from datetime import datetime

console = Console(True)
with open('config.json') as f:
    config = json.load(f)

class suggest(commands.Cog):

    def __init__(self, client):
        self.client = client
 
    @slash_command(guild_ids=[config.get("guild_id")]) # guild_ids=[config.get("guild_id")]
    async def suggest(self, ctx, suggestion: Option(str, description="The suggestion you want to make.")):
        suggestionChannel = self.client.get_channel(config.get("suggestion_channel"))
        member = ctx.guild.get_member(ctx.author.id)

        embed = discord.Embed(description=suggestion, color=member.colour)
        embed.set_author(name=member, icon_url=member.avatar.url)
        # embed.timestamp = datetime.utcnow()

        message = await suggestionChannel.send(embed=embed)
        await ctx.respond(message.jump_url, ephemeral=True)

        await message.add_reaction("<:upvote:912496476440117278>")
        await message.add_reaction(config.get("downvote_emoji"))
        await message.add_reaction(config.get("delete_emoji"))

        sql.create_suggestion(message.id, member.id, suggestion)

        console.log(f"{member}({member.id}) Used command suggest with argument: \"{suggestion}\".")

def setup(client):
    client.add_cog(suggest(client))