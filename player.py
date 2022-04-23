import math
import pprint
import json
import logging
import inspect
import item as item_py

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
        self.stats['life'] = ((self.stats["LifePerVitality"] / 4) * self.stats["base_vit"]) + (
                (self.stats["LifePerLevel"] / 4) * self.level) + self.stats["hpadd"]
        self.stats["points_to_spend"] = 0
        self.stats["str"] = self.stats["base_str"]
        self.stats["dex"] = self.stats["base_dex"]
        self.stats["enr"] = self.stats["base_enr"]
        self.stats["vit"] = self.stats["base_vit"]
        self.stats["stamina"] = self.stats["base_stamina"]

    def levelup(self, number_of_levels=1):
        self.level += number_of_levels
        self.stats["points_to_spend"] += 5 * number_of_levels

    def update_stats(self, **attr):
        self.add_inv_stats()

        for k, v in attr.items():
            self.stats[k] = v


        if self.class_type == "Amazon":
            self.stats["life"] = ((self.stats["LifePerVitality"] / 4) * self.stats["base_vit"]) + (
                    (self.stats["LifePerLevel"] / 4) * self.level) + self.stats["hpadd"] + self.stats["equipment_vitality"]
            self.stats["stamina"] = (self.level * 1) + (self.stats["base_vit"] + self.stats["equipment_vitality"]) + self.stats["base_stamina"] + self.stats["equipment_stamina"]
            self.stats["mana"] = (self.level * 1.5) + (self.stats["base_enr"] * 1.5)
        if self.class_type == "Assassin":
            self.stats["life"] = ((self.stats["LifePerVitality"] / 4) * self.stats["base_vit"]) + (
                    (self.stats["LifePerLevel"] / 4) * self.level) + self.stats["hpadd"] + self.stats["equipment_vitality"]
            self.stats["stamina"] = (self.level * 1.25) + ((self.stats["base_vit"] * 1.25) + self.stats["equipment_vitality"]) + self.stats["base_stamina"] + self.stats["equipment_stamina"]
            self.stats["mana"] = (self.level * 1.5) + (self.stats["base_enr"] * 1.75)
        if self.class_type == "Necromancer":
            self.stats["life"] = ((self.stats["LifePerVitality"] / 4) * self.stats["base_vit"]) + (
                    (self.stats["LifePerLevel"] / 4) * self.level) + self.stats["hpadd"] + self.stats["equipment_vitality"]
            self.stats["stamina"] = (self.level * 1) + (self.stats["base_vit"] + self.stats["equipment_vitality"]) + self.stats["base_stamina"] + self.stats["equipment_stamina"]
            self.stats["mana"] = (self.level * 2) + (self.stats["base_enr"] * 2)
        if self.class_type == "Barbarian":
            self.stats["life"] = ((self.stats["LifePerVitality"] / 4) * self.stats["base_vit"]) + (
                    (self.stats["LifePerLevel"] / 4) * self.level) + self.stats["hpadd"] + self.stats["equipment_vitality"]
            logging.debug(f"self.stats['stamina'] = {self.level * 1} + ({self.stats['base_vit']} + {self.stats['equipment_vitality']}) + {self.stats['equipment_stamina']}")
            self.stats["stamina"] = (self.level * 1) + (self.stats["base_vit"] + self.stats["equipment_vitality"]) + self.stats["equipment_stamina"]
            self.stats["mana"] = (self.level * 1) + (self.stats["base_enr"] * 1)
        if self.class_type == "Sorceress":
            self.stats["life"] = ((self.stats["LifePerVitality"] / 4) * self.stats["base_vit"]) + (
                    (self.stats["LifePerLevel"] / 4) * self.level) + self.stats["hpadd"] + self.stats["equipment_vitality"]
            self.stats["stamina"] = (self.level * 1.25) + ((self.stats["base_vit"] * 1.25) + self.stats["equipment_vitality"]) + self.stats["base_stamina"] + self.stats["equipment_stamina"]
            self.stats["mana"] = (self.level * 1.5) + (self.stats["base_enr"] * 1.75)
        if self.class_type == "Druid":
            self.stats["life"] = ((self.stats["LifePerVitality"] / 4) * self.stats["base_vit"]) + (
                    (self.stats["LifePerLevel"] / 4) * self.level) + self.stats["hpadd"] + self.stats["equipment_vitality"]
            self.stats["stamina"] = (self.level * 1) + (self.stats["base_vit"] + self.stats["equipment_vitality"]) + self.stats["base_stamina"] + self.stats["equipment_stamina"]
            self.stats["mana"] = (self.level * 2) + (self.stats["base_enr"] * 2)
        if self.class_type == "Paladin":
            self.stats["life"] = ((self.stats["LifePerVitality"] / 4) * self.stats["base_vit"]) + (
                    (self.stats["LifePerLevel"] / 4) * self.level) + self.stats["hpadd"] + self.stats["equipment_vitality"]
            self.stats["stamina"] = (self.level * 1) + (self.stats["base_vit"] + self.stats["equipment_vitality"]) + self.stats["base_stamina"] + self.stats["equipment_stamina"]
            self.stats["mana"] = (self.level * 1.5) + (self.stats["base_enr"] * 1.5)

        # Defense = (Dexterity / 4) + Total Defense from Equipment + Total Defense from Charms
        self.stats["ac"] = (self.stats["dex"]/4) + self.stats["equipment_ac"] + self.stats["charms_ac"] + self.stats["equipment_stamina"]

        if "mana%" in self.stats.keys():
            self.stats["mana"] *= 1 + (self.stats["mana%"] / 100)
        if "att%" in self.stats.keys():
            self.stats["att"] *= 1 + (self.stats["att%"] / 100)
        if "ac%" in self.stats.keys():
            logging.debug(f"ac is {self.stats['ac']}")
            logging.debug(f"ac% is {self.stats['ac%']}")
            self.stats["ac"] = self.stats["ac"] * (1 + (self.stats["ac%"] / 100))

    def add_attribute_points(self, attribute, number_of_points):
        attr = None
        attribute = attribute.lower()
        if attribute == "strength":
            attr = "base_str"
        if attribute == "dexterity":
            attr = "base_dex"
        if attribute == "intellect":
            attr = "base_int"
        if attribute == "vitality":
            attr = "base_vit"
        if attribute == "energy":
            attr = "base_enr"
        if attr is not None:
            logging.debug(f"added {number_of_points} to {attribute}")
            self.stats[attr] = self.stats[attr] + number_of_points

    def equip_item(self, equip_list: list):
        while True:
            need_str = False
            need_dex = False
            item_equiped = False
            for i in equip_list:
                temp = None
                item = Item()
                slot1 = None
                slot2 = None
                try:
                    temp = item.find_item(i)
                    temp = merge(temp)
                except Exception as e:
                    logging.debug(f"Could not add {i}")
                    logging.debug(e)

                if temp is not None:
                    item = item.make_item(temp)
                    logging.debug(f'player has {self.stats["base_str"]+ self.stats["str"]} and needs {item["reqstr"]}')

                    if self.stats["str"] + self.stats["base_str"] >= item["reqstr"] and self.stats["dex"] + self.stats["base_dex"] >= item["reqdex"]:
                        if "BodyLoc1" in temp.keys():
                            slot1 = temp["BodyLoc1"]
                            slot2 = temp["BodyLoc2"]
                        if self.slots[slot1] is None:
                            self.slots[slot1] = item
                            item_equiped = True
                            logging.debug(f"Equipped item in {slot1}")
                            equip_list.remove(i)
                            logging.debug(f"Removed {i}")
                        elif self.slots[slot2] is None:
                            self.slots[slot2] = item
                            item_equiped = True
                            logging.debug(f"Equipped item in {slot2}")
                            equip_list.remove(i)
                            logging.debug(f"Removed {i}")
                        else:
                            logging.warning("No open slots to equip item")
                    else:
                        logging.debug(f"Not enough strength to equip {item['index']}")
                        if item["reqstr"] > self.stats["str"] + self.stats["base_str"]:
                            need_str = True

                        if item["reqdex"] > self.stats["dex"] + self.stats["base_dex"]:
                            need_dex = True

            if not item_equiped and len(equip_list) == 0:
                if self.stats["points_to_spend"] > 0:
                    self.add_attribute_points("vitality", self.stats["points_to_spend"])
                    self.stats["points_to_spend"] -= self.stats["points_to_spend"]
                break
            else:
                if need_str:
                    if self.stats["points_to_spend"] > 0:
                        logging.debug("added 1 strength")
                        self.add_attribute_points("strength", 1)
                        self.stats["points_to_spend"] -= 1

                if need_dex:
                    if self.stats["points_to_spend"] > 0:
                        logging.debug("added 1 dexterity")
                        self.add_attribute_points("dexterity", 1)
                        self.stats["points_to_spend"] -= 1

                if self.stats["points_to_spend"] <= 0:
                    break

    def add_item_stats(self, gear):
        for slot, item in gear.items():
            if item is not None:
                unallowed = ['name', 'index', 'lvl req']
                required_stats = ["equipment_ac", "equipment_stamina", "equipment_vitality"]
                for i in required_stats:
                    if i not in self.stats.keys():
                        self.stats[i] = 0
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
                        self.stats["equipment_ac"] += item["ac"]
                        logging.debug(f"{item['name']} added {item['ac']} defense.")
                    if key == "ac%":
                        self.stats["ac%"] += item["ac%"]
                    if key == "str":
                        self.stats["str"] = self.stats["str"] + item["str"]
                    if key == "dex":
                        self.stats["dex"] = self.stats["dex"] + item["dex"]
                    if key == "stam":
                        logging.debug(f"{slot} added {value} stamina")
                        self.stats["equipment_stamina"] = self.stats["equipment_stamina"] + item["stam"]
                    if key == "vit":
                        logging.debug(f"{slot} added {value} vitality")
                        self.stats["equipment_vitality"] = self.stats["equipment_vitality"] + item["stam"]



    def add_inv_stats(self):
        if "charms_ac" not in self.stats.keys():
            self.stats["charms_ac"] = 0

    def reset_stats(self):
        stats_to_reset = ["mag%", "att%", "mana%", "equipment_ac", "ac%", "str", "dex", "vit"]
        for stat in stats_to_reset:
            self.stats[stat] = 0




    def remove_item_stats(self, item):
        for key, value in item.items():
            self.stats[key] = self.stats[key] - item[key]
            if self.stats[key] == 0:
                self.stats[key].pop()
