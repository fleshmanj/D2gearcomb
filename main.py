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
from utils import Debug, classes
from item import Item
from player import Player
d = Debug()

def generate_random_genome(slots: int):
    genome = []
    for i in range(slots):
        genome.append(random.randrange(2))
    d.debug(genome)
    return genome

if __name__ == "__main__":
    players = []
    for i in classes:
        temp = Player(i)
        players.append(temp)

    players[0].add_attribute_points("strength", 100)

    # print_character_stats(players[0].stats)
    players[0].equip_item("Griffon's Eye")
    players[0].equip_item("The Oculus")
    players[0].equip_item("Skullder's Ire")
    players[0].equip_item("Mara's Kaleidoscope")
    players[0].equip_item("Lidless Wall")
    players[0].equip_item("Magefist")
    players[0].equip_item("Silkweave")
    players[0].equip_item("Arachnid Mesh")
    players[0].equip_item("The Stone of Jordan")
    players[0].equip_item("The Stone of Jordan")
    # print_character_stats(players[0].stats)

    # players[0].equip_item("Skull Cap")

    unique_name = None
    name = None

    x = players[0].slots
    for k, v in x.items():
        try:
            if "index" in v.keys():
                unique_name = v["index"]
            if "name" in v.keys():
                name = v["name"]
            print(unique_name)
        except:
            print(f"{k} not equipped")

