from discord.ext import commands
import discord
import asyncio


class MyHelpCommand(commands.MinimalHelpCommand):
    def get_command_signature(self, command):
        string = (
            f"**{command.name}**"
            f"\n"
            f"\n"
            f"Usage-\n"
            f"```{self.clean_prefix}{command.qualified_name} {command.signature}```"
            f"\n"
        )
        return string

    async def send_bot_help(self, mapping):
        description = (
            f"```css\n"
            f"+ [] Means optional argument.\n"
            f"+ () Means mandatory argument.\n"
            f"+ {self.clean_prefix}help [command | cog] for help on a specific command/cog"
            f"```"
        )
        embed = discord.Embed(description=description, colour=0x00FF00)
        cogs = self.context.bot.cogs
        cogs = sorted(cogs)
        for cog in cogs:
            text = ""
            for command in cog.get_commands():
                text += "\n"
                text += self.get_command_signature(command=command)
            embed.add_field(name=str(cog), value=text)
        destination = self.get_destination()
        await destination.send(embed=embed)

    async def send_command_help(self, command):
        embed = discord.Embed(
            title=command.qualified_name,
            description=f"{command.description}\n```{self.clean_prefix}{command.qualified_name} {command.signature}```",
            colour=0x00FFFF,
        )
        if command.aliases:
            embed.add_field(
                name="**Aliases**", value=" ".join([f"`{x}`" for x in command.aliases])
            )
        destination = self.get_destination()
        await destination.send(embed=embed)

    async def send_group_help(self, group):
        embed = discord.Embed(
            title=group.qualified_name,
            description=f"```{self.clean_prefix}{group.qualified_name} {group.signature}```",
            colour=0x00FFFF,
        )
        value = ""
        if group.commands:
            for command in group.commands:
                value = (
                    value
                    + "\n"
                    + f"`{self.clean_prefix}{command.qualified_name} {command.signature}` "
                    f"  {command.description}"
                )
            embed.add_field(name="Sub Commands", value=value)

        destination = self.get_destination()
        await destination.send(embed=embed)

    async def send_cog_help(self, cog):
        embed = discord.Embed(title=str(cog), color=0x00FFFF)
        text = "```\n"
        for command in cog.get_commands():
            text += self.get_command_signature(command)
            text += "\n"
        text += "```"
        embed.description = text
        destination = self.get_destination()
        await destination.send(embed=embed)


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._original_help_command = client.help_command
        client.help_command = MyHelpCommand()
        client.help_command.cog = self
        print("SOMETHING happened")

    def cog_unload(self):
        self.bot.help_command = self._original_help_command


async def setup(client):
    await client.add_cog(Help(client))
    print("something happened")
