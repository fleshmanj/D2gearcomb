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

    def make_stats(self,**attr):
        for k, v in attr.items():
            self.stats[k] = v
        if self.class_type == "Amazon":
            self.stats["life"] = ((self.stats["LifePerVitality"] / 4) * self.stats["vit"]) + (
                (self.stats["LifePerLevel"] / 4) * self.level) + self.stats["hpadd"]
            self.stats["stamina"] = (self.level * 1) + (self.stats["vit"] * 1)
            self.stats["mana"] = (self.level * 1.5) + (self.stats["enr"] * 1.5)
        if self.class_type == "Assassin":
            self.stats["life"] = ((self.stats["LifePerVitality"] / 4) * self.stats["vit"]) + (
                (self.stats["LifePerLevel"] / 4) * self.level) + self.stats["hpadd"]
            self.stats["stamina"] = (self.level * 1.25) + (self.stats["vit"] * 1.25)
            self.stats["mana"] = (self.level * 1.5) + (self.stats["enr"] * 1.75)
        if self.class_type == "Necromancer":
            self.stats["life"] = ((self.stats["LifePerVitality"] / 4) * self.stats["vit"]) + (
                (self.stats["LifePerLevel"] / 4) * self.level) + self.stats["hpadd"]
            self.stats["stamina"] = (self.level * 1) + (self.stats["vit"] * 1)
            self.stats["mana"] = (self.level * 2) + (self.stats["enr"] * 2)
        if self.class_type == "Barbarian":
            self.stats["life"] = ((self.stats["LifePerVitality"] / 4) * self.stats["vit"]) + (
                (self.stats["LifePerLevel"] / 4) * self.level) + self.stats["hpadd"]
            self.stats["stamina"] = (self.level * 1) + (self.stats["vit"] * 1)
            self.stats["mana"] = (self.level * 1) + (self.stats["enr"] * 1)
        if self.class_type == "Sorceress":
            self.stats["life"] = ((self.stats["LifePerVitality"] / 4) * self.stats["vit"]) + (
                (self.stats["LifePerLevel"] / 4) * self.level) + self.stats["hpadd"]
            self.stats["stamina"] = (self.level * 1.25) + (self.stats["vit"] * 1.25)
            self.stats["mana"] = (self.level * 1.5) + (self.stats["enr"] * 1.75)
        if self.class_type == "Druid":
            self.stats["life"] = ((self.stats["LifePerVitality"] / 4) * self.stats["vit"]) + (
                (self.stats["LifePerLevel"] / 4) * self.level) + self.stats["hpadd"]
            self.stats["stamina"] = (self.level * 1) + (self.stats["vit"] * 1)
            self.stats["mana"] = (self.level * 2) + (self.stats["enr"] * 2)
        if self.class_type == "Paladin":
            self.stats["life"] = ((self.stats["LifePerVitality"] / 4) * self.stats["vit"]) + (
                (self.stats["LifePerLevel"] / 4) * self.level) + self.stats["hpadd"]
            self.stats["stamina"] = (self.level * 1) + (self.stats["vit"] * 1)
            self.stats["mana"] = (self.level * 1.5) + (self.stats["enr"] * 1.5)

        if "mana%" in self.stats.keys():
            self.stats["mana"] *= 1 + (self.stats["mana%"] / 100)
        if "att%" in self.stats.keys():
            self.stats["att"] *= 1 + (self.stats["att%"] / 100)
        if "ac%" in self.stats.keys():
            logging.debug(f"base_ac is {self.stats['base_ac']}")
            logging.debug(f"ac% is {self.stats['ac%']}")
            self.stats["ac"] = self.stats["base_ac"] * (1 + (self.stats["ac%"] / 100))





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
                    logging.warning("No open slots to equip item")

                self.add_item_stats(item)
                self.make_stats(mana=0, stamina=0, life=0)
            else:
                print(f"Not enough strength to equip {item['name']}")

    def add_item_stats(self, item):
        logging.debug(item.keys())
        unallowed = ['name', 'index', 'lvl req']
        if "base_ac" not in self.stats.keys():
            self.stats["base_ac"] = 0
        for key, value in item.items():
            if key not in self.stats.keys() and key not in unallowed:
                self.stats[key] = 0
            if key not in unallowed and key != "ac%":
                self.stats[key] = self.stats[key] + item[key]
            if key == "mag%/lvl":
                self.stats["mag%"] = self.stats["mag%"] + (value * self.level)
            if key == "att%":
                self.stats["att%"] += item["att%"]
            if key == "mana%":
                self.stats["mana%"] += item["mana%"]
            if key == "ac":
                self.stats["base_ac"] += item["ac"]
                logging.debug(f"{item['name']} added {item['ac']} defense.")
            if key == "ac%":
                self.stats["ac%"] += item["ac%"]
            if key == "str":
                self.stats["str"] = self.stats["str"] + item["str"]
            if key == "dex":
                self.stats["dex"] = self.stats["dex"] + item["dex"]


    def remove_item_stats(self, item):
        for key, value in item.items():
            self.stats[key] = self.stats[key] - item[key]
            if self.stats[key] == 0:
                self.stats[key].pop()
