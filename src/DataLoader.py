from pony.orm import *


def loadData(db):
    loadJobs(db)
    loadRaces(db)
    loadSwords(db)


@db_session
def loadJobs(db):
    if not db.Job.select(lambda j: j.name == "Warrior").first():
        s1 = db.Stats(str=4, agl=1, itl=1, mnd=1)
        db.Job(name="Warrior", stats=s1, image="https://i.imgur.com/dHLGGNs.png")
        s2 = db.Stats(str=1, agl=4, itl=1, mnd=1)
        db.Job(name="Archer", stats=s2, image="https://i.imgur.com/XrBkP1O.png")
        s3 = db.Stats(str=1, agl=1, itl=4, mnd=1)
        db.Job(name="Sorcerer", stats=s3, image="https://i.imgur.com/vpZLrxn.png")
        s4 = db.Stats(str=1, agl=1, itl=1, mnd=4)
        db.Job(name="Priest", stats=s4, image="https://i.imgur.com/1XGAYei.png")
    db.commit()


@db_session
def loadRaces(db):
    if not db.Race.select(lambda r: r.name == "Orc").first():
        s1 = db.Stats(str=4, agl=2, itl=0, mnd=1)
        db.Race(name="Orc", stats=s1, faction="https://i.imgur.com/kcXnYg3.png")
        s2 = db.Stats(str=2, agl=2, itl=2, mnd=1)
        db.Race(name="Human", stats=s2, faction="https://i.imgur.com/kcXnYg3.png")
        s3 = db.Stats(str=1, agl=2, itl=2, mnd=2)
        db.Race(name="Elf", stats=s3, faction="https://i.imgur.com/g1a0Jxg.png")
        s4 = db.Stats(str=0, agl=1, itl=2, mnd=4)
        db.Race(name="Fairy", stats=s4, faction="https://i.imgur.com/KBUV5zt.png")
        s5 = db.Stats(str=3, agl=3, itl=3, mnd=3)
        db.Race(name="Dragon", stats=s5, faction="https://i.imgur.com/oHMPKUd.png")
    db.commit()


@db_session
def loadSwords(db):
    if not db.Item.select(lambda i: i.name == "Kaskara" and i.type == "sword").first():
        s1 = db.Stats(str=3, agl=0, itl=0, mnd=0)
        db.Item(name="Kaskara", stats=s1, type="sword", value=1, image="https://i.imgur.com/hlO64Wp.png")
        s1 = db.Stats(str=6, agl=1, itl=0, mnd=0)
        db.Item(name="Antique", stats=s1, type="sword", value=1, image="https://i.imgur.com/Wv37LcE.png")
        s1 = db.Stats(str=9, agl=2, itl=2, mnd=0)
        db.Item(name="Knight", stats=s1, type="sword", value=1, image="https://i.imgur.com/tY8dTeq.png")
        s1 = db.Stats(str=12, agl=1, itl=3, mnd=1)
        db.Item(name="Anellas", stats=s1, type="sword", value=1, image="https://i.imgur.com/umWnXOn.png")
        s1 = db.Stats(str=15, agl=4, itl=3, mnd=3)
        db.Item(name="Barbaric", stats=s1, type="sword", value=1, image="https://i.imgur.com/futo1b4.png")
    db.commit()
