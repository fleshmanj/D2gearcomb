import json

from utils import Debug as d

d = d()
# d.toggle_debug(True)

f = open("json/ItemTypes.json", "r")
item_types = json.load(f)
f.close()

f = open("json/armor.json", "r")
armor = json.load(f)
f.close()

f = open("json/weapons.json", "r")
weapons = json.load(f)
f.close()

f = open("json/UniqueItems.json", "r")
unique_items = json.load(f)
f.close()


class Item:

    def __init__(self):
        self.name = None

    def find_item(self, name:str):
        found_item = {}
        found = False
        while not found:
            for i in unique_items:
                if name in unique_items[i].values():
                    d.debug(f"Found {name} in the database")
                    if unique_items[i]["code"] in weapons.keys():
                        d.debug(f"Found {name} in the weapons database")
                        temp = weapons[unique_items[i]["code"]]["type"]
                        found_item[temp] = (item_types[temp])
                        found_item[unique_items[i]["code"]] = weapons[unique_items[i]["code"]]
                        found_item[i] = unique_items[i]
                        return found_item

                    elif unique_items[i]["code"] in armor.keys():
                        d.debug(f"Found {name} in the armour database")
                        temp = armor[unique_items[i]["code"]]["type"]
                        found_item[temp] = item_types[temp]
                        found_item[unique_items[i]["code"]] = armor[unique_items[i]["code"]]
                        found_item[i] = unique_items[i]
                        return found_item

                    elif unique_items[i]["code"] in item_types.keys():
                        d.debug(f"Found {name} in the items database")
                        found_item[unique_items[i]["code"]] = item_types[unique_items[i]["code"]]
                        found_item[i] = (unique_items[i])
                        return found_item

            for i in weapons:
                if name in weapons[i].values():
                    d.debug(f"Found {name} in the weapons database")
                    temp = weapons[i]["type"]
                    found_item[temp] = item_types[temp]
                    found_item[i] = weapons[i]
                    return found_item
            for i in armor:
                if name in armor[i].values():
                    d.debug(f"Found {name} in the armor database")
                    temp = armor[i]["type"]
                    found_item[temp] = item_types[temp]
                    found_item[i] = armor[i]
                    return found_item
            if not found:
                d.debug(f"{name} not found")
                break
