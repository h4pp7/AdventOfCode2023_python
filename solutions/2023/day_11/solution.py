# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/11

from ...base import StrSplitSolution, answer

from itertools import combinations

def column(image, i):
    return [row[i] for row in image]

def manhattan_distance(a, b):
    return sum([abs(ai - bi) for ai, bi in zip(a, b)])

def get_galaxies(image):
    return [(x, y) for y, row in enumerate(image) for x, c in
            enumerate(row) if c == "#"]

def get_empty_space(image):
    width = len(image[0])
    empty_rows = [ln for ln, l in enumerate(image) if not any(c == "#" for c in l)]
    empty_cols = [cn for cn in range(width) if not any(c == "#" for c in
        column(image, cn))]
    return empty_rows, empty_cols

def expand(galaxies, empty_rows, empty_cols, age):
    for i, galaxy in enumerate(galaxies):
        above = sum([galaxy[1] > r for r in empty_rows])
        right_of = sum([galaxy[0] > c for c in empty_cols])
        galaxies[i] = (galaxy[0] + (right_of * (age - 1)), galaxy[1] + (above
            * (age -1)))
    return galaxies

class Solution(StrSplitSolution):
    _year = 2023
    _day = 11

    @answer((9947476, 519939907614))
    def solve(self) -> tuple[int, int]:
        image = [[c for c in l] for l in self.input]
        empty_rows, empty_cols = get_empty_space(image)
        galaxies = get_galaxies(image)
        expand(galaxies, empty_rows, empty_cols, 2)
        p1 = sum([manhattan_distance(a, b) for a, b in combinations(galaxies,
            2)])
        galaxies = get_galaxies(image)
        expand(galaxies, empty_rows, empty_cols, 1000000)
        p2 = sum([manhattan_distance(a, b) for a, b in combinations(galaxies,
            2)])
        return p1, p2
