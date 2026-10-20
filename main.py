import discord, asyncio
from discord import app_commands
from discord.ext import commands

# libs
import os 
import sys 
import json

# cogs
from cogs.other import Other

with open("config.json", "r") as f:
    config = json.load(f)

bot_prefix          = config["prefix"]
bot_tempdir         = config["temp_directory"]
bot_storagedir      = config["data_directory"]
bot_token           = config["discord_token"]
bot_maxfilesize     = config["max_file_size"]
bot_shards          = config["shard_count"]

class MyBot(commands.AutoShardedBot):
    async def setup_hook(self):
        await asyncio.gather(
            bot.add_cog(Other(bot))
        )

    async def on_ready(self):
        print(f"Logged in")

if __name__ == "__main__":
    intents = discord.Intents.all()
    intents.message_content = True
    bot = MyBot(command_prefix=bot_prefix,shard_count=bot_shards,case_insensitive=True,intents=intents)
    bot.run(bot_token)