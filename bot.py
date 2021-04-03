import discord
import config
from discord.ext import commands

bot = commands.Bot(
    command_prefix=config.bot_prefix, # bot prefix
)
bot.remove_command("help") # remove standart help command (by discord.py)

for cog in config.cogs: # get all cogs in config (cogs)
    bot.load_extension(cog) # load cogs.?

bot.run(config.bot_token) # run bot