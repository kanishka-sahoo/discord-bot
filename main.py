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
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='?', intents=intents)

init_extensions = ['cogs.general',
                   'cogs.messaging', 
                   'cogs.admins', 
                   'cogs.games', 
                   'cogs.useful']

async def setup_bot():
    for extension in init_extensions:
        await bot.load_extension(extension)


if __name__ == '__main__':
    asyncio.run(setup_bot())



#Informs user if incorrect role
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')









# Final line
bot.run(TOKEN)
