import discord
from discord.ext import commands
import youtube_dl
import os
import json
import ffmpeg
from subprocess import check_output
from discord.ext.commands.bot import Bot


client = discord.Client()

client = commands.Bot(command_prefix='$')

@client.event
async def onReady():
    print('We have logged in as {0.user}'.format(client))

async def set_to_unmuted(member: discord.Member):
    await member.edit(mute=False)

@commands.command()
async def pu(ctx, url: str):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice != None:
        await voice.disconnect()
    channel = ctx.author.voice.channel
    await channel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if os.path.isfile('song.mp3'):
        os.remove('song.mp3')
    os.system("yt-dlp --extract-audio --audio-format mp3 " + url)
    startPlay()
    voice.play(discord.FFmpegPCMAudio(executable='ffmpeg/bin/ffmpeg.exe', source='song.mp3'))


@commands.command()
async def p(ctx, *args):
    query = " ".join(args[:])
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice != None:
        await voice.disconnect()
    channel = ctx.author.voice.channel
    await channel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if os.path.isfile('song.mp3'):
        os.remove('song.mp3')
    os.system('yt-dlp --extract-audio --audio-format mp3 "ytsearch:' + query + '"')
    startPlay()
    voice.play(discord.FFmpegPCMAudio(executable='ffmpeg/bin/ffmpeg.exe', source='song.mp3'))

   
def startPlay():
    for file in os.listdir(os.getcwd()):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
            break
        elif file.endswith(".m4a"):
             print("bruh")
             os.rename(file, "song.mp3")
             break  

@commands.command()
async def d(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    await voice.disconnect()

@commands.command()
async def s(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice != None:
        await voice.disconnect()
    channel = ctx.author.voice.channel
    await channel.connect()

@commands.command()
async def h(ctx):
    await ctx.channel.send('Some crappy music bot v1.0 Made by David101')
    await ctx.channel.send('Commands:')
    await ctx.channel.send('$p search query - Play a song with a search query')
    await ctx.channel.send('$pu url - Play a song (YOU MUST PROVIDE A URL)')
    await ctx.channel.send('$s - Stop/Skip a song')
    await ctx.channel.send('$d - Disonnect bot from voice channel')


client.add_command(pu)
client.add_command(p)
client.add_command(d)
client.add_command(h)
client.add_command(s)

client.run('') #add your discord bot token here!