import discord
import random
from discord.ext import commands

class Admins(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  

  #Adds a new text channel to the guild
  @commands.command(name='create-channel', help='Create a channel, admin only')
  @commands.has_role('admin')
  async def create_channel(self, ctx, channel_name='real-python'):
      guild = ctx.guild
      existing_channel = discord.utils.get(guild.channels, name=channel_name)
      if not existing_channel:
          await ctx.send(f'Creating a new channel: {channel_name}')
          await guild.create_text_channel(channel_name)

  #Removes a given text or voice channel
  @commands.command(name='delete-channel', help='delete a channel with the specified name')
  async def delete_channel(self, ctx, channel_name):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if existing_channel is not None:
      await ctx.send(f'Deleting the channel: {channel_name}')
      await existing_channel.delete()
    else:
      await ctx.send(f'No channel named, "{channel_name}", was found')

  

def setup(bot):
    bot.add_cog(Admins(bot))
  