import discord
from discord.ext import commands
import sql
import json
from console import Console

console = Console(True)

class stars(commands.Cog):

    def __init__(self, client):
        self.client = client
        with open("config.json", "r") as f:
            self.config = json.load(f)

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.emoji == "⭐":
            if reaction.count >= self.config.get("pin_amount") and not sql.is_pinned(reaction.message.id):
                sql.add_pin(reaction.message.id, reaction.message.channel.id)

                originalChannel = self.client.get_channel(reaction.message.channel.id)
                originalMessage = await originalChannel.fetch_message(reaction.message.id)
                pinChannel = self.client.get_channel(self.config.get("pin_channel"))

                try:
                    image = originalMessage.attachments[0].proxy_url
                except:
                    image = None

                content = originalMessage.clean_content

                if len(content) < 256:
                    embed = discord.Embed(title=content, description=f"[Link]({originalMessage.jump_url})", color=originalMessage.author.color)
                else:
                    embed = discord.Embed(description=f"{content}\n\n[Link]({originalMessage.jump_url})", color=originalMessage.author.color)
                
                if image: embed.set_image(url=image)
                embed.set_author(name=originalMessage.author, icon_url=originalMessage.author.avatar.url)

                await pinChannel.send(embed=embed)


def setup(client):
    client.add_cog(stars(client))