# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/1

from ...base import StrSplitSolution, answer


def calibration_value(line: str) -> int:
    digits = [char for char in line if char.isdigit()]
    return int(digits[0] + digits[-1])

def replace_numbers(line: str) -> str:
    numbers = {
            "one": "one1one", "two": "two2two", "three": "three3three",
            "four": "four4four", "five": "five5five", "six":"six6six",
            "seven":"seven7seven", "eight":"eight8eight", "nine":"nine9nine"}
    for num, digit in numbers.items():
        line = line.replace(num, digit)
    return line

class Solution(StrSplitSolution):
    _year = 2023
    _day = 1

    @answer(55971)
    def part_1(self) -> int:
        return sum([calibration_value(line) for line in self.input])
        pass

    @answer(54719)
    def part_2(self) -> int:
        return sum([calibration_value(replace_numbers(line)) for line in self.input])
