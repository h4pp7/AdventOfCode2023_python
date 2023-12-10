# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/9

from collections import Counter

from ...base import StrSplitSolution, answer

def extrapolate(row, ex):
    diffs = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    if len(Counter(diffs)) == 1:
        return ex + diffs[-1]
    else:
        return extrapolate(diffs, ex + diffs[-1])

class Solution(StrSplitSolution):
    _year = 2023
    _day = 9

    @answer((1980437560, 977))
    def solve(self) -> tuple[int, int]:
        rows = [[int(n) for n in r.split()] for r in self.input]
        p1 = sum([extrapolate(r, r[-1]) for r in rows])
        p2 = sum([extrapolate(list(reversed(r)), r[0]) for r in rows])
        return p1, p2
