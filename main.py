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
from utils import build_stat_list
from utils import Debug as d

from item import Item

d = d()


def generate_random_genome(slots: int):
    genome = []
    for i in range(slots):
        genome.append(random.randrange(2))
    d.debug(genome)
    return genome


if __name__ == "__main__":
    pass

