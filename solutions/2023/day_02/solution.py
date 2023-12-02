# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/2

import re

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 2

    @staticmethod
    def minmax_cubes(line: str):
        return (max((int(n) for n in re.findall(f"(\\d+) {c}", line))) 
                for c in "rgb")

    @answer(2810)
    def part_1(self) -> int:
        score = 0
        for count, line in enumerate(self.input):
            r, g, b = self.minmax_cubes(line)
            if not any((r > 12, g > 13, b > 14)):
                score += count + 1
        return score

    @answer(69110)
    def part_2(self) -> int:
        power_sum = 0
        for line in self.input:
            r, g, b = self.minmax_cubes(line)
            power_sum += r * g * b
        return power_sum
