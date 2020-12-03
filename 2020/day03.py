from util import Day
import numpy as np


def preprocess(row):
    row = row.replace("#", "1 ").replace(".", "0 ").split()
    return np.array(row).astype(int)


def line(right, down, depth, width):
    d = range(0, depth, down)
    r = range(0, (len(d)) * right, right)
    return [(y, x % width) for x, y in zip(r, d)]


def main(day, part=1):
    day.apply(preprocess)
    day.data = np.array(day.data)
    deep, width = day.data.shape
    if part == 1:
        this_line = line(3, 1, deep, width)
        out = sum(day.data[tuple(np.transpose(this_line))])
    if part == 2:
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        out = 1
        for x, y in slopes:
            this_line = line(x, y, deep, width)
            out *= int(sum(day.data[tuple(np.transpose(this_line))]))
    return out


if __name__ == "__main__":
    day = Day(3)
    day.load(typing=str)

    print(main(day, part=2))

    # start on the open square (.) in the top-left corner and need to reach the bottom
    # follow a few specific slopes: rational numbers
