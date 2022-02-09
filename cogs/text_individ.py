import discord
from discord.ext import commands, tasks

class TextIndividCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Intial command"""
    @commands.command(description="ping chovek", name='cs')
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

    """Message cycle"""
    @tasks.loop(minutes=0.5)
    async def messageInterval(user: discord.Member, ctx):
        nowTime=datetime.datetime.now()#get a datetime to check if we are in school to repeat
        nowTimeInt=nowTime.hour*60+nowTime.minute#the hours are turned to minutes and added to the rest minutes
        if True: #nowTimeInt>=(8*60+30) and nowTimeInt<=(14*60):#work if between 8:30 and 14:00
            message="{} are cs4e e botka".format(user.mention)
            await ctx.send(message)
        else:
            try:
                await WithoutCS(user, ctx)
            except Exception as e:
                print(str(e))
    
    """Stop cycle"""
    async def WithoutCS(user: discord.Member, ctx):#function to end the cycle and sent a message
        messageInterval.cancel()
        message="{} haide bez cs".format(user.mention)
        await ctx.send(message)

# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(TextIndividCog(bot))