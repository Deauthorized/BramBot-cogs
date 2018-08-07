import discord
from discord.ext import commands
from redbot.core import checks


class Ping:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Ping the shard and latency"""
        latencies = self.bot.latencies
        msg = ""
        for shard, pingt in latencies:
            msg += "Shard {}/{}: {}ms\n".format(shard + 1, len(latencies), round(pingt*1000))
        em = discord.Embed(title=msg, colour=0x3d464c)
        await ctx.send(embed=em)
