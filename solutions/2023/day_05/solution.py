# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/5

from ...base import TextSolution, answer

def map_seed(seed, maps):
    for map in maps:
        for r, d in map:
            if seed in r:
                seed += d
                break
    return seed

class Solution(TextSolution):
    _year = 2023
    _day = 5

    @answer(51752125)
    def part_1(self) -> int:
        seeds, *maps = [p for p in self.input.split("\n\n")]
        seeds = [int(w) for w in seeds.split() if w.isnumeric()]
        maps = [[[int(w) for w in l.split() if w.isnumeric()] for l in
            m.split("\n")][1:] for m in maps]
        for m in maps:
            self.debug(m)
        maps = [[(range(m[1], m[1] + m[2]), m[0] - m[1]) for m in l] for l in maps]
        return min([map_seed(seed, maps) for seed in seeds])

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
