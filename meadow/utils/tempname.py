import discord
from discord.ext import commands

import os
import random
import string
import tempfile

def get_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def temp_file_name(extension=None):
    while True:
        name = os.path.join(temp_directory, get_random_string(8))
        if extension:
            name += f".{extension}"
        if not is_named_used(name):
            return name

def reserve_tempfile(arg):
    if arg is None:  # default
        arg = temp_file_name()
    elif "." not in arg:  # just extension
        arg = temp_file_name(arg)