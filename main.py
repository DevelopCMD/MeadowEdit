import discord, asyncio
from discord import app_commands
from discord.ext import commands

# libs
import os 
import sys 
import json

# cogs
from cogs.other import Other

sys.path.insert(0, os.getcwd())

with open("config.json", "r") as f:
    config = json.load(f)

# variables
prefix = config["prefix"]
shard_count = config["shard_count"]
token = config["discord_token"]

class MyBot(commands.AutoShardedBot):
    async def setup_hook(self):
        await bot.tree.sync()
        await asyncio.gather(
            bot.add_cog(Other(bot))
        )

    async def on_ready(self):
        print(f"Logged in")

if __name__ == "__main__":
    intents = discord.Intents.all()
    intents.message_content = True
    bot = MyBot(command_prefix=prefix,shard_count=shard_count,case_insensitive=True,intents=intents)
    bot.run(token)