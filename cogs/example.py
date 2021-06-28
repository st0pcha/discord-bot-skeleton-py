import config

import discord
from discord.ext import commands

class CogName(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener() # bot event
    async def on_ready(self):
        print("Bot is ready!")

    @commands.command() # bot command
    async def test(self, ctx):
        await ctx.send("Test")

        
def setup(bot):
    bot.add_cog(CogName(bot))
