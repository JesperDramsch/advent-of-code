from util import Day
from itertools import combinations
import numpy as np


def combine(data: list, r: int = 2) -> int:
    for comb in combinations(data, r):
        if sum(comb) == 2020:
            return np.prod(comb)


if __name__ == "__main__":
    day1 = Day(1)
    day1.load()

    print(combine(day1.data))
    print(combine(day1.data, 3))