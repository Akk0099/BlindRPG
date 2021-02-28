# from .Character import Character, Job, Race
from pony.orm import *


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
        self.db.Character(id=str(id), currentStats=statsC, initialStats=statsI, level=0)
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
            self.db.Job(name="Warrior", stats=s1)
            s2 = self.db.Stats(str=1, agl=4, itl=1, mnd=1)
            self.db.Job(name="Archer", stats=s2)
            s3 = self.db.Stats(str=1, agl=1, itl=4, mnd=1)
            self.db.Job(name="Sorcerer", stats=s3)
            s4 = self.db.Stats(str=1, agl=1, itl=1, mnd=4)
            self.db.Job(name="Priest", stats=s4)
        self.db.commit()

    @db_session
    def loadRacesD(self):
        if not self.db.Race.select(lambda r: r.name == "Orc").first():
            s1 = self.db.Stats(str=4, agl=2, itl=0, mnd=1)
            self.db.Race(name="Orc", stats=s1)
            s2 = self.db.Stats(str=2, agl=2, itl=2, mnd=1)
            self.db.Race(name="Human", stats=s2)
            s3 = self.db.Stats(str=1, agl=2, itl=2, mnd=2)
            self.db.Race(name="Elf", stats=s3)
            s4 = self.db.Stats(str=0, agl=1, itl=2, mnd=4)
            self.db.Race(name="Fairy", stats=s4)
            s5 = self.db.Stats(str=3, agl=3, itl=3, mnd=3)
            self.db.Race(name="Dragon", stats=s5)
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
