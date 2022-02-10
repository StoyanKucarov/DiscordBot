import codes #delete before pulling
import os
import discord
import re
import datetime
import asyncio
import random
from discord.ext import commands, tasks
from discord import FFmpegPCMAudio
from hangintherebuster import keep_alive
client = commands.Bot(command_prefix="!")
@client.event
async def on_ready():
  print('{0.user} on standby'
  .format(client))


@client.command(description="ping chovek", name='CS')
async def vrunkaizacs(ctx, user: discord.Member, enabled="start", interval=1):
    if enabled.lower() == "stop":#stop the cycle with command
        try:
            await WithoutCS(user, ctx)
        except Exception as e:
            print(str(e))
    elif enabled.lower() == "start":#start cycle for message
        try:
            messageInterval.change_interval(minutes=int(interval))
            messageInterval.start(user, ctx)
        except Exception as e:
            print(str(e))


@client.command(name='vikaiCS')
async def VikaiCS(ctx, user: discord.Member, vers="last"):
    # grab the user's voice channel
    try:
        voice_channel=user.voice.channel
        channel=None
    except Exception as e:
        print(str(e))
        await ctx.send('No channel found')
    # only play music if user is in a voice channel
    if voice_channel!= None:
        # create StreamPlayer
        try:
            vc= await voice_channel.connect()
            source=discord.FFmpegPCMAudio('audio_files/startCSLegacy.mp3')
            if vers=="last":
                source=discord.FFmpegPCMAudio('audio_files/startCS.mp3')
            player=vc.play(source)
            await asyncio.sleep(3)
            # disconnect after the player has finished
            await vc.disconnect()
        except Exception as e:
            print(str(e))
            await ctx.send('Error in connecting')
    else:
        await ctx.send('User is not in a channel.')

@client.command(name='b0tkaCS')
async def botkaCS(ctx, user: discord.Member, vers="last"):
    # grab the user's voice channel
    try:
        voice_channel=user.voice.channel
        channel=None
    except Exception as e:
        print(str(e))
        await ctx.send('No channel found')
    # only play music if user is in a voice channel
    if voice_channel!= None:
        try:
            # create StreamPlayer
            vc= await voice_channel.connect()
            #add a message on top
            mes=makeBotName(user.name)
            message=mes.format(user.mention)
            await ctx.send(message)
            source=discord.FFmpegPCMAudio('audio_files/botkaCSLegacy.mp3')
            if vers=="last":
                source=discord.FFmpegPCMAudio('audio_files/botkaCS.mp3')
            player=vc.play(source)
            await asyncio.sleep(3)
            # disconnect after the player has finished
            await vc.disconnect()
        except Exception as e:
            print(str(e))
            await ctx.send('Error in connecting')
    else:
        await ctx.send('User is not in a channel.')


@client.command(name='k0mputkaCS')
async def botkaCS(ctx, vers="last"):
    # grab the user's voice channel
    try:
        voice_channel=ctx.author.voice.channel
        channel=None
    except Exception as e:
        print(str(e))
        await ctx.send('No channel found')
    # only play music if user is in a voice channel
    if voice_channel!= None:
        try:
            # create StreamPlayer
            vc= await voice_channel.connect()
            #add a message on top
            await ctx.send("@everyone"+" vreme za k0mputka")
            source=discord.FFmpegPCMAudio('audio_files/kompetkaCSLegacy.mp3')
            if vers=="last":
                source=discord.FFmpegPCMAudio('audio_files/kompetkaCS.mp3')
            player=vc.play(source)
            await asyncio.sleep(3)
            # disconnect after the player has finished
            await vc.disconnect()
        except Exception as e:
            print(str(e))
            await ctx.send('Error in connecting')
    else:
        await ctx.send('User is not in a channel.')

@tasks.loop(minutes=0.5)
async def messageInterval(user: discord.Member, ctx):
    nowTime=datetime.datetime.now()#get a datetime to check if we are in school to repeat
    nowTimeInt=nowTime.hour*60+nowTime.minute#the hours are turned to minutes and added to the rest minutes
    if nowTimeInt>=(0*8*60+30) and nowTimeInt<=(14*60*100):#work if between 8:30 and 14:00
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

def makeBotName(name):#make bot name ex:Stelyo -> b0tlyo
    if len(name)<=3:
        return "{} b0t"+name
    elif len(name)==4:
        return "{} b0t"+name[2:]
    elif len(name)==5:
        return "{} b0t"+name[2:]
    else:
        return "{} b0t"+name[3:]

@client.event
async def on_message(message):
  chance=random.random()
  mes="{} tiho e slow".format(message.author.mention)
  if chance<=0.05 and message.author.id!=940642505953796106:
    await message.channel.send(mes)
  await client.process_commands(message)

def IsVasilenRandom():
    isTwo=random.randint(1, 100)
    if isTwo<=2:
        return True
    return False

BotToken = codes.token #change to os.environ['token'] 
keep_alive()
client.run(BotToken)
