import json
import pprint

from stat_meanings import stat_meanings


class Debug:

    def __init__(self):
        self.debug_toggle = False

    def debug(self, string_to_print):
        if self.debug_toggle:
            print(string_to_print)

    def toggle_debug(self, input: bool):
        self.debug_toggle = input


def merge(item_dict: dict):
    new_dict = {}
    for k, v in item_dict.items():
        for next_key, next_value in v.items():
            new_dict[next_key] = next_value
    return new_dict

classes = ["Assassin", "amazon", "barbarian", "druid", "necromancer", "paladin", "sorceress"]




def print_character_stats(my_dict):
    for key, value in my_dict.items():
        if key in stat_meanings:
            print(stat_meanings[key], value)
        else:
            print(key, value)
