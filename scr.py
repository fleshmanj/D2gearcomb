class_type = "Sorceress"
stats = {"energy": 25, "mana%": 0}
level = 99


def make_stats(**attr):
    for k, v in attr.items():
        stats[k] = v
    if class_type == "Amazon":
        stats["life"] = (level * 2) + (stats["energy"] * 3)
        stats["stamina"] = (level * 1) + (stats["energy"] * 1)
        stats["mana"] = (level * 1.5) + (stats["energy"] * 1.5)
    if class_type == "Assassin":
        stats["life"] = (level * 2) + (stats["energy"] * 3)
        stats["stamina"] = (level * 1.25) + (stats["energy"] * 1.25)
        stats["mana"] = (level * 1.5) + (stats["energy"] * 1.75)
    if class_type == "Necromancer":
        stats["life"] = (level * 1.5) + (stats["energy"] * 2)
        stats["stamina"] = (level * 1) + (stats["energy"] * 1)
        stats["mana"] = (level * 2) + (stats["energy"] * 2)
    if class_type == "Barbarian":
        stats["life"] = (level * 2) + (stats["energy"] * 4)
        stats["stamina"] = (level * 1) + (stats["energy"] * 1)
        stats["mana"] = (level * 1) + (stats["energy"] * 1)
    if class_type == "Sorceress":
        stats["life"] = (level * 2) + (stats["energy"] * 3)
        stats["stamina"] = (level * 1.25) + (stats["energy"] * 1.25)
        stats["mana"] = (level * 1.5) + (stats["energy"] * 1.75)
    if class_type == "Druid":
        stats["life"] = (level * 1.5) + (stats["energy"] * 2)
        stats["stamina"] = (level * 1) + (stats["energy"] * 1)
        stats["mana"] = (level * 2) + (stats["energy"] * 2)
    if class_type == "Paladin":
        stats["life"] = (level * 2) + (stats["energy"] * 3)
        stats["stamina"] = (level * 1) + (stats["energy"] * 1)
        stats["mana"] = (level * 1.5) + (stats["energy"] * 1.5)

    stats["mana"] *= 1 + (stats["mana%"]/100)
    stats["att"] *= 1 + (stats["att%"] / 100)
    stats["ac"] *= 1 + (stats["ac%"] / 100)

make_stats(mana=0, stamina=0, life=0)
print(stats)