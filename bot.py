import os
import discord
import re
from discord.ext import commands, tasks
from hangintherebuster import keep_alive
client = commands.Bot(command_prefix="!")
@client.event
async def on_ready():
  print('{0.user} on standby'
  .format(client))


@client.command(description="ping chovek")
async def vrunkaizacs(ctx, enabled, usar: discord.Member, interval=45):
    if enabled.lower() == "stop":
        messageInterval.cancel()
    elif enabled.lower() == "start":
        messageInterval.change_interval(minutes=int(interval))
        messageInterval.start(usar)

@tasks.loop(minutes=45)
async def messageInterval(user: discord.Member, message=""):
    message="{} are cs4e e botka".format(user.mention)
    channel=client.get_channel(708961064313946124)
    await channel.send(message)

BotToken = os.environ['token']
keep_alive()
client.run(BotToken)
