from util import Day
from aocd import submit
from typing import List


def rolling_sum_comparison(data: List[int], window: int = 1) -> int:
    count: int = 0
    for i, _ in enumerate(data):
        if i >= window:
            last = sum(data[i - window : i])
            curr = sum(data[i - window + 1 : i + 1])
            if curr > last:
                count += 1
    return count


def main(day, part=1):
    if part == 1:
        return rolling_sum_comparison(day.data)
    if part == 2:
        return rolling_sum_comparison(day.data, 3)


if __name__ == "__main__":
    day = Day(1)
    day.download()

    day.load(typing=int)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=1, year=2021)

    day.load(typing=int)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=1, year=2021)
