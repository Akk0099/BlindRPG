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


async def chooseGender(client, game, channel, author, gender):
    if checkGender(gender):
        await client.get_channel(channel).send(game.changeChar(author.id, "gender", gender))
        await client.get_channel(channel).send(
            embed=constructCharPanel(author, game.getChar(author.id)))
    else:
        await client.get_channel(channel).send(
            "Pick Male or Female. The gender **{}** is not supported.".format(gender))


def checkGender(gender):
    return gender == ("Male" or "Female")
