from discord.ext import commands
import discord

"""
Settings Module
    - Can not be disabled.

Main settings:
    - Prefix
        - Prefixes
        - Auto Capitilization

    - Pins
        - Pin Channel
        - Pin Emoji     ! Changed to premade custom emojis
        - Pin Amount

    - Suggestions
        - Suggestion Upvote & Downvote Emoji    ! Changed to premade custom emojis
        - Suggestion Channel
        - Enable/Disable Threads

    - Polls
        - Auto-adding reactions
        - Tags such as CHOOSE-X, CREATE-THREAD, OPT-OUT
"""

class optionsButton(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Prev", style=discord.ButtonStyle.grey) # Change to emoji
    async def prev(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.value = "prev"
        self.stop()

    @discord.ui.button(label="Next", style=discord.ButtonStyle.grey) # Change to emoji
    async def next(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.value = "next"
        self.stop()

def getSettingsStatus(name: str):
    pass

class Settings(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group()
    async def settings(self, ctx):
        embed = discord.Embed(
            title="Settings",
            description="__Please enter the name of the settings you want to change.__"
        )
        embed.add_field(name="Prefix", value="This includes the ability to remove and add prefixes. Also whether or not you want the prefix to be case insensitive.", inline=True)
        embed.add_field(name="Pins" + f" - `{getSettingsStatus()}`", value="Pin channel and Pin amount.", inline=True)
        embed.add_field(name="Suggestions" + f" - `{getSettingsStatus()}`", value="Suggestion channel and whether or not threads are enabled.", inline=True)

        original_message = await ctx.send(embed=embed)

        message = await self.client.wait_for("message", check=lambda message: message.author == ctx.author and message.channel == ctx.channel)

        if message.lower() == "prefix":
            embed = discord.Embed(
                title="Prefixes",
                description="```!```"
            )

        elif message.lower() == "pins":
            pass

        elif message.lower() == "suggestions":
            pass

        else:
            await ctx.send("Invalid input. Please enter either prefix, pins or suggestions.")
            return


def setup(client):
    client.add_cog(Settings(client))