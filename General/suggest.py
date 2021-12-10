import discord
from discord.ext import commands
from discord.ext.commands.core import group
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle
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

class suggest(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["s"])
    async def suggest(self, ctx, *, suggestion):
        data, suggestions = loadJson()
        data = data[str(ctx.guild.id)]

        if data["suggestionChannel"] and data["downvoteEmoji"] and data["upvoteEmoji"]:

            suggestionChannel = self.client.get_channel(int(data["suggestionChannel"]))
            member = ctx.guild.get_member(ctx.author.id)

            embed=discord.Embed(description=suggestion, colour=member.color)
            embed.set_author(name=ctx.author)
            # embed.set_footer(text="ID:")

            message = await suggestionChannel.send(embed=embed)

            await message.add_reaction(data["upvoteEmoji"])
            await message.add_reaction(data["downvoteEmoji"])
            await message.add_reaction("🚫")
            await message.add_reaction("💬")

            # embed.set_footer(text=f"Message id: {message.id}")

            # await message.edit(embed=embed)

            suggestions[str(ctx.guild.id)][str(message.id)] = {
                "body": suggestion,
                "messageId": message.id,
                "authorId": ctx.author.id,
                "threadId": None
            }


            write(suggestions)

        else:
            await ctx.send("Please setup a suggestion channel, upvote emoji and downvote emoji.")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        data, suggestions = loadJson()
        data = data.get(str(payload.guild_id))
        suggestion = suggestions.get(str(payload.guild_id)).get(str(payload.message_id))
        if payload.emoji.name == "🚫" and not self.client.get_user(payload.user_id).bot:
            if data["suggestionChannel"] and data["downvoteEmoji"] and data["upvoteEmoji"]:
                    if suggestion:
                        channel = self.client.get_channel(int(data["suggestionChannel"]))
                        message = channel.get_partial_message(payload.message_id)
                        guild = self.client.get_guild(payload.guild_id)
                        member = guild.get_member(payload.user_id)

                        if channel.permissions_for(member).manage_messages or member.id == suggestion["authorId"]:
                            await message.delete()
                            if suggestion["threadId"]:
                                await guild.get_thread(suggestion["threadId"]).delete()
                            del suggestions[str(guild.id)][str(payload.message_id)]
                            write(suggestions)

                        else:
                            await message.remove_reaction("🚫", member)

        if payload.emoji.name == "💬" and not self.client.get_user(payload.user_id).bot:
            if data["suggestionChannel"] and data["downvoteEmoji"] and data["upvoteEmoji"]:
                    if suggestion and not suggestion["threadId"]:
                        channel = self.client.get_channel(int(data["suggestionChannel"]))
                        message = await channel.fetch_message(payload.message_id)
                        guild = self.client.get_guild(payload.guild_id)
                        member = guild.get_member(payload.user_id)
                        author = self.client.get_user(suggestion["authorId"])

                        
                        thread = await message.start_thread(name=suggestion["body"], auto_archive_duration=60)
                        suggestion["threadId"] = thread.id
                        await thread.add_user(author)
                        await thread.send(f"{member.mention} started this thread.")

                        await message.remove_reaction("💬", member)
                        await message.remove_reaction("💬", guild.get_member(792801822594301952))
                        suggestions[str(payload.guild_id)][str(payload.message_id)] = suggestion
                        write(suggestions)

    @group()
    async def suggestions(self, ctx):
        pass

    @suggestions.command()
    async def edit(self, ctx):
         data, suggestions = loadJson()


def setup(client):
    client.add_cog(suggest(client))