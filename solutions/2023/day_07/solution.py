# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/7

from collections import Counter

from ...base import TextSolution, answer


def parse(input):
    table = str.maketrans("AKQJ", "XWVU")
    input = input.translate(table)
    return [l.split() for l in input.split("\n")]

def rank(hand):
    freq = [v for k, v in Counter(hand).most_common()]
    match freq[0]:
        case 5: # five of a kind
            return "6" + hand
        case 4: # four of a kind
            return "5" + hand
        case 1: # high card
            return "0" + hand
        case 3 if freq[1] == 2: # full house
            return "4" + hand
        case 3: # three of a kind
            return "3" + hand
        case 2 if freq[1] == 2: # two pairs
            return "2" + hand
        case 2: # one pair
            return "1" + hand

class Solution(TextSolution):
    _year = 2023
    _day = 7

    @answer(254024898)
    def part_1(self) -> int:
        hands = parse(self.input)
        hands.sort(key = lambda val: rank(val[0]))
        score = 0
        for i, h in enumerate(hands):
            score += (i + 1) * int(h[1])
        return score

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
