# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/4

from collections import Counter

from ...base import StrSplitSolution, answer

class Solution(StrSplitSolution):
    _year = 2023
    _day = 4

    @answer(22897)
    def part_1(self) -> int:
        cards = [[n for n in card if n.isnumeric()]
                    for card in [line.split(" ") for line in self.input]]
        winning_cards = [len([k for k,v in Counter(card).items() if v>1])
                            for card in cards]
        return sum([pow(2, score - 1) for score in winning_cards if score > 0])

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
