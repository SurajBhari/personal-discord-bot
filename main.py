import discord
from discord.ext import commands
import random
import config
import asyncio

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

async def load_extensions():
    for filename in listdir("./cogs"):
        if filename.endswith('.py'):
            if not filename.startswith("_"):
                await bot.load_extension(f'cogs.{filename[:-3]}')
                # slice to remove `.py` from the end of the file name
                print("Loaded cog: " + filename[:-3])

    await bot.load_extension('jishaku')


async def main():
    async with bot:
        await load_extensions()
        await bot.start(config.token)

asyncio.run(main())
