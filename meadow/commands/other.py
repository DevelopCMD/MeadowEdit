import discord
from discord.ext import commands

class Other(commands.Cog, name="Other"):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.hybrid_command()
    async def ping(self, ctx: commands.Context):
        """
        Check the latency of the bot.
        """
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")