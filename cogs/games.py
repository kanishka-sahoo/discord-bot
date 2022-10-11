import discord
import random
from discord.ext import commands

class Games(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  #ADD THIS OR I WILL KILL YOU IN YOUR SLEEP
  @commands.command(name='hangman', help='coming soon')
  async def hangman_game(self, ctx):
    await ctx.send('I dont exist yet')

def setup(bot):
    bot.add_cog(Games(bot))