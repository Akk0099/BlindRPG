import discord


def constructCharPanel(author, char):
    if char["name"]:
        embed = discord.Embed(
            title="Name: {}  Lvl: {}".format(char["name"], char["level"]),
            colour=0x38ACD2,
        )
    else:
        embed = discord.Embed(
            title="Name: {}  Lvl: {}".format("-", char["level"]), colour=0x38ACD2
        )
    embed.set_author(name="{} Character".format(author.name))

    ##Add Race / Class / Gender
    if char["race"]:
        embed.add_field(name="Race", value=char["race"]["name"])
    else:
        embed.add_field(name="Race", value="None")

    if char["job"]:
        embed.add_field(name="Job", value=char["job"]["name"])
    else:
        embed.add_field(name="Job", value="None")

    if char["gender"] != "":
        embed.add_field(name="Gender", value=char["gender"])
    else:
        embed.add_field(name="Gender", value="None")

    ##Add Stats
    embed.add_field(name="Strength", value=char["currentStats"]["str"])
    embed.add_field(name="Agility", value=char["currentStats"]["agl"])
    embed.add_field(name="Intelligence", value=char["currentStats"]["itl"])
    embed.add_field(name="Mind", value=char["currentStats"]["mnd"])
    return embed


async def raceInfo(channel):
    embed = discord.Embed(title="Race Info", colour=0xc9b216)
    embed.add_field(name="Orc", value="STR +4 | AGL +2 | INT +0 | MND +1", inline=False)
    embed.add_field(
        name="Human", value="STR +2 | AGL +2 | INT +2 | MND +1", inline=False
    )
    embed.add_field(name="Elf", value="STR +1 | AGL +2 | INT +2 | MND +2", inline=False)
    embed.add_field(
        name="Fairy", value="STR +0 | AGL +1 | INT +2 | MND +4", inline=False
    )
    embed.add_field(
        name="Dragon", value="STR +3 | AGL +3 | INT +3 | MND +3", inline=False
    )
    await channel.send(embed=embed)


async def jobInfo(channel):
    embed = discord.Embed(title="Job Info", colour=0xc9b216)
    embed.add_field(
        name="Warrior", value="STR +4 | AGL +1 | INT +1 | MND +1", inline=False
    )
    embed.add_field(
        name="Archer", value="STR +1 | AGL +4 | INT +1 | MND +1", inline=False
    )
    embed.add_field(
        name="Sorcerer", value="STR +1 | AGL +1 | INT +4 | MND +1", inline=False
    )
    embed.add_field(
        name="Priest", value="STR +1 | AGL +1 | INT +1 | MND +4", inline=False
    )
    await channel.send(embed=embed)


async def helpInfo(channel):
    embed = discord.Embed(
        title="Help Page",
        description="Card with the existent comands and small description of what each one does",
        colour=0xc9b216,
    )
    embed.add_field(
        name="!rpg",
        value="Use this prefix before all the other commands so the bot can recognize them.",
        inline=False,
    )
    embed.add_field(name="create", value="Creates your character.", inline=False)
    embed.add_field(
        name="name (name)", value="Gives your character a name.", inline=False
    )
    embed.add_field(
        name="race (name)",
        value="Gives the race with the given name to your character. See more in race-info.",
        inline=False,
    )
    embed.add_field(
        name="job (name)",
        value="Gives the job with the given name to your character.",
        inline=False,
    )
    embed.add_field(
        name="gender (Male/Female)",
        value="Choose Male or Female gender for your character.",
        inline=False,
    )
    embed.add_field(
        name="race-info",
        value="Show all the information about the available races.",
        inline=False,
    )
    embed.add_field(
        name="job-info",
        value="Show all the information about the available jobs.",
        inline=False,
    )
    embed.add_field(name="me", value="Show you character card.", inline=False)
    embed.add_field(name="daily-train", value="Train your character to boost your stats.", inline=False)
    await channel.send(embed=embed)


def failMessage(message):
    return discord.Embed(title=message, colour=0xEE3B3B)


def successMessage(message):
    return discord.Embed(title=message, colour=0x55a630)


def infoMessage(message):
    return discord.Embed(title=message, colour=0xc9b216)


async def chooseName(game, channel, author, name):
    if game.getChar(id=author.id):
        await channel.send(game.changeName(id=author.id, name=name))
        await channel.send(
            embed=constructCharPanel(author=author, char=game.getChar(id=author.id))
        )
    else:
        await notCreatedYetMessage(channel=channel)


async def chooseGender(game, channel, author, gender):
    if game.getChar(id=author.id):
        if checkGender(gender):
            await channel.send(game.changeGender(author.id, gender))
            await channel.send(
                embed=constructCharPanel(author, game.getChar(id=author.id))
            )
        else:
            await channel.send(failMessage("Pick Male or Female. The gender **{}** is not supported.".format(gender)))
    else:
        await notCreatedYetMessage(channel=channel)


async def chooseRace(game, channel, author, race):
    if game.getChar(id=author.id):
        if game.checkRace(race=race):
            await channel.send(game.changeRace(id=author.id, race=race))
            await channel.send(
                embed=constructCharPanel(author=author, char=game.getChar(author.id))
            )
        else:
            await channel.send(failMessage(
                "The race **{}** is not supported. Pick one of the follwing races: Orc/Human/Elf/Fairy/Dragon.".format(
                    race)))
    else:
        await notCreatedYetMessage(channel=channel)


async def chooseJob(game, channel, author, job):
    if game.getChar(id=author.id):
        if game.checkJob(job=job):
            await channel.send(game.changeJob(id=author.id, job=job))
            await channel.send(
                embed=constructCharPanel(author=author, char=game.getChar(id=author.id))
            )
        else:
            await channel.send(failMessage(
                "The job **{}** is not supported. Pick one of the follwing jobs: Warrior/Archer/Sorcerer/Priest.".format(
                    job)))
    else:
        await notCreatedYetMessage(channel=channel)


async def getMe(game, channel, author):
    if game.getChar(id=author.id):
        await channel.send(
            embed=constructCharPanel(author=author, char=game.getChar(id=author.id))
        )
    else:
        await notCreatedYetMessage(channel=channel)


async def notCreatedYetMessage(channel):
    await channel.send(failMessage("You don't have a character created yet. More info use !rpg help"))


async def wrongCommand(channel):
    await channel.send(
        "That command is not supported."
        + "```fix"
        + "\n"
        + "More info use !rpg help```"
    )


def checkGender(gender):
    return gender in {"Male", "Female"}


async def dailyTrain(game, channel, author):
    if game.getChar(id=author.id):
        result = game.dailyTrain(id=author.id)
        if (result[1]):
            await channel.send(embed=successMessage(result[0]))
        else:
            await channel.send(embed=failMessage(result[0]))
    else:
        await notCreatedYetMessage(channel=channel)
