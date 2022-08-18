from pydoc import describe
from discord.ext import commands
import discord

class Events(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(member:discord.Member):
        if member.guild.system_channel:
            embed = discord.Embed(title="Welcome to the server!", description=f"{member.mention} has joined the server!", color=0x00ff00)
            embed.set_thumbnail(url=member.avatar_url)
            await member.guild.system_channel.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_member_remove(member:discord.Member):
        if member.guild.system_channel:
            embed = discord.Embed(title="We will Try to miss you!", description=f"{member.mention} ({member.id}) has decided to leave us for the good!", color=0xffff)
            embed.set_thumbnail(url=member.avatar.url)
            await member.guild.system_channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Events(bot))
    print("Loaded Events")