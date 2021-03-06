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

f = open("json/SetItems.json", "r")
set_items = json.load(f)
f.close()

f = open("json/Sets.json", "r")
sets = json.load(f)
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

            for i in set_items:
                if name in set_items[i].values():
                    logging.debug(f"Found {name} in set_items")
                    if set_items[i]["item"] in weapons.keys():
                        logging.debug(f"Found {name} in the weapons database")
                        temp = weapons[set_items[i]["item"]]
                        found_item[temp] = (item_types[temp])
                        found_item[set_items[i]["item"]] = weapons[set_items[i]["item"]]
                        found_item[i] = set_items[i]
                        return found_item

                    elif set_items[i]["item"] in armor.keys():
                        logging.debug(f"Found {name} in the armour database")
                        temp = armor[set_items[i]["item"]]
                        found_item[temp["type"]] = item_types[temp["type"]]
                        found_item[set_items[i]["item"]] = armor[set_items[i]["item"]]
                        found_item[i] = set_items[i]
                        return found_item

                    elif set_items[i]["item"] in item_types.keys():
                        logging.debug(f"Found {name} in the items database")
                        found_item[set_items[i]["item"]] = item_types[set_items[i]["item"]]
                        found_item[i] = (set_items[i])
                        return found_item
            if not found:
                logging.debug(f"{name} not found")
                break

    def make_item(self, item_dict: dict):
        logging.debug(f"item_dict:{item_dict}")
        func = inspect.currentframe().f_back.f_code
        property = 0
        aproperty = 0
        item = {}

        # Commented out for max item defense testing
        # if "minac" in item_dict.keys():
        #     item["ac"] = math.floor((item_dict["minac"] + item_dict["maxac"]) / 2)

        if "maxac" in item_dict.keys():
            item["ac"] = item_dict["maxac"]
        for k, v in item_dict.items():
            if str(k).startswith("prop"):
                property += 1
                try:
                    # item[item_dict[f"prop{property}"]] = math.floor(
                    #     (item_dict[f"min{property}"] + item_dict[f"max{property}"]) / 2)
                    # added max modifiers
                    if v == "ac":
                        if "ac" in item.keys():
                            item["ac"] = item["ac"] + item_dict[f"max{property}"]
                    else:
                        item[item_dict[f"prop{property}"]] = math.floor(item_dict[f"max{property}"])
                except:
                    item[item_dict[f"prop{property}"]] = item_dict[f"par{property}"]
            elif str(k).startswith("aprop"):
                aproperty += 1
                try:
                    # item[item_dict[f"prop{property}"]] = math.floor(
                    #     (item_dict[f"min{property}"] + item_dict[f"max{property}"]) / 2)
                    # added max modifiers

                    item[f"aprop{aproperty}_{item_dict[f'aprop{aproperty}a']}"] = math.floor(item_dict[f"amax{aproperty}a"])
                except:
                    item[f"aprop{aproperty}_{item_dict[f'aprop{aproperty}a']}"] = item_dict[f"apar{aproperty}a"]


        if "ac" in item.keys():
            # logging.debug(f"ac in {item_dict['name']}")
            if "ac%" in item_dict.values():
                logging.debug(f"{item_dict['name']}'s defense set to {item['ac'] * (1 + (item['ac%'] / 100))}")
                item["ac"] *= 1 + (item["ac%"] / 100)
                item["ac%"] = 0

        if "ac%" in item_dict.keys() and "ac" not in item.keys():
            logging.debug(f"{item_dict['name']}'s defense set to {item_dict['ac%']}")
            item["ac%"] = item_dict["ac%"]

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
        if "reqdex" in item_dict.keys():
            item["reqdex"] = item_dict["reqdex"]
        else:
            item["reqdex"] = 0
        if "set" in item_dict.keys():
            item[item_dict["set"]] = 1
        if "add func" in item_dict.keys():
            item["add func"] = item_dict["add func"]
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
