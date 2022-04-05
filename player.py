import math
import pprint
import json

from item import Item
from utils import Debug as d
from utils import print_character_stats

d = d()
# d.toggle_debug(True)

classes = ["Assassin", "amazon", "barbarian", "druid", "necromancer", "paladin", "sorceress"]


class Player:
    """
    attribute priorities minimum strength, minimum dexterity, max, vitality
    """

    def __init__(self, class_type):
        self.class_type = class_type
        self.stats = {}
        self.level = 0
        self.life = 0
        self.stamina = 0
        self.mana = 0
        self.slots = {"head": None,
                      "glov": None,
                      "belt": None,
                      "feet": None,
                      "tors": None,
                      "rrin": None,
                      "lrin": None,
                      "neck": None,
                      "rarm": None,
                      "larm": None,
                      }

        self.set_stats(self.class_type)
        pass

    def set_stats(self, class_type: str):
        class_type = class_type.capitalize()
        f = open("json/charstats.json", "r")
        data = json.load(f)
        if class_type in data.keys():
            self.stats = data[class_type]
        self.life = ((self.stats["LifePerVitality"] / 4) * self.stats["vit"]) + (
                (self.stats["LifePerLevel"] / 4) * self.level) + self.stats["hpadd"]

    def levelup(self, number_of_levels=1):
        self.level += number_of_levels

    def add_attribute_points(self, attribute, number_of_points):
        attr = None
        if attribute == "strength":
            attr = "str"
        if attribute == "dexterity":
            attr = "dex"
        if attribute == "intellect":
            attr = "int"
        if attribute == " vitality":
            attr = "vit"
        if attr is not None:
            d.debug("added points")
            self.stats[attr] = self.stats[attr] + number_of_points

    def equip_item(self, name):
        temp = None
        item = Item()
        slot1 = None
        slot2 = None
        try:
            temp = item.find_item(name)
            temp = merge(temp)
        except:
            d.debug(f"Could not add {name}")

        if temp is not None:
            item = make_item(temp)
            d.debug(self.stats["str"])
            d.debug(item["reqstr"])
            if self.stats["str"] >= item["reqstr"]:
                if "BodyLoc1" in temp.keys():
                    slot1 = temp["BodyLoc1"]
                    slot2 = temp["BodyLoc2"]
                if self.slots[slot1] is None:
                    self.slots[slot1] = item
                    d.debug(f"Equipped item in {slot1}")
                elif self.slots[slot2] is None:
                    self.slots[slot2] = item
                    d.debug(f"Equipped item in {slot2}")
                else:
                    d.debug("No open slots to equip item")

                self.add_item_stats(item)
            else:
                print(f"Not enough strength to equip {item['name']}")

    def add_item_stats(self, item):
        unallowed = ['name', 'index', 'lvl req']
        for key, value in item.items():
            if key not in self.stats.keys() and key not in unallowed:
                self.stats[key] = 0
            if key not in unallowed:
                self.stats[key] = self.stats[key] + item[key]

    def remove_item_stats(self, item):
        for key, value in item.items():
            self.stats[key] = self.stats[key] - item[key]
            if self.stats[key] == 0:
                self.stats[key].pop()


def merge(item_dict: dict):
    new_dict = {}
    for k, v in item_dict.items():
        for next_key, next_value in v.items():
            new_dict[next_key] = next_value
    return new_dict


def make_item(item_dict: dict):
    property = 0
    item = {}
    if "minac" in item_dict.keys():
        ac = math.floor((item_dict["minac"] + item_dict["maxac"]) / 2)
    for k, v in item_dict.items():
        if "prop" in k:
            property += 1
            try:
                item[item_dict[f"prop{property}"]] = math.floor(
                    (item_dict[f"min{property}"] + item_dict[f"max{property}"]) / 2)
            except:
                item[item_dict[f"prop{property}"]] = item_dict[f"par{property}"]
    if "ac" in item.keys():
        item["ac"] = item["ac"] + ac

    if "lvl req" in item_dict.keys():
        item["lvl req"] = item_dict["lvl req"]
    else:
        item["levelreq"] = item_dict["levelreq"]
    if "index" in item_dict.keys():
        item["index"] = item_dict["index"]
    if "name" in item_dict.keys():
        item["name"] = item_dict["name"]
    if "reqstr" in item_dict.keys():
        item["reqstr"] = item_dict["reqstr"]
    else:
        item["reqstr"] = 0
    return item


if __name__ == "__main__":
    players = []
    for i in classes:
        temp = Player(i)
        players.append(temp)

    players[0].add_attribute_points("strength", 100)

    # print_character_stats(players[0].stats)
    players[0].equip_item("Griffon's Eye")
    players[0].equip_item("The Oculus")
    players[0].equip_item("Skullder's Ire")
    players[0].equip_item("Mara's Kaleidoscope")
    players[0].equip_item("Lidless Wall")
    players[0].equip_item("Magefist")
    players[0].equip_item("Silkweave")
    players[0].equip_item("Arachnid Mesh")
    players[0].equip_item("The Stone of Jordan")
    players[0].equip_item("The Stone of Jordan")
    # print_character_stats(players[0].stats)

    # players[0].equip_item("Skull Cap")

    unique_name = None
    name = None

    x = players[0].slots
    for k, v in x.items():
        try:
            if "index" in v.keys():
                unique_name = v["index"]
            if "name" in v.keys():
                name = v["name"]
            print(unique_name)
        except:
            print(f"{k} not equipped")
