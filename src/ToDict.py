from pony.orm import *


@db_session
def character(obj):
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
def item(obj):
    if obj is None:
        return None
    item = obj.to_dict()
    item['stats'] = obj.stats.to_dict()
    return item


@db_session
def mob(obj):
    if obj is None:
        return None
    mob = obj.to_dict()
    mob['stats'] = obj.stats.to_dict()
    mob['drops'] = []
    for element in obj.drops:
        drop = element.to_dict()
        drop['item'] = element.item.name
        mob['drops'].append(drop)
    # mob['drops'] = dict.fromkeys(, 0)
    # print(mob['drops'])
    return mob
