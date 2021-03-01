import discord


def constructCharPanel(author, char):
    if char['name']:
        embed = discord.Embed(title="Name: {}  Lvl: {}".format(char['name'], char['level']), colour=0x38acd2)
    else:
        embed = discord.Embed(title="Name: {}  Lvl: {}".format("-", char['level']), colour=0x38acd2)
    embed.set_author(name="{} Character".format(author.name))

    ##Add Race / Class / Gender
    if char['race']:
        embed.add_field(name="Race", value=char['race']['name'])
    else:
        embed.add_field(name="Race", value="None")

    if char['job']:
        embed.add_field(name="Job", value=char['job']['name'])
    else:
        embed.add_field(name="Job", value="None")

    if char['gender'] != "":
        embed.add_field(name="Gender", value=char['gender'])
    else:
        embed.add_field(name="Gender", value="None")

    ##Add Stats
    embed.add_field(name="Strength", value=char['currentStats']['str'])
    embed.add_field(name="Agility", value=char['currentStats']['agl'])
    embed.add_field(name="Intelligence", value=char['currentStats']['itl'])
    embed.add_field(name="Mind", value=char['currentStats']['mnd'])
    return embed


async def raceInfo(client, channel):
    embed = discord.Embed(title="Race Info", colour=0xee3b3b)
    embed.add_field(name="Orc", value="STR +4 | AGL +2 | INT +0 | MND +1", inline=False)
    embed.add_field(name="Human", value="STR +2 | AGL +2 | INT +2 | MND +1", inline=False)
    embed.add_field(name="Elf", value="STR +1 | AGL +2 | INT +2 | MND +2", inline=False)
    embed.add_field(name="Fairy", value="STR +0 | AGL +1 | INT +2 | MND +4", inline=False)
    embed.add_field(name="Dragon", value="STR +3 | AGL +3 | INT +3 | MND +3", inline=False)
    await client.get_channel(channel).send(embed=embed)


async def jobInfo(client, channel):
    embed = discord.Embed(title="Job Info", colour=0xee3b3b)
    embed.add_field(name="Warrior", value="STR +4 | AGL +1 | INT +1 | MND +1", inline=False)
    embed.add_field(name="Archer", value="STR +1 | AGL +4 | INT +1 | MND +1", inline=False)
    embed.add_field(name="Sorcerer", value="STR +1 | AGL +1 | INT +4 | MND +1", inline=False)
    embed.add_field(name="Priest", value="STR +1 | AGL +1 | INT +1 | MND +4", inline=False)
    await client.get_channel(channel).send(embed=embed)


async def helpInfo(client, channel):
    embed = discord.Embed(title="Help Page",
                          description="Card with the existent comands and small description of what each one does",
                          colour=0xee3b3b)
    embed.add_field(name="!rpg",
                    value="Use this prefix before all the other commands so the bot can recognize them.", inline=False)
    embed.add_field(name="create", value="Creates your character.", inline=False)
    embed.add_field(name="name (name)", value="Gives your character a name.", inline=False)
    embed.add_field(name="race (name)",
                    value="Gives the race with the given name to your character. See more in race-info.", inline=False)
    embed.add_field(name="job (name)", value="Gives the job with the given name to your character.", inline=False)
    embed.add_field(name="gender (Male/Female)", value="Choose Male or Female gender for your character.", inline=False)
    embed.add_field(name="race-info", value="Show all the information about the available races.", inline=False)
    embed.add_field(name="job-info", value="Show all the information about the available jobs.", inline=False)
    embed.add_field(name="me", value="Show you character card.", inline=False)
    await client.get_channel(channel).send(embed=embed)


async def message(message):
    return discord.Embed(title=message, colour=0x55a630)


async def chooseName(client, game, channel, author, name):
    if game.getChar(id=author.id):
        await client.get_channel(channel).send(game.changeName(id=author.id, name=name))
        await client.get_channel(channel).send(
            embed=constructCharPanel(author=author, char=game.getChar(id=author.id)))
    else:
        await notCreatedYetMessage(client=client, channel=channel)


async def chooseGender(client, game, channel, author, gender):
    if game.getChar(id=author.id):
        if checkGender(gender):
            await client.get_channel(channel).send(game.changeGender(author.id, gender))
            await client.get_channel(channel).send(
                embed=constructCharPanel(author, game.getChar(id=author.id)))
        else:
            await client.get_channel(channel).send(
                "Pick Male or Female. The gender **{}** is not supported.".format(gender))
    else:
        await notCreatedYetMessage(client=client, channel=channel)


async def chooseJob(client, game, channel, author, job):
    if game.getChar(id=author.id):
        if game.checkJob(job=job):
            await client.get_channel(channel).send(game.changeJob(id=author.id, job=job))
            await client.get_channel(channel).send(
                embed=constructCharPanel(author=author, char=game.getChar(id=author.id)))
        else:
            await client.get_channel(channel).send(
                "The job **{}** is not supported. Pick one of the follwing jobs: Warrior/Archer/Sorcerer/Priest.".format(
                    job) + "\n" + "```fix" + "\n" + "More info use !rpg job-info```")
    else:
        await notCreatedYetMessage(client=client, channel=channel)


async def chooseRace(client, game, channel, author, race):
    if game.getChar(id=author.id):
        if game.checkRace(race=race):
            await client.get_channel(channel).send(game.changeRace(id=author.id, race=race))
            await client.get_channel(channel).send(
                embed=constructCharPanel(author=author, char=game.getChar(author.id)))
        else:
            await client.get_channel(channel).send(
                "The race **{}** is not supported. Pick one of the follwing races: Orc/Human/Elf/Fairy/Dragon.".format(
                    race) + "\n" + "```fix" + "\n" + "More info use !rpg race-info```")
    else:
        await notCreatedYetMessage(client=client, channel=channel)


async def getMe(client, game, channel, author):
    if game.getChar(id=author.id):
        await client.get_channel(channel).send(
            embed=constructCharPanel(author=author, char=game.getChar(id=author.id)))
    else:
        await notCreatedYetMessage(client=client, channel=channel)


async def notCreatedYetMessage(client, channel):
    await client.get_channel(channel).send(
        "You don't have a character created yet." + "```fix" + "\n" + "More info use !rpg help```")


async def wrongCommand(client, channel):
    await client.get_channel(channel).send(
        "That command is not supported." + "```fix" + "\n" + "More info use !rpg help```")


def checkGender(gender):
    return gender in {"Male", "Female"}


async def dailyTrain(client, game, channel, author):
    if game.getChar(id=author.id):
        await client.get_channel(channel).send(
            embed=await message(message=game.dailyTrain(id=author.id)))
    else:
        await notCreatedYetMessage(client=client, channel=channel)
