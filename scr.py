import math

to_merge = {"circ":{
    "ItemType": "Circlet",
    "Code": "circ",
    "Equiv1": "helm",
    "Repair": 1,
    "Body": 1,
    "BodyLoc1": "head",
    "BodyLoc2": "head",
    "Rare": 1,
    "MaxSock1": 1,
    "MaxSock25": 2,
    "MaxSock40": 3,
    "Rarity": 3,
    "CostFormula": 1,
    "StorePage": "armo",
    "expansion": 1,
    "lineNumber": 76
},

"ci3": {
    "name": "Diadem",
    "version": 100,
    "rarity": 1,
    "spawnable": 1,
    "minac": 50,
    "maxac": 60,
    "durability": 20,
    "level": 85,
    "levelreq": 64,
    "cost": 58000,
    "gamble cost": 1382500,
    "code": "ci3",
    "namestr": "ci3",
    "magic lvl": 18,
    "alternategfx": "lit",
    "OpenBetaGfx": "lit",
    "normcode": "ci1",
    "ubercode": "ci2",
    "ultracode": "ci3",
    "invwidth": 2,
    "invheight": 2,
    "hasinv": 1,
    "gemsockets": 3,
    "gemapplytype": 1,
    "flippyfile": "flpci2",
    "invfile": "invci3",
    "type": "circ",
    "dropsound": "item_helm",
    "dropsfxframe": 12,
    "usesound": "item_helm",
    "transtbl": 5,
    "lightradius": 3,
    "durwarning": 3,
    "bitfield1": 3,
    "CharsiMagicLvl": 255,
    "GheedMagicLvl": 255,
    "AkaraMagicLvl": 255,
    "FaraMagicLvl": 255,
    "LysanderMagicLvl": 255,
    "DrognanMagicLvl": 255,
    "HratliMagicLvl": 255,
    "AlkorMagicLvl": 255,
    "OrmusMagicLvl": 255,
    "ElzixMagicLvl": 255,
    "AshearaMagicLvl": 255,
    "CainMagicLvl": 255,
    "HalbuMagicLvl": 255,
    "JamellaMagicLvl": 255,
    "LarzukMagicLvl": 255,
    "MalahMagicLvl": 255,
    "DrehyaMagicLvl": 255,
    "Transform": 1,
    "InvTrans": 2,
    "NightmareUpgrade": "xxx",
    "HellUpgrade": "xxx",
    "nameable": 1,
    "expansion": 1,
    "lineNumber": 116
},

"337":{
    "index": "Griffon's Eye",
    "version": 100,
    "enabled": 1,
    "ladder": 1,
    "rarity": 1,
    "lvl": 84,
    "lvl req": 76,
    "code": "ci3",
    "*type": "diadem",
    "cost mult": 5,
    "cost add": 5000,
    "prop1": "ac",
    "min1": 100,
    "max1": 200,
    "prop2": "cast2",
    "min2": 25,
    "max2": 25,
    "prop3": "allskills",
    "min3": 1,
    "max3": 1,
    "prop4": "extra-ltng",
    "min4": 10,
    "max4": 15,
    "prop5": "pierce-ltng",
    "min5": 15,
    "max5": 20,
    "expansion": 1
}
}

def merge(item_dict:dict):
    new_dict = {}
    for k,v in item_dict.items():
        for next_key, next_value in v.items():
            new_dict[next_key] = next_value
    return new_dict
    # new_dict = a
    # for i in b:
    #     new_dict[i] = b[i]
    # for i in c:
    #     new_dict[i] = c[i]
    # return new_dict

def make_item(item_dict:dict):
    property = 0
    item = {}
    ac = math.floor((item_dict["minac"] + item_dict["maxac"])/2)
    for k,v in item_dict.items():
        if "prop" in k:
            property += 1
            item[item_dict[f"prop{property}"]] = math.floor((item_dict[f"min{property}"]+item_dict[f"max{property}"])/2)
    if "ac" not in item.keys():
        item["ac"] = ac
    else:
        item["ac"] = item["ac"] + ac

    if "lvl req" in item_dict.keys():
        item["lvl req"] = item_dict["lvl req"]
    else:
        item["levelreq"] = item_dict["levelreq"]
    return item





    if "minac" in item_dict.keys():
        ac = math.floor((item_dict["minac"] + item_dict["maxac"])/2)

new = merge(to_merge)
make_item(new)
