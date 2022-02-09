import codes #delete before pulling
import os
import discord
import re
import datetime
from discord.ext import commands, tasks
import sys, traceback
from hangintherebuster import keep_alive

# Below cogs represents our folder our cogs are in. Following is the file name. So 'audio.py' in cogs, would be cogs.audio
# Think of it like a dot path import
initial_extensions = ['cogs.audio', 'cogs.text_individ']
bot = commands.Bot(command_prefix="!")

# Here we load our extensions(cogs) listed above in [initial_extensions].
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    print('{0.user} on standby'.format(bot))

BotToken = codes.token #change to os.environ['token'] 
keep_alive()
bot.run(BotToken)
