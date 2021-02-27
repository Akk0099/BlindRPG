import Character as Char


class BlindRPG:
    chars = {}

    def __init__(self):
        pass

    def createChar(self, id):
        char = Char.Character()
        newChar = {id: char}
        self.chars.update(newChar)

    def getChar (self, id):
        return self.chars[id].__dict__

    def printchars(self):
        for char in self.chars:
            print(char)
            print(self.chars[char].__dict__)

    def changeChar(self, id, field, value):
        if self.chars[id]:
            self.chars[id].changeField(field, value)
