# Python program showing
# a use of input()
from src import BlindRPG as rpg
from src import Database as D

db = D.Database(True)
game = rpg.BlindRPG(db)
game.createChar("1")
game.changeName("1", "Akk")
game.changeRace("1", "Orc")
game.checkDailyAction("1")
db.database.drop_all_tables(with_all_data=True)
