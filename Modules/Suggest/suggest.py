import discord
from discord.ext import commands
from discord.commands import slash_command, Option
from discord.ui import view
from console import Console
import sql
from datetime import datetime

console = Console(True)

class suggest(commands.Cog):

    def __init__(self, client):
        self.client = client
 
    @slash_command(guild_ids=[716611500256657469])
    async def suggest(self, ctx, suggestion: Option(str, description="The suggestion you want to make.")):
        suggestionChannel = self.client.get_channel(720939526314393610)
        member = ctx.guild.get_member(ctx.author.id)

        embed = discord.Embed(description=suggestion, color=member.colour) # Yes I'm british
        embed.set_author(name=member, icon_url=member.avatar.url)
        embed.timestamp = datetime.utcnow()

        message = await suggestionChannel.send(embed=embed)
        await ctx.respond("Done.", ephemeral=True)

        await message.add_reaction("<:upvote:912496476440117278>")
        await message.add_reaction("<:downvote:912739814728687647>")
        await message.add_reaction("<:delete:912496536959717407>")

        sql.create_suggestion(message.id, member.id, suggestion)

        console.log(f"{member}({member.id}) Used command suggest with argument: \"{suggestion}\".")

def setup(client):
    client.add_cog(suggest(client))