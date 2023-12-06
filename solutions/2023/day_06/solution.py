# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/6

from ...base import StrSplitSolution, answer
from operator import mul
from functools import reduce

class Solution(StrSplitSolution):
    _year = 2023
    _day = 6

    @answer(2344708)
    def part_1(self) -> int:
        time, distance = [[int(n) for n in l.split() if n.isnumeric()] for l in
                self.input]
        push = lambda t: [p*(t-p) for p in range(t)]
        return reduce(mul, [len([d for d in push(time[r]) if d > distance[r]])
            for r in range(len(time))])

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
