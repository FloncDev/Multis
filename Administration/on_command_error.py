import discord
from discord.ext import commands
import json

class errors(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        output = ""
        if isinstance(error, commands.MissingRequiredArgument): output = "You are missing a required argument."
        elif isinstance(error, commands.CommandNotFound): output = None
        elif isinstance(error, commands.BotMissingPermissions): output = "The bot doesn not have permission to do this."
        elif isinstance(error, commands.MissingPermissions): output = "You do not have permission to do this."
        else: output = f"An unkown error has occured.\n```{error}```"

        if output != None: await ctx.reply(embed=discord.Embed(title=output, colour=0xff0000))
        await ctx.message.add_reaction("❌")

def setup(client):
    client.add_cog(errors(client))