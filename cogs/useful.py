import discord
import random
from discord.ext import commands

class Useful(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  #uses eval() to solve basic math
  @commands.command(name='math', help='Does math problems for you')
  async def math_solver(self, ctx, *args):
    args = ''.join(args)
    if args == 'help':
      await ctx.send("OOPS")
      return
    await ctx.send(args)
    result = eval(args)
    await ctx.send('The result is ' + str(result))

def setup(bot):
    bot.add_cog(Useful(bot))