import json
import pprint
import logging
import inspect

from stat_meanings import stat_meanings


def merge(item_dict: dict):
    new_dict = {}
    for k, v in item_dict.items():
        for next_key, next_value in v.items():
            new_dict[next_key] = next_value
    return new_dict


classes = ["Assassin", "amazon", "barbarian", "druid", "necromancer", "paladin", "sorceress"]


def arrange_items(items: list) -> list:
    return []


def print_character_stats(my_dict):
    for key, value in my_dict.items():
        if key in stat_meanings:
            print(f"{stat_meanings[key]}: {value}")
        else:
            print(f"{key}: {value}")
