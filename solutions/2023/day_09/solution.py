# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/9

from collections import Counter

from ...base import StrSplitSolution, answer


def diff(row, ex):
    diffs = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    ex += diffs[-1]
    if len(Counter(diffs)) == 1:
        return ex
    else:
        return diff(diffs, ex)

class Solution(StrSplitSolution):
    _year = 2023
    _day = 9

    @answer(1980437560)
    def part_1(self) -> int:
        rows = [[int(n) for n in r.split()] for r in self.input]
        return sum([diff(r, r[-1]) for r in rows])

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
