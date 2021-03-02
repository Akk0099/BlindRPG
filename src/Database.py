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
            currentStats = Required('Stats', reverse='charactersC')
            race = Optional('Race')
            job = Optional('Job')
            gender = Optional(str)
            initialStats = Required('Stats', reverse='charactersI')
            dailyAction = Optional(datetime, 6)

        class Race(self.database.Entity):
            id = PrimaryKey(int, auto=True)
            name = Optional(str)
            stats = Required('Stats')
            characters = Set(Character)
            faction = Optional(str)

        class Stats(self.database.Entity):
            id = PrimaryKey(int, auto=True)
            str = Optional(int)
            agl = Optional(int)
            itl = Optional(int)
            mnd = Optional(int)
            jobs = Set('Job')
            races = Set(Race)
            charactersC = Set(Character, reverse='currentStats')
            charactersI = Set(Character, reverse='initialStats')

        class Job(self.database.Entity):
            id = PrimaryKey(int, auto=True)
            stats = Required(Stats)
            name = Optional(str)
            characters = Set(Character)
            image = Optional(str)

        self.database.generate_mapping(create_tables=True)
