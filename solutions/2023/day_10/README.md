# Day 10 (2023)

`Pipe Maze` ([prompt](https://adventofcode.com/2023/day/10))

## Part 1
Since I always get confused working with indices in these kind of puzzles
I'm going to use complex numbers for coordinates again
(like in an [Argand diagram](https://en.wikipedia.org/wiki/Complex_plane#Argand_diagram)).
The real part represents the x-coordinate and the imaginary the y-coordinate.
The nice thing about it, that you can get the orthogonal neighbours with:

```python
for i in range(4):
    print(c + 1j**i)
```

I should probably just hard-code what tile to replace S with for my input
and then figure out way how to do that programmatically later.

## Part 2

