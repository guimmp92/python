#!/usr/bin/python

"""
http://rosettacode.org/wiki/Conway's_Game_of_Life#Python
http://garagelab.com/profiles/blogs/conway-s-game-of-life-in-python
"""

from collections import Counter, defaultdict
import itertools

life_rules = defaultdict(int, {
    (1, 2): 1,  # live w/ 2 live neighbors -> live
    (1, 3): 1,  # live w/ 3 live neighbors -> live
    (0, 3): 1   # dead w/ 3 live neighbors -> live
    # anything else -> dead
})


def seed_universe(pattern):
    u = universe = defaultdict(int)

    # Blinker
    u[(1, 0)], u[(1, 1)], u[(1, 2)] = 1, 1, 1

    # Toad
    #u[(5, 5)], u[(5, 6)], u[(5, 7)] = 1, 1, 1
    #u[(6, 6)], u[(6, 7)], u[(6, 8)] = 1, 1, 1

    # Glider
    #u[(5, 5)], u[(5, 6)], u[(5, 7)] = 1, 1, 1
    #u[(6, 5)] = 1
    #u[(7, 6)] = 1

    return universe

neighbors_offset = list(itertools.product(range(-1, 2), range(-1, 2)))
neighbors_offset.remove((0, 0))


def get_neighbors(cell):
    neighbors = set()
    (x, y) = cell
    for dx, dy in neighbors_offset:
        neighbors.add((x+dx, y+dy))
    return list(neighbors)


def bigbang(pattern="blinker"):
    max_generations = 10
    universe = seed_universe(pattern)

    for g in range(max_generations):
        next_generation = defaultdict(int)
        live_cells = [position for position, state in universe.iteritems() if state == 1]
        print "live cells: {0}".format(live_cells)

        # For each live cell, retrieve the neighbor cells and tally them up.
        # If a cell is the neighbor of three live cells, it will have a count of 3.
        counts = Counter(n for c in live_cells for n in get_neighbors(c))

        # Now we have a count of all cells neighboring live cells, apply the rules
        # of life.
        for c in counts:
            next_generation[c] = life_rules[universe[c], counts[c]]

        # Replace the universe with the next gen.
        universe = next_generation

if __name__ == "__main__":
    bigbang(pattern="blinker")
