import random


def roll100Dice():
    roll = random.randint(1, 100)
    if roll <= 50:
        return False
    elif roll >= 51:
        return True


def roll4Dice():
    return random.randint(1, 4)


def rollStatDice():
    stats = ["str", "agl", "itl", "mnd"]
    return random.choice(stats)
