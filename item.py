import json
import math
import logging
import inspect


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
        func = inspect.currentframe().f_back.f_code
        self.name = None

    def find_item(self, name: str):
        func = inspect.currentframe().f_back.f_code
        """
        Builds the item from json files
        """
        found_item = {}
        found = False
        while not found:
            for i in unique_items:
                if name in unique_items[i].values():
                    logging.debug(f"Found {name} in the database")
                    if unique_items[i]["code"] in weapons.keys():
                        logging.debug(f"Found {name} in the weapons database")
                        temp = weapons[unique_items[i]["code"]]["type"]
                        found_item[temp] = (item_types[temp])
                        found_item[unique_items[i]["code"]] = weapons[unique_items[i]["code"]]
                        found_item[i] = unique_items[i]
                        return found_item

                    elif unique_items[i]["code"] in armor.keys():
                        logging.debug(f"Found {name} in the armour database")
                        temp = armor[unique_items[i]["code"]]["type"]
                        found_item[temp] = item_types[temp]
                        found_item[unique_items[i]["code"]] = armor[unique_items[i]["code"]]
                        found_item[i] = unique_items[i]
                        return found_item

                    elif unique_items[i]["code"] in item_types.keys():
                        logging.debug(f"Found {name} in the items database")
                        found_item[unique_items[i]["code"]] = item_types[unique_items[i]["code"]]
                        found_item[i] = (unique_items[i])
                        return found_item

            for i in weapons:
                if name in weapons[i].values():
                    logging.debug(f"Found {name} in the weapons database")
                    temp = weapons[i]["type"]
                    found_item[temp] = item_types[temp]
                    found_item[i] = weapons[i]
                    return found_item
            for i in armor:
                if name in armor[i].values():
                    logging.debug(f"Found {name} in the armor database")
                    temp = armor[i]["type"]
                    found_item[temp] = item_types[temp]
                    found_item[i] = armor[i]
                    return found_item
            if not found:
                logging.debug(f"{name} not found")
                break

    def make_item(self, item_dict: dict):
        func = inspect.currentframe().f_back.f_code
        property = 0
        item = {}
        ac = 0
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
        if "ac" in item_dict.keys():
            item["ac"] = item_dict["ac"]
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

    def build_stat_list(self, json_file_name):
        func = inspect.currentframe().f_back.f_code
        keyword = "prop"
        stats = []
        clean_stats = []
        stats_dict = {}
        f = open(json_file_name, 'r')
        data = json.load(f)
        for i in data:
            temp = data[i]
            for k in temp:
                if keyword in k:
                    stats.append(temp[k])
        for i in range(len(stats)):
            if stats[i] not in clean_stats:
                clean_stats.append(stats[i])
        for i in clean_stats:
            stats_dict[i] = ""
        return stats_dict
