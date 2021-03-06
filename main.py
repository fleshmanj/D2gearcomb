"""
GA (M, maxCycle):
1. Generate M chromosome (s) for first population
2. Cycle = 1
3. Condition = true
4. While Cycle <= maxCycle and condition == true:
   a. Implement crossover operation on random selected chromosomes
   b. Implement mutation operation on random selected chromosomes
   c. Select M chromosomes from generated ones to make the new generation
   d. Cycle = Cycle + 1
5. Return the best result of current generation
"""
import random
import logging
import inspect
import os

import utils
from utils import classes
from item import Item
from player import Player

if os.path.exists("./runlog.log"):
    os.remove('./runlog.log')

FORMAT = "[{%(levelname)s} %(filename)s:%(lineno)s 	- %(funcName)20s() ] %(message)s"
logging.basicConfig(filename='runlog.log', level=logging.DEBUG, format=FORMAT)


def generate_random_genome(slots: int):
    func = inspect.currentframe().f_back.f_code
    genome = []
    for i in range(slots):
        genome.append(random.randrange(2))
    return genome


if __name__ == "__main__":

    """
    up until 100
    crushing blow
    deadly strike 
    openwounds
    
    use custom breakpoints
    faster cast rate
    increased attack speed
    
    life stolen
    mana stolen
    """
    # Sorc test
    # player = Player("Sorceress")
    # sorc_equipment = ["Griffon's Eye", "The Oculus", "Aldur's Deception", "Mara's Kaleidoscope", "Lidless Wall",
    #                   "Magefist", "Aldur's Advance", "Arachnid Mesh", "The Stone of Jordan", "The Stone of Jordan"]
    # player.equip_item(sorc_equipment)

    # Barb test
    player = Player("Barbarian")

    barb_equipment = ["Boneflesh", "Bul Katho's Wedding Band", "Carrion Wind", "Dracul's Grasp","Gorerider", "Highlord's Wrath", "Swordback Hold", "The Gnasher", "Vampiregaze", "Verdugo's Hearty Cord"]
    player.levelup(99)
    player.equip_item(barb_equipment)

    for k,v in player.slots.items():
        if v != None:
            print(f"Equipped {v['index']} in {k}")

    player.add_item_stats(player.slots)
    player.update_stats(mana=0, stamina=0, life=0)



    # player.add_attribute_points("strength", 88)
    # player.add_attribute_points("vitality", 213)
    # player.add_attribute_points("dexterity", 181)



    unique_name = None
    name = None

    # x = player.slots
    # for k, v in x.items():
    #     try:
    #         if "index" in v.keys():
    #             unique_name = v["index"]
    #         if "name" in v.keys():
    #             name = v["name"]
    #         print(unique_name)
    #     except:
    #         print(f"{k} not equipped")
    # utils.print_character_stats(player.stats)

    for k,v in player.slots.items():
        if v != None:
            print(f"Equipped {v['index']} in {k}")

    for k, v in player.stats.items():
        print(f"{k}:{v}")


