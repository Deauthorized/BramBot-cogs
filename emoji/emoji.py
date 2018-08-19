
import io
import os
import aiohttp
import discord
from redbot.core import commands
from redbot.core.utils.chat_formatting import box, pagify


class Emoji:

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)

    @commands.command(pass_context=True)
    async def emoji(self, ctx, emoji):
        """Enlarge a server emoji"""
        # print(emoji)
        if emoji is discord.Emoji:
            await ctx.channel.trigger_typing()
            emoji_name = emoji.name
            ext = emoji.url.split(".")[-1]
            async with self.session.get(emoji.url) as resp:
                data = await resp.read()
            file = discord.File(io.BytesIO(data),filename="{}.{}".format(emoji.name, ext))
            await ctx.send(file=file)
            # await self.bot.say(emoji.url)
        else:
            emoji_id = emoji.split(":")[-1].replace(">", "")
            if not emoji_id.isdigit():
                return
            await ctx.channel.trigger_typing()
            # print(emoji_id)
            if emoji.startswith("<a"):
                async with self.session.get("https://cdn.discordapp.com/emojis/{}.gif?v=1".format(emoji_id)) as resp:
                    data = await resp.read()
                file = discord.File(io.BytesIO(data),filename="{}.gif".format(emoji_id))
            else:
                async with self.session.get("https://cdn.discordapp.com/emojis/{}.png?v=1".format(emoji_id)) as resp:
                    data = await resp.read()
                file = discord.File(io.BytesIO(data),filename="{}.png".format(emoji_id))
            await ctx.send(file=file)
    
    @commands.command()
    async def oof(self, ctx):
        """oof"""
        emojis = ["🅾", "🇴", "🇫"]
        channel = ctx.message.channel
        guild = ctx.message.guild
        if not channel.permissions_for(guild.me).manage_messages:
            async for message in channel.history(limit=2):
                msg = message
            for emoji in emojis:
                await message.add_reaction(emoji)
        else:
            await ctx.message.delete()
            async for message in channel.history(limit=1):
                msg = message
            for emoji in emojis:
                await message.add_reaction(emoji)
