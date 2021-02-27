class Character:

    name = ""
    level = 0
    race = ""
    job = ""
    hp = 0
    gender = ""

    strength = 0
    agility = 0
    intelligence = 0
    mind = 0

    def __init__(self):
        self.name = ""
        self.level = 0
        self.race = ""
        self.job = ""
        self.maxHp = 0
        self.gender = ""

        self.strength = 0
        self.agility = 0
        self.intelligence = 0
        self.mind = 0

    def changeField(self, field, value):
        setattr(self, field, value)
