from datetime import datetime
from pony.orm import *
import src.Dice as dice
import src.DataLoader as loader
import src.ToDict as to_dict


class BlindRPG:
    db = None

    def __init__(self, db):
        self.db = db.database
        loader.loadData(self.db)

    ##### CHARACTERS #####

    # Creates character for user with id
    @db_session
    def createChar(self, id, name):
        statsC = self.db.Stats(str=0, agl=0, itl=0, mnd=0)
        statsI = self.db.Stats(str=0, agl=0, itl=0, mnd=0)
        inventory = self.db.Inventory(wallet=0)
        char = self.db.Character(id=str(id), currentStats=statsC, initialStats=statsI, level=0,
                                 dailyAction=datetime.now(),
                                 inventory=inventory)
        if name:
            char.name = name[0]
        self.db.commit()
        return "Character created !"

    # Retrieves character for the user with id
    @db_session
    def getChar(self, id):
        char = self.db.Character.select(lambda c: c.id == str(id)).first()
        if char:
            return to_dict.character(char)
        else:
            return None

    # Change character name of the user with id
    @db_session
    def changeName(self, id, name):
        char = self.db.Character[str(id)]
        char.name = name
        self.db.commit()
        return "Character name changed to {} !".format(name)

    # Change character gender of the user with id
    @db_session
    def changeGender(self, id, gender):
        char = self.db.Character[str(id)]
        char.gender = gender
        self.db.commit()
        return "Character gender changed to {} !".format(gender)

    # Change character job of the user with id
    @db_session
    def changeJob(self, id, job):
        char = self.db.Character[str(id)]
        job = self.db.Job.select(lambda j: j.name == job).first()
        char.job = job
        self.updateStats(char)
        self.db.commit()
        return "Character job changed !"

    # Change character race of the user with id
    @db_session
    def changeRace(self, id, race):
        char = self.db.Character[str(id)]
        race = self.db.Race.select(lambda j: j.name == race).first()
        char.race = race
        self.updateStats(char)
        self.db.commit()
        return "Character race changed !"

    # Check input job
    @db_session
    def checkJob(self, job):
        job = self.db.Job.select(lambda j: j.name == job).first()
        if job:
            return job
        else:
            return None

    # Check input race
    @db_session
    def checkRace(self, race):
        race = self.db.Race.select(lambda r: r.name == race).first()
        if race:
            return race
        else:
            return None

    # Update current character stats on job or race change
    @db_session
    def updateStats(self, char):
        str = char.initialStats.str
        agl = char.initialStats.agl
        itl = char.initialStats.itl
        mnd = char.initialStats.mnd
        if (char.race):
            str += char.race.stats.str
            agl += char.race.stats.agl
            itl += char.race.stats.itl
            mnd += char.race.stats.mnd
        if (char.job):
            str += char.job.stats.str
            agl += char.job.stats.agl
            itl += char.job.stats.itl
            mnd += char.job.stats.mnd
        char.currentStats.str = str
        char.currentStats.agl = agl
        char.currentStats.itl = itl
        char.currentStats.mnd = mnd
        self.db.commit()

    # Update current and initial stats on stat increase
    @db_session
    def updateInitialStats(self, charID, stat, value):
        char = self.db.Character[str(charID)]
        if (stat == "str"):
            char.currentStats.str = char.currentStats.str + value
            char.initialStats.str = char.initialStats.str + value
        if (stat == "agl"):
            char.currentStats.agl = char.currentStats.agl + value
            char.initialStats.agl = char.initialStats.agl + value
        if (stat == "itl"):
            char.currentStats.itl = char.currentStats.itl + value
            char.initialStats.itl = char.initialStats.itl + value
        if (stat == "mnd"):
            char.currentStats.mnd = char.currentStats.mnd + value
            char.initialStats.mnd = char.initialStats.mnd + value
        self.db.commit()

    # Check if daily action executed
    @db_session
    def checkDailyAction(self, charID):
        char = self.db.Character[str(charID)]
        time = datetime.now()

        # Uncomment in the future
        # delta = (time - char.dailyAction).seconds >= 3600

        delta = (time - char.dailyAction).seconds >= 15
        if delta:
            char.dailyAction = time
            self.db.commit()
            return delta
        else:
            return delta

    # Daily train action
    def dailyTrain(self, id):
        if self.checkDailyAction(id):
            if dice.roll100Dice():
                return "Daily train did not succeed.", False
            else:
                increase = dice.roll4Dice()
                stat = dice.rollStatDice()
                self.updateInitialStats(charID=id, stat=stat, value=increase)
                return "Daily train was successful. {} was increased by {}.".format(stat.upper(), increase), True
        else:
            return "Daily action unavailable.", False

    ##### CHARACTERS #####

    ##### ITEMS #####

    # Retreive item with item name
    @db_session
    def getItem(self, item):
        item = self.db.Item.select(lambda i: i.name == item).first()
        if item:
            return to_dict.item(item)
        else:
            return None

    ##### ITEMS #####

    ##### MOBS #####

    # Retreive mob with mob name
    @db_session
    def getMob(self, mob):
        mob = self.db.Mob.select(lambda m: m.name == mob).first()
        if mob:
            return to_dict.mob(mob)
        else:
            return None

    ##### MOBS #####
