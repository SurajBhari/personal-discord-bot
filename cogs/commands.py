from pydoc import describe
from discord.ext import commands
import discord
import random

class Commands(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @commands.command(name='8ball')
    async def eight_ball(self, ctx, *, question):
        answers = ['It is certain', ' It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', ' As I see it, yes', ' Most likely', ' Outlook good', ' Yes', ' Signs point to yes', ' Reply hazy, try again', ' Ask again later', ' Better not tell you now', ' Cannot predict now', ' Concentrate and ask again', "Dont count on it", ' My reply is no', ' My sources say no', ' Outlook not so good', ' Very doubtful']
        answer = random.choice(answers)
        embed = discord.Embed(title=answer, description=question,   color=discord.Color.blue())
        await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Commands(bot))
    print("Loaded Events")