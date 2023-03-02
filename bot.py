# bot.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from src import Util, BlindRPG, Database

valid_channels = {1080894903464235068}

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
db = Database.Database(False)
client = commands.Bot(command_prefix="!rpg ")
game = BlindRPG.BlindRPG(db=db)

# Discord Bot ready for use !
@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


# Verification if message sent in valid channel
@client.check
async def in_valid_channel(ctx):
    return ctx.channel.id in valid_channels


# Create character
@client.command(name="create")
async def createChar(ctx, *args):
    await Util.createChar(game=game, channel=ctx.channel, author=ctx.author, name=args)


# Choose character name
@client.command(name="name")
async def chooseName(ctx, arg):
    await Util.chooseName(game=game, channel=ctx.channel, author=ctx.author, name=arg)


# Choose character gender
@client.command(name="gender")
async def chooseGender(ctx, arg):
    await Util.chooseGender(
        game=game, channel=ctx.channel, author=ctx.author, gender=arg
    )


# Choose character race
@client.command(name="race")
async def chooseRace(ctx, arg):
    await Util.chooseRace(game=game, channel=ctx.channel, author=ctx.author, race=arg)


# Choose character job
@client.command(name="job")
async def chooseJob(ctx, arg):
    await Util.chooseJob(game=game, channel=ctx.channel, author=ctx.author, job=arg)


# Get Item info
@client.command(name="item")
async def itemInfo(ctx, arg):
    await Util.getItem(game=game, channel=ctx.channel, item=arg)


# Get Mob info
@client.command(name="mob")
async def mobInfo(ctx, arg):
    await Util.getMob(game=game, channel=ctx.channel, mob=arg)


# Get general info
@client.command(name="info")
async def helpInfo(ctx):
    await Util.helpInfo(channel=ctx.channel)


# Get Race info
@client.command(name="race-info")
async def raceInfo(ctx):
    await Util.raceInfo(channel=ctx.channel)


# Get Job info
@client.command(name="job-info")
async def jobInfo(ctx):
    await Util.jobInfo(channel=ctx.channel)


# Get character info
@client.command(name="me")
async def selfInfo(ctx):
    await Util.getMe(game=game, channel=ctx.channel, author=ctx.author)


# Use daily train action
@client.command(name="daily-train")
async def dailyTrain(ctx):
    await Util.dailyTrain(game=game, channel=ctx.channel, author=ctx.author)


async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return await Util.wrongCommand(channel=ctx.channel)
    raise error

client.run(TOKEN)
