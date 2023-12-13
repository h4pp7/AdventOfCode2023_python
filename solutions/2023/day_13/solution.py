# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/13

from ...base import TextSolution, answer
from pprint import pprint


def find_symmetrie(pattern):
    for i in range(len(pattern) - 1):
        if pattern[i] == pattern[i + 1]:
            for l, m in zip(reversed(pattern[:i + 1]), pattern[i + 1:]):
                if l != m:
                    break
            else:
                return i + 1
    return 0

class Solution(TextSolution):
    _year = 2023
    _day = 13

    @answer(27502)
    def part_1(self) -> int:
        patterns = [[[s for s in l] for l in p.split("\n")] for p in
                self.input.split("\n\n")]
        horizontal = sum([find_symmetrie(p) for p in patterns]) * 100
        patterns = [[list(row) for row in zip(*reversed(p))] for p in patterns]
        vertical = sum([find_symmetrie(p) for p in patterns])
        return horizontal + vertical

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
