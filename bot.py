# bot.py
import os
import discord
from src import Util, BlindRPG, Database
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

db = Database.Database()
client = discord.Client()
game = BlindRPG.BlindRPG(db=db)
testChJP = 704712658330451978
testChUNI = 815375116254969878


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id not in {testChJP, testChUNI}:
        return

    channel = message.channel.id

    content = message.content.split()
    if content[0] == "!rpg":
        if content[1] == "create":
            await client.get_channel(channel).send(game.createChar(message.author.id))
        elif content[1] == "name":
            await Util.chooseName(client=client, game=game, channel=channel, author=message.author, name=content[2])
        elif content[1] == "gender":
            await Util.chooseGender(client=client, game=game, channel=channel, author=message.author, gender=content[2])
        elif content[1] == "race":
            await Util.chooseRace(client=client, game=game, channel=channel, author=message.author, race=content[2])
        elif content[1] == "job":
            await Util.chooseJob(client=client, game=game, channel=channel, author=message.author, job=content[2])
        elif content[1] == "help":
            await Util.helpInfo(client=client, channel=channel)
        elif content[1] == "race-info":
            await Util.raceInfo(client=client, channel=channel)
        elif content[1] == "job-info":
            await Util.jobInfo(client=client, channel=channel)
        elif content[1] == "me":
            await Util.getMe(client=client, game=game, channel=channel, author=message.author)
        else:
            await Util.wrongCommand(client=client, channel=channel)


client.run(TOKEN)
