import discord
from redbot.core import checks, commands

class Prefixes:

    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command('set serverprefix')

    @commands.command()
    @commands.guild_only()
    @checks.admin_or_permissions(manage_server=True)
    async def prefix(self, ctx, *prefixes):
        """Sets server prefix(es)"""

        if not prefixes:
            await ctx.bot.db.guild(ctx.guild).prefix.set([])
            em = discord.Embed(description="Guild prefixes have been reset.", 
                colour=(await ctx.embed_colour()))
            await ctx.send(embed=em)
            return
        prefixes = sorted(prefixes, reverse=True)
        await ctx.bot.db.guild(ctx.guild).prefix.set(prefixes)

        if ctx.guild:
            prefixes = await ctx.bot.db.guild(ctx.guild).prefix()
        else:
            prefixes = None
        if not prefixes:
            prefixes = await ctx.bot.db.prefix()
        
        prefix_string = " ".join(prefixes)

        em = discord.Embed(description="Prefix set to `{}`".format(prefix_string), colour=(await ctx.embed_colour()))
        await ctx.send(embed=em)
    
    @commands.command()
    @commands.guild_only()
    async def prefixes(self, ctx):
        """List server prefix(es)"""

        if ctx.guild:
            prefixes = await ctx.bot.db.guild(ctx.guild).prefix()
        else:
            prefixes = None
        if not prefixes:
            prefixes = await ctx.bot.db.prefix()
        
        prefix_string = " ".join(prefixes)

        em = discord.Embed(description="Guild's current prefixes: `{}`".format(prefix_string), colour=(await ctx.embed_colour()))
        await ctx.send(embed=em)
