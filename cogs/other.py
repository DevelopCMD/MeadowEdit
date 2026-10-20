import discord
from discord import app_commands
from discord.ext import commands

class Other(commands.Cog, name="Other"):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.hybrid_command()
    async def ping(self, ctx: commands.Context):
        """
        Ping. Yes.
        You know.
        """
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")