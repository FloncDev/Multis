import discord
from discord.ext import commands
from discord.ext.commands.core import group
import json

def loadJson():
        with open("json/serverConfig.json", "r") as file:
            data = json.load(file)

        with open("json/suggestions.json", "r") as file:
            suggestions = json.load(file)

        return data, suggestions

def write(suggestions):
    with open("json/suggestions.json", "w") as file:
        json.dump(suggestions, file, indent=2)

class cog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def suggest(self, ctx, *, suggestion):
        data, suggestions = loadJson()
        data = data[str(ctx.guild.id)]

        if data["suggestionChannel"] and data["downvoteEmoji"] and data["upvoteEmoji"]:

            suggestionChannel = self.client.get_channel(int(data["suggestionChannel"]))
            member = ctx.guild.get_member(ctx.author.id)

            embed=discord.Embed(description=suggestion, colour=member.color)
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            embed.set_footer(text="ID:")

            message = await suggestionChannel.send(embed=embed)

            await message.add_reaction(data["upvoteEmoji"])
            await message.add_reaction(data["downvoteEmoji"])
            await message.add_reaction("🚫")

            embed.set_footer(text=f"Message id: {message.id}")

            await message.edit(embed=embed)

            suggestions[str(ctx.guild.id)][str(message.id)] = {
                "body": suggestion,
                "messageId": message.id,
                "authorId": ctx.author.id
            }


            write(suggestions)

        else:
            await ctx.send("Please setup a suggestion channel, upvote emoji and downvote emoji.")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        data, suggestions = loadJson()
        if payload.emoji.name == "🚫" and not self.client.get_user(payload.user_id).bot:
            if data[str(payload.guild_id)]["suggestionChannel"] and data[str(payload.guild_id)]["downvoteEmoji"] and data[str(payload.guild_id)]["upvoteEmoji"]:
                    if suggestions[str(payload.guild_id)][str(payload.message_id)]:
                        channel = self.client.get_channel(int(data[str(payload.guild_id)]["suggestionChannel"]))
                        message = channel.get_partial_message(payload.message_id)
                        guild = self.client.get_guild(payload.guild_id)
                        member = guild.get_member(payload.user_id)

                        if channel.permissions_for(member).manage_messages or member.id == suggestions[str(guild.id)][str(payload.message_id)]["authorId"]:
                            await message.delete()
                            del suggestions[str(guild.id)][str(payload.message_id)]
                            write(suggestions)

                        else:
                            await message.remove_reaction("🚫", member)

    @group()
    async def suggestions(self, ctx):
        pass

    @suggestions.command()
    async def edit(self, ctx):
         data, suggestions = loadJson()

    @suggestions.command()
    async def respond(self, ctx, id, *, response):
        data, suggestions = loadJson()


def setup(client):
    client.add_cog(cog(client))