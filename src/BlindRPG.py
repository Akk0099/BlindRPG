from .Character import Character, Job, Race


class BlindRPG:
    chars = {}
    jobs = {}
    races = {}

    def __init__(self):
        self.loadJobs()
        self.loadRaces()

    def createChar(self, id):
        char = Character()
        newChar = {id: char}
        self.chars.update(newChar)
        return "Character created !"

    def getChar(self, id):
        return self.chars[id].__dict__

    def printchars(self):
        for char in self.chars:
            print(char)
            print(self.chars[char].__dict__)

    def changeChar(self, id, field, value):
        if self.chars[id]:
            self.chars[id].changeField(field, value)
        return "Character {} changed !".format(field)

    def changeJob(self, id, job):
        if self.chars[id]:
            self.chars[id].setJob(job=self.jobs[job])
        return "Character job changed !"

    def changeRace(self, id, race):
        if self.chars[id]:
            self.chars[id].setRace(race=self.races[race])
        return "Character race changed !"

    # Later change to load from file
    def loadJobs(self):
        paladin = {"Paladin": Job(name="Paladin", str=4, agl=1, int=1, mnd=1)}
        archer = {"Archer": Job(name="Archer", str=1, agl=4, int=1, mnd=1)}
        wizard = {"Wizard": Job(name="Wizard", str=1, agl=1, int=4, mnd=1)}
        conjurer = {"Conjurer": Job(name="Conjurer", str=1, agl=1, int=1, mnd=4)}
        self.jobs.update(paladin)
        self.jobs.update(archer)
        self.jobs.update(wizard)
        self.jobs.update(conjurer)

    # Later change to load from file
    def loadRaces(self):
        orc = {"Orc": Race(name="Orc", str=4, agl=2, int=0, mnd=1)}
        human = {"Human": Race(name="Human", str=2, agl=2, int=2, mnd=1)}
        elf = {"Elf": Race(name="Elf", str=1, agl=2, int=2, mnd=2)}
        fairy = {"Fairy": Race(name="Fairy", str=0, agl=1, int=2, mnd=4)}
        self.races.update(orc)
        self.races.update(human)
        self.races.update(elf)
        self.races.update(fairy)
