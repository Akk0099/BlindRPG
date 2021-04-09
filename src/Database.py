from datetime import datetime

from pony.orm import *
from pony.orm import Database as PonyDatabase


class Database:

    def __init__(self, test):
        self.database = PonyDatabase()
        if (test):
            self.database.bind(provider='sqlite', filename='../tests/database.sqlite', create_db=True)
        else:
            self.database.bind(provider='sqlite', filename='../data/database.sqlite', create_db=True)

        class Character(self.database.Entity):
            id = PrimaryKey(str)
            name = Optional(str)
            level = Optional(int)
            gender = Optional(str)
            dailyAction = Optional(datetime, 6)
            job = Optional('Job')
            race = Optional('Race')
            initialStats = Required('Stats', reverse='charactersI')
            currentStats = Required('Stats', reverse='charactersC')
            inventory = Required('Inventory')

        class Job(self.database.Entity):
            id = PrimaryKey(int, auto=True)
            name = Optional(str)
            image = Optional(str)
            characters = Set(Character)
            stats = Required('Stats')

        class Race(self.database.Entity):
            id = PrimaryKey(int, auto=True)
            name = Optional(str)
            faction = Optional(str)
            characters = Set(Character)
            stats = Required('Stats')

        class Stats(self.database.Entity):
            id = PrimaryKey(int, auto=True)
            str = Optional(int)
            agl = Optional(int)
            itl = Optional(int)
            mnd = Optional(int)
            charactersI = Optional(Character, reverse='initialStats')
            charactersC = Optional(Character, reverse='currentStats')
            race = Optional(Race)
            job = Optional(Job)
            item = Optional('Item')
            mob = Optional('Mob')

        class Item(self.database.Entity):
            id = PrimaryKey(int, auto=True)
            name = Optional(str)
            type = Optional(str)
            image = Optional(str)
            value = Optional(int)
            stats = Required(Stats)
            drops = Set('Drop')
            inventories = Set('Inventory')

        class Mob(self.database.Entity):
            id = PrimaryKey(int, auto=True)
            name = Required(str)
            type = Required(str)
            image = Optional(str)
            stats = Required(Stats)
            drops = Set('Drop')

        class Inventory(self.database.Entity):
            id = PrimaryKey(int, auto=True)
            wallet = Required(int)
            character = Optional(Character)
            items = Set(Item)

        class Drop(self.database.Entity):
            id = PrimaryKey(int, auto=True)
            rate = Required(float)
            mob = Required(Mob)
            item = Required(Item)

        self.database.generate_mapping(create_tables=True)
