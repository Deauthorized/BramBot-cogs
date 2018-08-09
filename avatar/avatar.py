import discord
from discord.ext import commands
from redbot.core import checks

class Avatar:
	"""View a user's avatar"""

	def __init__(self,bot):
		self.bot = bot
    
	@commands.command(pass_context=True)
	async def avatar(self, ctx, user: discord.Member=None):
		"""Embed profile image!"""
		author = ctx.message.author
		em = discord.Embed()
		if not user:
			user = author
		if user.avatar_url:
			em.set_image(url=user.avatar_url)
		else:
			em.set_image(url=user.default_avatar_url)
		if await ctx.embed_requested():
            		await ctx.send(embed=em)
		else:
			await ctx.send(embed=em)
