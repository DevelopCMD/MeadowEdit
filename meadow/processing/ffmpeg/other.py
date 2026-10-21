import discord
from discord.ext import commands

import config
import os
import processing.mediatype
import asyncio
import utils.tempname
import subprocess

async def speed(file, sp):
    outname = reserve_tempfile("mp4")
    await subprocces.run(command, check=True, capture_output=True, text=True)