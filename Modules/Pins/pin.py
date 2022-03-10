import discord
from discord.ext import commands
from discord.commands import permission
from console import Console
import json
import sql

console = Console(True)

class pin(commands.Cog):

    def __init__(self, client):
        self.client = client
        with open("config.json", "r") as f:
            self.config = json.load(f)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def pin(self, ctx):
        try:
            if not sql.is_pinned(ctx.message.reference.message_id):
                originalChannel = self.client.get_channel(ctx.message.reference.channel_id)
                originalMessage = await originalChannel.fetch_message(ctx.message.reference.message_id)
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

                sql.add_pin(ctx.message.reference.message_id, ctx.message.reference.channel_id)

                console.log(f"{ctx.author}({ctx.author.id}) Pinned message {originalMessage.id} in #{originalChannel.name}({originalChannel.id}).")

            else:
                await ctx.send("That message is already pinned.")
        except:
            await ctx.send("Please reply to a message.")

    @commands.message_command(name="Pin Message", guild_ids=[716611500256657469])
    @permission(discord.has_role("Staff"))
    async def pin_message(self, ctx, message: discord.Message):
        if not sql.is_pinned(message.id):
            pinChannel = self.client.get_channel(self.config.get("pin_channel"))

            try:
                image = message.attachments[0].proxy_url
            except:
                image = None

            content = message.clean_content

            if len(content) < 256:
                embed = discord.Embed(title=content, description=f"[Link]({message.jump_url})", color=message.author.color)
            else:
                embed = discord.Embed(description=f"{content}\n\n[Link]({message.jump_url})", color=message.author.color)
            
            if image: embed.set_image(url=image)
            try: embed.set_author(name=message.author, icon_url=message.author.avatar.url)
            except: embed.set_author(name=message.author)

            sentMessage = await pinChannel.send(embed=embed)

            try: await sentMessage.publish()
            except: pass

            await ctx.respond(f"Message pinned!")

            sql.add_pin(message.id, message.channel.id)

            console.log(f"{message.author}({message.author.id}) Pinned message {message.id} in #{pinChannel} by app command.")

        else:
            await ctx.respond("Message is already pinned.", ephemeral=True)

def setup(client):
    client.add_cog(pin(client))