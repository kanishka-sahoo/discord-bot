import discord
import random
from discord.ext import commands

class Messaging(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  #Pings the bot to check for activity
  @commands.command(name='Ping', help='Ping the bot')
  async def ping(self, ctx):
      await ctx.send('Pong!')
  
  #Acts as a parrot, repeats the phrase
  @commands.command(name='say', help='Repeats the phrase')
  async def simon_says(self, ctx, *args):
    await ctx.send(' '.join(args))

  #Sends a dm to the mentioned User
  @commands.command(name='send-dm', help='sends a dm to mentioned user, admin only')
  @commands.has_role('admin')
  async def send_dm(self, ctx, member: discord.Member, *, content):
      channel = await member.create_dm()
      await channel.send(content)
      await ctx.send("Sent the dm...")

  #Reverses the sent text
  @commands.command(name='reverse', help='Reverses the sent text')
  async def reverse_message(self, ctx, *args):
    message_to_reverse = ' '.join(args)
    reversed_message = message_to_reverse[::-1]
    await ctx.send(reversed_message)

  #Like sa, but has cointdown
  @commands.command(name='time-say', help='say command, but has timeout. Write as >time-say `duration(secs)` `message`')
  async def time_say(self, ctx, duration: int, *args):
    args = ' '.join(args)
    if duration > 1000:
      return
    await ctx.channel.purge(limit=1)
    await ctx.send(args, delete_after=duration)

def setup(bot):
    bot.add_cog(Messaging(bot))