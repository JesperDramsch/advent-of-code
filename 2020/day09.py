from util import Day
from aocd import submit
import pandas as pd


def moving_sum(data: list, length=25) -> dict:
    out = []
    mx = len(data)
    for i, dat in enumerate(data):
        out.append((dat, [dat + data[x] for x in range(i + 1, min((i + length, mx)))]))
    return out


def first_break(data: dict, preamble=25) -> int:
    for i in range(preamble, len(data)):
        test = data[i][0]
        out = any([test in sums for _, sums in data[i-preamble:i]])
        if not out:
            return test


def find_sum(sequence, target):
    seq = pd.Series(sequence)

    for x in range(2, len(seq)):
        roll_sum = seq.rolling(x).sum()
        if sum(roll_sum == target) > 0:
            break
    pos = roll_sum.index[roll_sum == target].tolist()[0] + 1
    subseq = seq[pos - x : pos]
    lower, upper = min(subseq), max(subseq)
    return lower + upper


def main(day, part=1, preamble=25):
    sum_data = moving_sum(day.data, preamble)
    first = first_break(sum_data, preamble)
    if part == 1:
        out = first
    if part == 2:
        out = find_sum(day.data, first)
    return out


if __name__ == "__main__":
    day = Day(9)
    day.download()

    day.load()
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=9, year=2020)

    day.load()
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=9, year=2020)
