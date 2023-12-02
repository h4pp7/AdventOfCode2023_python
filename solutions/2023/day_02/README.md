# Day 2 (2023)

`Cube Conundrum` ([prompt](https://adventofcode.com/2023/day/2))

## Part 1
I decided to ignore the difference between `;` (separates draws) and `,` (serparates colors) for now.
Actually, I decided to ignore all of the punctuation and just parse the 4 needed values 
(game number, number of red, green, and blue cubes, respectively) with regex.

Fun thing I learned for parsing: you can have _rf-strings_ like so:

```python
[[n for n in re.findall(rf"(\d+) {c}", line)] for c in "rgb"]
```

Feels slightly cursed and is not better than just escaping the `\d` in this case 
but could be handy in other situations.

So, for each line get the biggest number for every color 
and check if any of those are bigger than the number of available cubes in that color.

## Part 2
Turns out we don't have to change the parsing and can keep ignoring all the punctuation.
Since I already parsed the max numbers of cubes for each color for each game,
part 2 is even easier than part 1.
I only need the sum of the products of each line, processed like this.
