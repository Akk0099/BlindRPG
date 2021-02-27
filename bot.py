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
    # await client.get_channel(testCh).send("I am ALIVE !!!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content.split()
    if content[0] == "!rpg":
        if content[1] == "create":
            await client.get_channel(testCh).send(game.createChar(message.author.id))
            # await client.get_channel(testCh).send(game.getChar(message.author.id))
        if content[1] == "name":
            await client.get_channel(testCh).send(game.changeChar(message.author.id, "name", content[2]))
            await client.get_channel(testCh).send(
                embed=Util.constructCharPanel(message.author, game.getChar(message.author.id)))
        if content[1] == "gender":
            await Util.chooseGender(client, game, testCh, message.author, content[2])
        if content[1] == "race":
            await client.get_channel(testCh).send(game.changeChar(message.author.id, "race", content[2]))
            await client.get_channel(testCh).send(
                embed=Util.constructCharPanel(message.author, game.getChar(message.author.id)))
        if content[1] == "job":
            await client.get_channel(testCh).send(game.changeChar(message.author.id, "job", content[2]))
            await client.get_channel(testCh).send(
                embed=Util.constructCharPanel(message.author, game.getChar(message.author.id)))
    # print(content)
    # await client.get_channel(testCh).send("I can see that.")
    # print(message.author.id)
    # print(message.author.name)


client.run(TOKEN)
