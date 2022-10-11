import discord
import random
from discord.ext import commands

class Embeds(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name='create-embed', help='creates embed')
  async def embed(self, ctx, header, *args):
    embed = discord.Embed(colour=0xafbecd)
    embed.add_field(name=header, value=args)
    try:
      await ctx.send(embed=embed)
    except discord.HTTPException:
       await ctx.send("Embed creation failed!")


def setup(bot):
    bot.add_cog(Embeds(bot))
    