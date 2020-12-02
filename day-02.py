import aoc
import itertools
import numpy as np


def is_valid(password):
    mi, ma, ch, pa = password
    cou = pa.count(ch)

    return mi <= cou <= ma


def is_valid_2(password):
    mi, ma, ch, pa = password

    return (pa[mi-1] == ch) ^ (pa[ma-1] == ch)


def parse_password(password):
    segments = password.split(" ")
    limits = segments[0].split("-")
    char = segments[1][:-1]
    entry = segments[2]
    return int(limits[0]), int(limits[1]), char, entry


if __name__ == "__main__":
    passwords = aoc.parse_input(2)

    print("Part 1")
    aoc.copy_answer(sum(is_valid(p) for p in map(parse_password, passwords)))

    print("Part 2")
    aoc.copy_answer(sum(is_valid_2(p) for p in map(parse_password, passwords)))
