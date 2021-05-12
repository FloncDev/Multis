from Administration.settings import write
import discord
from discord import colour
from discord.ext import commands
import json

from discord.ext.commands.core import command

def getJson():
    with open("json/serverConfig.json", "r") as file:
        data = json.load(file)
    with open("json/pins.json", "r") as file:
        return data, json.load(file)

def writeJson(pins):
    with open("json/pins.json", "w") as file:
        json.dump(pins, file)

class cog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        data, pins = getJson()
        if data[str(payload.guild_id)]["pinChannel"] and data[str(payload.guild_id)]["pinAmount"]:
            channelId = int(data[str(payload.guild_id)]["pinChannel"])
            if payload.channel_id != channelId and payload.emoji.name == "⭐":
                if pins.get(str(payload.message_id), False) == False:
                    channel = self.client.get_channel(payload.channel_id)
                    message = await channel.fetch_message(payload.message_id)
                    stars = 0
                    user = self.client.get_user(message.author.id)
                    guild = self.client.get_guild(payload.guild_id)
                    member = guild.get_member(message.author.id)
                    for i in message.reactions:
                        if i.emoji == "⭐":
                            stars = i.count
                    if stars >= int(data[str(payload.guild_id)]["pinAmount"]):
                        try:
                            image = message.attachments[0].proxy_url
                        except:
                            image = None
                        
                        pinChannel = guild.get_channel(channelId)
                        if len(message.clean_content) < 1950:
                            embed = discord.Embed(title=message.clean_content, description=f"[Link]({message.jump_url})", colour=member.colour) # Yes, i'm britsh and spell it colour.
                            if image != None: embed.set_image(url=image)
                            embed.set_author(name=user, icon_url=user.avatar_url)
                        else:
                            embed = discord.Embed(description=f"{message.clean_content}\n\n[Link]({message.jump_url})", colour=member.colour)
                            if image != None: embed.set_image(url=image)
                            embed.set_author(name=user, icon_url=user.avatar_url)
                        
                        await pinChannel.send(embed=embed)
                        pins[str(payload.message_id)] = True

                        writeJson(pins)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def pin(self, ctx):
        config, data = getJson()
        originalChannel = self.client.get_channel(ctx.message.reference.channel_id)
        message = await originalChannel.fetch_message(ctx.message.reference.message_id)
        channelId = int(config[str(ctx.guild.id)]["pinChannel"])
        user = self.client.get_user(message.author.id)
        member = ctx.guild.get_member(message.author.id)
        try:
            image = message.attachments[0].proxy_url
        except:
            image = None
        
        pinChannel = ctx.guild.get_channel(channelId)
        if len(message.clean_content) < 256:
            embed = discord.Embed(title=message.clean_content, description=f"[Link]({message.jump_url})", colour=member.colour) # Yes, i'm britsh and spell it colour.
            if image != None: embed.set_image(url=image)
            embed.set_author(name=user, icon_url=user.avatar_url)
        else:
            embed = discord.Embed(description=f"{message.clean_content}\n\n[Link]({message.jump_url})", colour=member.colour)
            if image != None: embed.set_image(url=image)
            embed.set_author(name=user, icon_url=user.avatar_url)
        
        await pinChannel.send(embed=embed)


def setup(client):
    client.add_cog(cog(client))