import discord
from discord.ext import commands
import random
import config

from os import listdir

description = '''Specially made bot for my own server nothing more '''

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='?', description=description, intents=intents)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# load cogs from cogs directory

for cog in listdir('cogs'):
    if cog.endswith('.py'):
        if not cog.startswith("_"):
            bot.load_extension(f'cogs.{cog[:-3]}')
            # slice to remove `.py` from the end of the file name
            print("Loaded cog: " + cog[:-3])

bot.load_extension('jishaku')
bot.run(config.token)