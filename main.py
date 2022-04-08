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

    player = Player("Sorceress")
    player.add_attribute_points("strength", 136)
    player.add_attribute_points("dexterity", 100)
    player.equip_item("Griffon's Eye")
    player.equip_item("The Oculus")
    player.equip_item("Skullder's Ire")
    player.equip_item("Mara's Kaleidoscope")
    player.equip_item("Lidless Wall")
    player.equip_item("Magefist")
    player.equip_item("Silkweave")
    player.equip_item("Arachnid Mesh")
    player.equip_item("The Stone of Jordan")
    player.equip_item("The Stone of Jordan")

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
    for k,v in player.stats.items():
        print(f"{k}:{v}")