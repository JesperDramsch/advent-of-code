from util import Day
from aocd import submit
from functools import lru_cache


def lanternfish_handler(data, days):
    unique_days = set(data)
    fishies = {}
    for day in unique_days:
        fishies[day] = exponential_lanternfish(days, day)

    return sum(fishies[day] for day in data)


@lru_cache(None)
def exponential_lanternfish(day, fertility):
    if day <= 0:
        return 1
    if fertility == 0:
        return exponential_lanternfish(day - 1, 6) + exponential_lanternfish(day - 1, 8)

    return exponential_lanternfish(day - fertility, 0)


def main(day, part=1):
    if part == 1:
        days = 80
    if part == 2:
        days = 256
    return lanternfish_handler(day.data, days)


if __name__ == "__main__":
    day = Day(6)
    day.download()

    day.load(sep=",", typing=int)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=6, year=2021)

    day.load(sep=",", typing=int)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=6, year=2021)
