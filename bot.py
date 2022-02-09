import os
import discord
import re
import datetime
from discord.ext import commands, tasks
from hangintherebuster import keep_alive
client = commands.Bot(command_prefix="!")
@client.event
async def on_ready():
  print('{0.user} on standby'
  .format(client))


@client.command(description="ping chovek", name='cs')
async def vrunkaizacs(ctx, user: discord.Member, enabled="start", interval=1):
    if enabled.lower() == "stop":#check for stop or if the time is 
        try:
            await WithoutCS(user, ctx)
        except Exception as e:
            print(str(e))
    elif enabled.lower() == "start":
        try:
            messageInterval.change_interval(minutes=int(interval))
            messageInterval.start(user, ctx)
        except Exception as e:
            print(str(e))

@tasks.loop(minutes=0.5)
async def messageInterval(user: discord.Member, ctx):
    nowTime=datetime.datetime.now()#get a datetime to check if we are in school to repeat
    nowTimeInt=nowTime.hour*60+nowTime.minute#the hours are turned to minutes and added to the rest minutes
    if nowTimeInt>=(8*60+30) and nowTimeInt<=(14*60):#work if between 8:30 and 14:00
        message="{} are cs4e e botka".format(user.mention)
        await ctx.send(message)
    else:
        try:
            await WithoutCS(user, ctx)
        except Exception as e:
            print(str(e))

async def WithoutCS(user: discord.Member, ctx):#function to end the cycle and sent a message
    messageInterval.cancel()
    message="{} haide bez cs".format(user.mention)
    await ctx.send(message)

BotToken = os.environ['token']
keep_alive()
client.run(BotToken)
