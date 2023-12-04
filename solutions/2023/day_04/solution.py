# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/4

from collections import Counter

from ...base import StrSplitSolution, answer

def get_winners(input):
    cards = [[n for n in card if n.isnumeric()]
                for card in [line.split(" ") for line in input]]
    return [len([k for k,v in Counter(card).items() if v>1])
                    for card in cards]

class Solution(StrSplitSolution):
    _year = 2023
    _day = 4

    @answer(22897)
    def part_1(self) -> int:
        return sum([2 ** (score - 1) for score in get_winners(self.input) if score > 0])

    @answer(5095824)
    def part_2(self) -> int:
        winners = get_winners(self.input)
        cards = [1 for w in winners]
        for i, n in enumerate(winners):
            self.debug(cards)
            for j in range(n):
                cards[i + j + 1] += cards[i]
        return sum(cards)
