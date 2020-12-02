import aoc
import itertools
import numpy as np

if __name__ == "__main__":
    numbers = [int(s) for s in aoc.parse_input(1)]

    print("Part 1")
    combinations = itertools.permutations(numbers, 2)
    for com in combinations:
        if sum(com) == 2020:
            print(com)
            ans = np.prod(com)
            print(ans)
            aoc.copy_answer(ans)

    print("Part 2")
    combinations = itertools.permutations(numbers, 3)
    for com in combinations:
        if sum(com) == 2020:
            print(com)
            ans = np.prod(com)
            print(ans)
            aoc.copy_answer(ans)
