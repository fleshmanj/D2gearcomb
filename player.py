import math
import pprint
import json
import logging
import inspect

from item import Item
from utils import print_character_stats, merge

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
        attribute = attribute.lower()
        if attribute == "strength":
            attr = "str"
        if attribute == "dexterity":
            attr = "dex"
        if attribute == "intellect":
            attr = "int"
        if attribute == "vitality":
            attr = "vit"
        if attribute == "energy":
            attr = "enr"
        if attr is not None:
            logging.debug(f"added {number_of_points} to {attribute}")
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
            logging.debug(f"Could not add {name}")

        if temp is not None:
            item = item.make_item(temp)
            logging.debug(f'player has {self.stats["str"]} and needs {item["reqstr"]}')
            if self.stats["str"] >= item["reqstr"]:
                if "BodyLoc1" in temp.keys():
                    slot1 = temp["BodyLoc1"]
                    slot2 = temp["BodyLoc2"]
                if self.slots[slot1] is None:
                    self.slots[slot1] = item
                    logging.debug(f"Equipped item in {slot1}")
                elif self.slots[slot2] is None:
                    self.slots[slot2] = item
                    logging.debug(f"Equipped item in {slot2}")
                else:
                    logging.warn("No open slots to equip item")

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








