from pony.orm import *


def loadData(db):
    loadJobs(db)
    loadRaces(db)
    loadSwords(db)
    loadMobs(db)


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

##### Load Items #####
@db_session
def loadSwords(db):
    if not db.Item.select(lambda i: i.name == "Kaskara" and i.type == "sword").first():
        s1 = db.Stats(str=3, agl=0, itl=0, mnd=0)
        db.Item(name="Kaskara", stats=s1, type="sword", value=1, image="https://i.imgur.com/hlO64Wp.png")
        s1 = db.Stats(str=6, agl=1, itl=0, mnd=0)
        db.Item(name="Antique", stats=s1, type="sword", value=1, image="https://i.imgur.com/Wv37LcE.png")
        s1 = db.Stats(str=9, agl=2, itl=1, mnd=0)
        db.Item(name="Knight", stats=s1, type="sword", value=1, image="https://i.imgur.com/tY8dTeq.png")
        s1 = db.Stats(str=12, agl=3, itl=2, mnd=1)
        db.Item(name="Anellas", stats=s1, type="sword", value=1, image="https://i.imgur.com/umWnXOn.png")
        s1 = db.Stats(str=15, agl=4, itl=3, mnd=2)
        db.Item(name="Barbaric", stats=s1, type="sword", value=1, image="https://i.imgur.com/futo1b4.png")
    db.commit()

#>>>>>>>>>>>>>>>Change images <<<<<<<<<
@db_session
def loadBows(db):
    if not db.Item.select(lambda i: i.name == "Raven" and i.type == "bow").first():
        s1 = db.Stats(str=0, agl=3, itl=0, mnd=0)
        db.Item(name="Raven", stats=s1, type="bow", value=1, image="https://i.imgur.com/hlO64Wp.png")
        s1 = db.Stats(str=1, agl=6, itl=0, mnd=0)
        db.Item(name="Light", stats=s1, type="bow", value=1, image="https://i.imgur.com/Wv37LcE.png")
        s1 = db.Stats(str=2, agl=9, itl=1, mnd=0)
        db.Item(name="Lost", stats=s1, type="bow", value=1, image="https://i.imgur.com/tY8dTeq.png")
        s1 = db.Stats(str=3, agl=12, itl=2, mnd=1)
        db.Item(name="Leaf", stats=s1, type="bow", value=1, image="https://i.imgur.com/umWnXOn.png")
        s1 = db.Stats(str=4, agl=15, itl=3, mnd=2)
        db.Item(name="MK", stats=s1, type="bow", value=1, image="https://i.imgur.com/futo1b4.png")
    db.commit()

@db_session
def loadCodices(db):
    if not db.Item.select(lambda i: i.name == "Wise" and i.type == "codice").first():
        s1 = db.Stats(str=0, agl=0, itl=0, mnd=3)
        db.Item(name="Wise", stats=s1, type="codice", value=1, image="https://i.imgur.com/hlO64Wp.png")
        s1 = db.Stats(str=0, agl=0, itl=1, mnd=6)
        db.Item(name="Trinitas", stats=s1, type="codice", value=1, image="https://i.imgur.com/Wv37LcE.png")
        s1 = db.Stats(str=0, agl=1, itl=2, mnd=9)
        db.Item(name="Star", stats=s1, type="codice", value=1, image="https://i.imgur.com/tY8dTeq.png")
        s1 = db.Stats(str=1, agl=2, itl=3, mnd=12)
        db.Item(name="Orbit", stats=s1, type="codice", value=1, image="https://i.imgur.com/umWnXOn.png")
        s1 = db.Stats(str=2, agl=3, itl=4, mnd=15)
        db.Item(name="SAB", stats=s1, type="codice", value=1, image="https://i.imgur.com/futo1b4.png")
    db.commit()

@db_session
def loadStaves(db):
    if not db.Item.select(lambda i: i.name == "Raven" and i.type == "staff").first():
        s1 = db.Stats(str=0, agl=0, itl=3, mnd=0)
        db.Item(name="Saphire", stats=s1, type="staff", value=1, image="https://i.imgur.com/hlO64Wp.png")
        s1 = db.Stats(str=0, agl=0, itl=6, mnd=1)
        db.Item(name="Fatal", stats=s1, type="staff", value=1, image="https://i.imgur.com/Wv37LcE.png")
        s1 = db.Stats(str=0, agl=1, itl=9, mnd=2)
        db.Item(name="Ancient", stats=s1, type="staff", value=1, image="https://i.imgur.com/tY8dTeq.png")
        s1 = db.Stats(str=1, agl=2, itl=12, mnd=3)
        db.Item(name="Winged", stats=s1, type="staff", value=1, image="https://i.imgur.com/umWnXOn.png")
        s1 = db.Stats(str=2, agl=3, itl=15, mnd=4)
        db.Item(name="Onyx", stats=s1, type="staff", value=1, image="https://i.imgur.com/futo1b4.png")
    db.commit()



##### Load Monsters #####
@db_session
def loadMobs(db):
    if not db.Item.select(lambda i: i.name == "OrcX" and i.type == "Orc").first():
        s1 = db.Stats(str=1, agl=1, itl=1, mnd=1)
        mob1 = db.Mob(name="OrcX", stats=s1, type="Orc", image="https://i.imgur.com/cqx50Sh.png")
        item1 = db.Item.select(lambda i: i.name == "Kaskara").first()
        item2 = db.Item.select(lambda i: i.name == "Barbaric").first()
        db.Drop(mob=mob1, item=item1, rate=0.5)
        db.Drop(mob=mob1, item=item2, rate=0.1)
    db.commit()



