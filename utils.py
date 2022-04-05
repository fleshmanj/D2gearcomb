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



def build_stat_list(json_file_name):
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

def print_character_stats(my_dict):
    for key, value in my_dict.items():
        if key in stat_meanings:
            print(stat_meanings[key], value)
        else:
            print(key,value)


