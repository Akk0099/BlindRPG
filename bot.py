# bot.py
import os
import discord
from src import Util, BlindRPG
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
game = BlindRPG.BlindRPG()
testCh = 704712658330451978


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content.split()
    if content[0] == "!rpg":
        if content[1] == "create":
            await client.get_channel(testCh).send(game.createChar(message.author.id))
        if content[1] == "name":
            await client.get_channel(testCh).send(game.changeChar(message.author.id, "name", content[2]))
            await client.get_channel(testCh).send(
                embed=Util.constructCharPanel(author=message.author, char=game.getChar(message.author.id)))
        if content[1] == "gender":
            await Util.chooseGender(client=client, game=game, channel=testCh, author=message.author, gender=content[2])
        if content[1] == "race":
            await Util.chooseRace(client=client, game=game, channel=testCh, author=message.author, race=content[2])
        if content[1] == "job":
            await Util.chooseJob(client=client, game=game, channel=testCh, author=message.author, job=content[2])
        if content[1] == "help":
            await client.get_channel(testCh).send("Still working on this command. xD")
        if content[1] == "race-info":
            await Util.raceInfo(client=client, channel=testCh)
        if content[1] == "job-info":
            await Util.jobInfo(client=client, channel=testCh)


client.run(TOKEN)
