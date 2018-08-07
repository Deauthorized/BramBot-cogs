import discord
from discord.ext import commands
import subprocess
import asyncio
from subprocess import Popen
import threading
from asyncio.subprocess import PIPE
from redbot.core.utils.chat_formatting import pagify

class Updater:
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["updateme"])
    @commands.is_owner()
    async def updater(self, ctx):
        """Attempt to update bot version"""
        await ctx.send("Attemping to update...")
        proc = await asyncio.create_subprocess_shell("redbot-launcher --update-dev", stdin=None, stderr=None, stdout=PIPE)
        out = await proc.stdout.read()
        msg = pagify(out.decode('utf-8'))
        #await ctx.send(f"```ini\n\n[Bash Input]: {arg}\n```")
        
        for page in msg:
            await ctx.send("```py\n\n{}```".format(page))
        await ctx.send("Restart bot to apply update")