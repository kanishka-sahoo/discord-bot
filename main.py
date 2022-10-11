# bot.py
import os
import random
import asyncio
import ctypes
import struct

# Adds the main discord api functions
from discord.ext import commands
from dotenv import load_dotenv
import discord
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Bot Command Prefix
bot = commands.Bot(command_prefix='?')

init_extensions = ['cogs.general',
                   'cogs.messaging', 
                   'cogs.admins', 
                   'cogs.games', 
                   'cogs.useful']

if __name__ == '__main__':
    for extension in init_extensions:
        bot.load_extension(extension)



#Informs user if incorrect role
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')









# Final line
bot.run(TOKEN)
