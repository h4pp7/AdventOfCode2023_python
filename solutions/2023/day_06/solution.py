# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/6

from functools import reduce
from operator import mul

from ...base import StrSplitSolution, answer, slow


def push(t):
    return (p*(t-p) for p in range(t))

class Solution(StrSplitSolution):
    _year = 2023
    _day = 6

    @answer(2344708)
    def part_1(self) -> int:
        time, distance = [[int(n) for n in l.split() if n.isnumeric()] for l in
                self.input]
        return reduce(mul, (len([d for d in push(time[r]) if d > distance[r]])
            for r in range(len(time))))

    @slow
    @answer(30125202)
    def part_2(self) -> int:
        time, distance = [int("".join([c for c in l if c.isdigit()])) for l in self.input]
        return len([d for d in push(time) if d > distance])
