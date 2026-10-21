import discord, asyncio
from discord import app_commands
from discord.ext import commands

# libs
import os 
import sys 
import json

# bot data
from meadow.commands.other import Other

sys.path.insert(0, os.getcwd())

import config

class MyBot(commands.AutoShardedBot):
    async def setup_hook(self):
        await asyncio.gather(
            bot.add_cog(Other(bot))
        )

    async def on_ready(self):
        print(f"Logged in")
        sync = await bot.tree.sync()
        print(f"Synced {len(sync)} commands")

if __name__ == "__main__":
    intents = discord.Intents.all()
    intents.message_content = True
    bot = MyBot(command_prefix=config.prefix,shard_count=config.shard_count,case_insensitive=True,intents=intents)
    bot.run(config.discord_token)