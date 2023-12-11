# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/10

from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2023
    _day = 10

    # @answer(1234)
    def part_1(self) -> int:
        # Use box drawing characters for easier visualization
        sketch = self.input.translate(str.maketrans("|-LJ7F.", "║═╚╝╗╔·"))
        pipemap = {
                complex(x, y): c
                    for y, l in enumerate(sketch.split("\n"))
                    for x, c in enumerate(l)
        }
        pipes = {
                "║": (-1j,  1j),
                "═": ( -1,  1 ),
                "╚": (-1j,  1 ),
                "╝": (-1j, -1 ),
                "╗": (-1 ,  1j),
                "╔": ( 1 ,  1j)
        }
        start = None
        for k, v in pipemap.items():
            if v == "S":
                start = k
                break
        for i in range(4):
            nxy = start + 1j**i
            if pipemap[nxy] in pipes:
                for d in pipes[pipemap[nxy]]:
                    print(pipemap[nxy], d - 1j**i)
        return start

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
