import discord
from discord.ext import commands
from console import Console

console = Console(True)

class pin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def pin(self, ctx):
        originalChannel = self.client.get_channel(ctx.message.reference.channel_id)
        originalMessage = await originalChannel.fetch_message(ctx.message.reference.message_id)
        pinChannel = self.client.get_channel(787508205634715679)

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

        console.log(f"{ctx.author}({ctx.author.id}) Pinned message {originalMessage.id} in #{originalChannel.name}({originalChannel.id}).")

def setup(client):
    client.add_cog(pin(client))