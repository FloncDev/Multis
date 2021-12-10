import discord
from discord.ext import commands
import sys
from io import StringIO
import contextlib

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

class debug(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def debug(self, ctx, *, code):
        """Evaluates Python code."""
        env = {
            'client': self.client,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message
        }

        env.update(globals())

        try:
            if code.count("`") >= 6:
                code = code.replace("```py", "")
                code = code.replace("```", "")

            code.replace("\`\`\`", "```")

            with stdoutIO() as output:
                exec(code, env)
            await ctx.send("```" + output.getvalue() + "```")
        except Exception as e:
            await ctx.send(f'```py\n{e.__class__.__name__}: {e}```')

def setup(client):
    client.add_cog(debug(client))