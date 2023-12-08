# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/8

import re
from itertools import cycle
from math import lcm

from ...base import StrSplitSolution, answer


def count_steps(start, goal, instr, net):
    node = start
    steps = 0
    while not node.endswith(goal):
        steps += 1
        node = net[node][next(instr)]
    return steps

class Solution(StrSplitSolution):
    _year = 2023
    _day = 8

    @answer((14893, 10241191004509))
    def solve(self) -> tuple[int, int]:
        input = self.input
        instr = cycle([0 if i == "L" else 1 for i in  input[0]])
        net = {a: (b, c) for a, b , c in [re.findall("[0-9A-Z]+", l) for l in
            input[2:]]}
        p1 = count_steps("AAA", "ZZZ", instr, net)
        p2 = lcm(*[count_steps(start, "Z", instr, net) for start in net.keys()
            if start.endswith("A")])
        return p1, p2
