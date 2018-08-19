from .prefixes import Prefixes

def setup(bot):
    bot.add_cog(Prefixes(bot))