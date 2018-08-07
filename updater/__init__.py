from .updater import Updater

def setup(bot):
    bot.add_cog(Updater(bot))
