import discord

def constructCharPanel(author, char):
    embed = discord.Embed(title="Name: {}".format(char["name"]), colour=0x38acd2)
    embed.set_author(name="{} Character".format(author.name))
    embed.add_field(name="Strength", value=char["strength"])
    embed.add_field(name="Agility", value=char["agility"])
    embed.add_field(name="Intelligence", value=char["intelligence"])
    embed.add_field(name="Mind", value=char["mind"])
    return embed