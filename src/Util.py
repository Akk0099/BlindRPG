import discord


def constructCharPanel(author, char):
    embed = discord.Embed(title="Name: {}  Lvl: {}".format(char["name"], char["level"]), colour=0x38acd2)
    embed.set_author(name="{} Character".format(author.name))

    ##Add Race / Class / Gender
    if char["race"] != "":
        embed.add_field(name="Race", value=char["race"])
    else:
        embed.add_field(name="Race", value="None")

    if char["job"] != "":
        embed.add_field(name="Job", value=char["job"])
    else:
        embed.add_field(name="Job", value="None")

    if char["gender"] != "":
        embed.add_field(name="Gender", value=char["gender"])
    else:
        embed.add_field(name="Gender", value="None")

    ##Add Stats
    embed.add_field(name="Strength", value=char["strength"])
    embed.add_field(name="Agility", value=char["agility"])
    embed.add_field(name="Intelligence", value=char["intelligence"])
    embed.add_field(name="Mind", value=char["mind"])
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
        await client.get_channel(channel).send(game.changeChar(author.id, "job", job))
        await client.get_channel(channel).send(
            embed=constructCharPanel(author=author, char=game.getChar(author.id)))
    else:
        await client.get_channel(channel).send(
            "The job **{}** is not supported. Pick one of the follwing jobs: Paladin/Archer/Wizard/Conjurer.".format(
                job) + "\n" + "```fix" + "\n" + "More info use !rpg job-info```")


async def chooseRace(client, game, channel, author, race):
    if checkRace(race):
        await client.get_channel(channel).send(game.changeChar(author.id, "race", race))
        await client.get_channel(channel).send(
            embed=constructCharPanel(author=author, char=game.getChar(author.id)))
    else:
        await client.get_channel(channel).send(
            "The race **{}** is not supported. Pick one of the follwing jobs: Orc/Human/Elf/Fairy.".format(
                race) + "\n" + "```fix" + "\n" + "More info use !rpg race-info```")


def checkGender(gender):
    return gender == ("Male" or "Female")


def checkJob(job):
    return job == ('Paladin' or 'Archer' or 'Wizard' or 'Conjurer')


def checkRace(race):
    return race == ('Orc' or 'Human' or 'Elf' or 'Fairy')
