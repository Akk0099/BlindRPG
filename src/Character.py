class Character:
    name = ""
    level = 0
    race = None
    job = None
    hp = 0
    gender = ""
    stats = None
    initialStats = None

    def __init__(self):
        self.name = ""
        self.level = 0
        self.race = None
        self.job = None
        self.maxHp = 0
        self.gender = ""
        self.initialStats = Stats()
        self.stats = Stats()

    def changeField(self, field, value):
        setattr(self, field, value)

    def setRace(self, race):
        self.race = race
        self.updateStats()

    def setJob(self, job):
        self.job = job
        self.updateStats()

    def updateStats(self):
        if self.job and self.race:
            self.stats = self.initialStats + self.job.stats + self.race.stats
        elif self.job:
            self.stats = self.initialStats + self.job.stats
        elif self.race:
            self.stats = self.initialStats + self.race.stats


class Race:
    name = ""
    stats = None

    def __init__(self, name, str, agl, int, mnd):
        self.name = name
        self.stats = Stats(str=str, agl=agl, int=int, mnd=mnd)


class Job:
    name = ""
    stats = None

    def __init__(self, name, str, agl, int, mnd):
        self.name = name
        self.stats = Stats(str=str, agl=agl, int=int, mnd=mnd)


class Stats:
    str = 0
    agl = 0
    int = 0
    mnd = 0

    def __init__(self, str=0, agl=0, int=0, mnd=0):
        self.str = str
        self.agl = agl
        self.int = int
        self.mnd = mnd

    def __add__(self, other):
        str = self.str + other.str
        agl = self.agl + other.agl
        int = self.int + other.int
        mnd = self.mnd + other.mnd
        return Stats(str=str, agl=agl, int=int, mnd=mnd)
