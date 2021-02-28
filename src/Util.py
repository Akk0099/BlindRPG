import discord


def constructCharPanel(author, char):
    embed = discord.Embed(title="Name: {}  Lvl: {}".format(char["name"], char["level"]), colour=0x38acd2)
    embed.set_author(name="{} Character".format(author.name))

    ##Add Race / Class / Gender
    if char["race"]:
        embed.add_field(name="Race", value=char["race"].name)
    else:
        embed.add_field(name="Race", value="None")

    if char["job"]:
        embed.add_field(name="Job", value=char["job"].name)
    else:
        embed.add_field(name="Job", value="None")

    if char["gender"] != "":
        embed.add_field(name="Gender", value=char["gender"])
    else:
        embed.add_field(name="Gender", value="None")

    ##Add Stats
    embed.add_field(name="Strength", value=char["stats"].str)
    embed.add_field(name="Agility", value=char["stats"].agl)
    embed.add_field(name="Intelligence", value=char["stats"].int)
    embed.add_field(name="Mind", value=char["stats"].mnd)
    return embed


async def raceInfo(client, channel):
    embed = discord.Embed(title="Race Info", colour=0xee3b3b)
    embed.add_field(name="Orc", value="STR +4 | AGL +2 | INT +0 | MND +1", inline=False)
    embed.add_field(name="Human", value="STR +2 | AGL +2 | INT +2 | MND +1", inline=False)
    embed.add_field(name="Elf", value="STR +1 | AGL +2 | INT +2 | MND +2", inline=False)
    embed.add_field(name="Fairy", value="STR +0 | AGL +1 | INT +2 | MND +4", inline=False)
    await client.get_channel(channel).send(embed=embed)


async def jobInfo(client, channel):
    embed = discord.Embed(title="Job Info", colour=0xee3b3b)
    embed.add_field(name="Paladin", value="STR +4 | AGL +1 | INT +1 | MND +1", inline=False)
    embed.add_field(name="Archer", value="STR +1 | AGL +4 | INT +1 | MND +1", inline=False)
    embed.add_field(name="Wizard", value="STR +1 | AGL +1 | INT +4 | MND +1", inline=False)
    embed.add_field(name="Conjurer", value="STR +1 | AGL +1 | INT +1 | MND +4", inline=False)
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


async def chooseGender(client, game, channel, author, gender):
    if checkGender(gender):
        await client.get_channel(channel).send(game.changeChar(author.id, "gender", gender))
        await client.get_channel(channel).send(
            embed=constructCharPanel(author, game.getChar(author.id)))
    else:
        await client.get_channel(channel).send(
            "Pick Male or Female. The gender **{}** is not supported.".format(gender))


async def chooseJob(client, game, channel, author, job):
    if checkJob(job):
        await client.get_channel(channel).send(game.changeJob(author.id, job))
        await client.get_channel(channel).send(
            embed=constructCharPanel(author=author, char=game.getChar(author.id)))
    else:
        await client.get_channel(channel).send(
            "The job **{}** is not supported. Pick one of the follwing jobs: Paladin/Archer/Wizard/Conjurer.".format(
                job) + "\n" + "```fix" + "\n" + "More info use !rpg job-info```")


async def chooseRace(client, game, channel, author, race):
    if checkRace(race):
        await client.get_channel(channel).send(game.changeRace(author.id, race))
        await client.get_channel(channel).send(
            embed=constructCharPanel(author=author, char=game.getChar(author.id)))
    else:
        await client.get_channel(channel).send(
            "The race **{}** is not supported. Pick one of the follwing races: Orc/Human/Elf/Fairy.".format(
                race) + "\n" + "```fix" + "\n" + "More info use !rpg race-info```")


def checkGender(gender):
    return gender in {"Male", "Female"}


def checkJob(job):
    return job in {'Paladin', 'Archer', 'Wizard', 'Conjurer'}


def checkRace(race):
    return race in {'Orc' or 'Human' or 'Elf' or 'Fairy'}
