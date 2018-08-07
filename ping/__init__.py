from .pinginfo import Pinginfo


def setup(bot):
    bot.add_cog(Pinginfo(bot))
