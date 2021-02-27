# Python program showing
# a use of input()
from src import BlindRPG as rpg

game = rpg.BlindRPG()
game.createChar(1)
game.printchars()
game.changeChar(1, "name", "Helder")
game.printchars()



