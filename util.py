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
