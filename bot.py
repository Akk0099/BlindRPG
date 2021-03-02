# bot.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from src import Util, BlindRPG, Database

valid_channels = {704712658330451978, 815375116254969878}

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
db = Database.Database(False)
client = commands.Bot(command_prefix="!rpg ")
game = BlindRPG.BlindRPG(db=db)


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


# global check
@client.check
async def in_valid_channel(ctx):
    return ctx.channel.id in valid_channels


@client.command(name="create")
async def createChar(ctx):
    await ctx.send(game.createChar(ctx.author.id))


@client.command(name="name")
async def chooseName(ctx, arg):
    await Util.chooseName(game=game, channel=ctx.channel, author=ctx.author, name=arg)


@client.command(name="gender")
async def chooseGender(ctx, arg):
    await Util.chooseGender(
        game=game, channel=ctx.channel, author=ctx.author, gender=arg
    )


@client.command(name="race")
async def chooseRace(ctx, arg):
    await Util.chooseRace(game=game, channel=ctx.channel, author=ctx.author, race=arg)


@client.command(name="job")
async def chooseJob(ctx, arg):
    await Util.chooseJob(game=game, channel=ctx.channel, author=ctx.author, job=arg)


@client.command(name="info")
async def helpInfo(ctx):
    await Util.helpInfo(channel=ctx.channel)


@client.command(name="race-info")
async def raceInfo(ctx):
    await Util.raceInfo(channel=ctx.channel)


@client.command(name="job-info")
async def jobInfo(ctx):
    await Util.jobInfo(channel=ctx.channel)


@client.command(name="me")
async def selfInfo(ctx):
    await Util.getMe(game=game, channel=ctx.channel, author=ctx.author)


@client.command(name="daily-train")
async def dailyTrain(ctx):
    await Util.dailyTrain(game=game, channel=ctx.channel, author=ctx.author)


async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return await Util.wrongCommand(channel=ctx.channel)
    raise error


client.run(TOKEN)
