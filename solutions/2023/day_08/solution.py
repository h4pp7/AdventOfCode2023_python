# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/8

import re
from itertools import cycle

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 8

    @answer(14893)
    def part_1(self) -> int:
        input = self.input
        instr = cycle([0 if i == "L" else 1 for i in  input[0]])
        net = {a: (b, c) for a, b , c in [re.findall("[A-Z]+", l) for l in
            input[2:]]}
        steps = 0
        node = "AAA"
        while node != "ZZZ":
            steps += 1
            node = net[node][next(instr)]
        return steps

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
