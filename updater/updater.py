import discord
from redbot.core import commands
import subprocess
import asyncio
from subprocess import Popen
import threading
from asyncio.subprocess import PIPE
from redbot.core.utils.chat_formatting import pagify

BaseCog = getattr(commands, "Cog", object)

class Updater(BaseCog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["updater"])
    @commands.is_owner()
    async def update(self, ctx):
        """Attempt to update bot version"""
        await ctx.send("Attemping to update...")
        proc = await asyncio.create_subprocess_shell("pip3 install -U --process-dependency-links --force-reinstall --user  --no-cache-dir Red-DiscordBot[voice]",
                                                     stdin=None, stderr=None, stdout=PIPE)
        out = await proc.stdout.read()
        msg = pagify(out.decode('utf-8'))

        for page in msg:
            await ctx.send("```py\n\n{}```".format(page))
        await ctx.send("Restart bot to apply changes.")
