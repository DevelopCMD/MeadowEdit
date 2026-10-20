import discord
from discord import app_commands
from discord.ext import commands

class Other(commands.Cog, name="Other"):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.hybrid_command(name="ping", description="Replies with Pong!")
    async def ping(self, ctx: commands.Context):
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")