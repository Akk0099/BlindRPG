from datetime import datetime
from pony.orm import *
import random


class BlindRPG:
    chars = {}
    jobs = {}
    races = {}
    db = None

    def __init__(self, db):
        self.db = db.database
        self.loadJobsD()
        self.loadRacesD()

    @db_session
    def createChar(self, id):
        statsC = self.db.Stats(str=0, agl=0, itl=0, mnd=0)
        statsI = self.db.Stats(str=0, agl=0, itl=0, mnd=0)
        self.db.Character(id=str(id), currentStats=statsC, initialStats=statsI, level=0, dailyAction=datetime.now())
        self.db.commit()
        return "Character created !"

    @db_session
    def getChar(self, id):
        char = self.db.Character.select(lambda c: c.id == str(id)).first()
        if char:
            return self.to_dict_character(char)
        else:
            return None

    @db_session
    def changeName(self, id, name):
        char = self.db.Character[str(id)]
        char.name = name
        self.db.commit()
        return "Character name changed to {} !".format(name)

    @db_session
    def changeGender(self, id, gender):
        char = self.db.Character[str(id)]
        char.gender = gender
        self.db.commit()
        return "Character gender changed to {} !".format(gender)

    @db_session
    def changeJob(self, id, job):
        char = self.db.Character[str(id)]
        job = self.db.Job.select(lambda j: j.name == job).first()
        char.job = job
        if char.race:
            self.updateCharStats(charStats=char.currentStats, initStats=char.initialStats, raceStats=char.race.stats,
                                 jobStats=job.stats)
        else:
            self.updateCharStats(charStats=char.currentStats, initStats=char.initialStats, jobStats=job.stats,
                                 raceStats=None)
        self.db.commit()
        return "Character job changed !"

    @db_session
    def checkJob(self, job):
        job = self.db.Job.select(lambda j: j.name == job).first()
        if job:
            return job
        else:
            return None

    @db_session
    def changeRace(self, id, race):
        char = self.db.Character[str(id)]
        race = self.db.Race.select(lambda j: j.name == race).first()
        char.race = race
        if char.job:
            self.updateCharStats(charStats=char.currentStats, initStats=char.initialStats, raceStats=race.stats,
                                 jobStats=char.job.stats)
        else:
            self.updateCharStats(charStats=char.currentStats, initStats=char.initialStats, raceStats=race.stats,
                                 jobStats=None)
        self.db.commit()
        return "Character race changed !"

    @db_session
    def checkRace(self, race):
        race = self.db.Race.select(lambda r: r.name == race).first()
        if race:
            return race
        else:
            return None

    @db_session
    def loadJobsD(self):
        if not self.db.Job.select(lambda j: j.name == "Warrior").first():
            s1 = self.db.Stats(str=4, agl=1, itl=1, mnd=1)
            self.db.Job(name="Warrior", stats=s1, image="https://i.imgur.com/dHLGGNs.png")
            s2 = self.db.Stats(str=1, agl=4, itl=1, mnd=1)
            self.db.Job(name="Archer", stats=s2, image="https://i.imgur.com/XrBkP1O.png")
            s3 = self.db.Stats(str=1, agl=1, itl=4, mnd=1)
            self.db.Job(name="Sorcerer", stats=s3, image="https://i.imgur.com/vpZLrxn.png")
            s4 = self.db.Stats(str=1, agl=1, itl=1, mnd=4)
            self.db.Job(name="Priest", stats=s4, image="https://i.imgur.com/1XGAYei.png")
        self.db.commit()

    @db_session
    def loadRacesD(self):
        if not self.db.Race.select(lambda r: r.name == "Orc").first():
            s1 = self.db.Stats(str=4, agl=2, itl=0, mnd=1)
            self.db.Race(name="Orc", stats=s1, faction="https://i.imgur.com/kcXnYg3.png")
            s2 = self.db.Stats(str=2, agl=2, itl=2, mnd=1)
            self.db.Race(name="Human", stats=s2, faction="https://i.imgur.com/kcXnYg3.png")
            s3 = self.db.Stats(str=1, agl=2, itl=2, mnd=2)
            self.db.Race(name="Elf", stats=s3, faction="https://i.imgur.com/g1a0Jxg.png")
            s4 = self.db.Stats(str=0, agl=1, itl=2, mnd=4)
            self.db.Race(name="Fairy", stats=s4, faction="https://i.imgur.com/KBUV5zt.png")
            s5 = self.db.Stats(str=3, agl=3, itl=3, mnd=3)
            self.db.Race(name="Dragon", stats=s5, faction="https://i.imgur.com/oHMPKUd.png")
        self.db.commit()

    @db_session
    def to_dict_character(self, obj):
        if obj is None:
            return None
        char = obj.to_dict()
        char['currentStats'] = obj.currentStats.to_dict()
        char['initialStats'] = obj.initialStats.to_dict()
        if obj.race:
            char['race'] = obj.race.to_dict()
        if obj.job:
            char['job'] = obj.job.to_dict()

        return char

    @db_session
    def updateCharStats(self, charStats, initStats, jobStats, raceStats):
        if jobStats and raceStats:
            charStats.str = initStats.str + jobStats.str + raceStats.str
            charStats.agl = initStats.agl + jobStats.agl + raceStats.agl
            charStats.itl = initStats.itl + jobStats.itl + raceStats.itl
            charStats.mnd = initStats.mnd + jobStats.mnd + raceStats.mnd
        elif jobStats:
            charStats.str = initStats.str + jobStats.str
            charStats.agl = initStats.agl + jobStats.agl
            charStats.itl = initStats.itl + jobStats.itl
            charStats.mnd = initStats.mnd + jobStats.mnd
        elif raceStats:
            charStats.str = initStats.str + raceStats.str
            charStats.agl = initStats.agl + raceStats.agl
            charStats.itl = initStats.itl + raceStats.itl
            charStats.mnd = initStats.mnd + raceStats.mnd
        else:
            charStats = initStats
        self.db.commit()

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

    def dailyTrain(self, id):
        if self.checkDailyAction(id):
            if self.roll100Dice():
                return "Daily train did not succeed.", False
            else:
                increase = self.roll4Dice()
                stat = self.rollStatDice()
                self.updateInitialStats(charID=id, stat=stat, value=increase)
                return "Daily train was successful.{} was increased by {}.".format(stat, increase), True
        else:
            return "Daily action unavailable.", False

    def roll100Dice(self):
        roll = random.randint(1, 100)
        if roll <= 50:
            return False
        elif roll >= 51:
            return True

    def roll4Dice(self):
        return random.randint(1, 4)

    def rollStatDice(self):
        stats = ["str", "agl", "itl", "mnd"]
        return random.choice(stats)
