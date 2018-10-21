import discord
from redbot.core import commands
import lavalink

BaseCog = getattr(commands, "Cog", object)

class Thumbnail(BaseCog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def thumbnail(self, ctx):
        """Current songs thumbnail"""
        player = lavalink.get_player(ctx.guild.id)

        if self._player_check(ctx) and player.current:
            return await self._embed_msg(ctx)

        else:
            return await self._embed_error(ctx)

    @staticmethod
    def _player_check(ctx):
        try:
            lavalink.get_player(ctx.guild.id)
            return True
        except KeyError:
            return False

    @staticmethod
    async def _embed_msg(ctx):
        player = lavalink.get_player(ctx.guild.id)
        songid = player.current.uri.replace(
            "https://www.youtube.com/watch?v=", "")
        embed = discord.Embed(
            colour=(await ctx.embed_colour()
            ),
            title="Now playing: " + player.current.title,
            url=player.current.uri
        )
        embed.set_image(
            url="https://img.youtube.com/vi/{}/mqdefault.jpg".format(songid)
        )
        await ctx.send(embed=embed)

    @staticmethod
    async def _embed_error(ctx):
        embed = discord.Embed(
            colour=(await ctx.embed_colour()
            ),
            title="No song is currently playing."
        )
        await ctx.send(embed=embed)
