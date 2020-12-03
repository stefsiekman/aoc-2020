import aoc
import itertools
import numpy as np


def tree_count(trees, width, slope):
    steps = 0
    tree_count = 0
    posx = 0
    while steps < len(lines):
        tree_count += trees[steps][posx % width]
        posx += slope[0]
        steps += slope[1]

    return tree_count


if __name__ == "__main__":
    lines = aoc.parse_input(3)
    trees = [[t == '#' for t in l] for l in lines]
    width = len(lines[0])

    aoc.copy_answer(tree_count(trees, width, (3, 1)))

    values = [
        tree_count(trees, width, (1, 1)),
        tree_count(trees, width, (3, 1)),
        tree_count(trees, width, (5, 1)),
        tree_count(trees, width, (7, 1)),
        tree_count(trees, width, (1, 2)),
    ]

    aoc.copy_answer(np.prod(values))
