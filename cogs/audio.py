import discord
from discord.ext import commands, tasks

class AudioCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='vikaiCS')
    async def VikaiCS(context):
        # grab the user who sent the command
        user=context.message.author
        voice_channel=user.voice.voice_channel
        channel=None
        # only play music if user is in a voice channel
        if voice_channel!= None:
            # grab user's voice channel
            channel=voice_channel.name
            await client.say('User is in channel: '+ channel)
            # create StreamPlayer
            vc= await client.join_voice_channel(voice_channel)
            player = vc.create_ffmpeg_player('audio_files/startCS.mp3', after=lambda: print('done'))
            player.start()
            while not player.is_done():
                await asyncio.sleep(1)
            # disconnect after the player has finished
            player.stop()
            await vc.disconnect()
        else:
            await client.say('User is not in a channel.')

def setup(bot):
    bot.add_cog(AudioCog(bot))