# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/2

import re

from ...base import StrSplitSolution, answer


def min_cubes(line: str) -> tuple:
    game = int(re.findall(r"\d+", line)[0])
    r, g, b = (max((int(n) for n in re.findall(f"(\\d+) {c}", line))) for c in "rgb")
    return game, r, g, b

class Solution(StrSplitSolution):
    _year = 2023
    _day = 2

    @answer(2810)
    def part_1(self) -> int:
        score = 0
        for line in self.input:
            game, r, g, b = min_cubes(line)
            if not any((r > 12, g > 13, b > 14)):
                score += game
        return score

    @answer(69110)
    def part_2(self) -> int:
        power_sum = 0
        for line in self.input:
            _, r, g, b = min_cubes(line)
            power_sum += r * g * b
        return power_sum
