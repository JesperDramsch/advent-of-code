from day import Day
from aocd import submit
from dataclasses import dataclass

import re
from math import prod


@dataclass
class ToyBoatRace:
    time: int
    winning_distance: int

    def strategies(self):
        return [x * (self.time - x) for x in range(1, self.time)]

    def count_wins(self):
        return sum(1 for x in self.strategies() if x > self.winning_distance)

    def __repr__(self):
        return f"{self.time=}, {self.winning_distance=}"


def parse_data(data):
    return (map(int, re.findall(r"\d+", line)) for line in data)


def main(day, part=1):
    time, distance = parse_data(day.data)
    if part == 1:
        races = [ToyBoatRace(t, d) for t, d in zip(time, distance)]
        return prod([race.count_wins() for race in races])
    if part == 2:
        pass


if __name__ == "__main__":
    day = Day(6)
    day.download()

    day.load()
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=6, year=2023)

    # day.load()
    # p2 = main(day, part=2)
    # print(p2)
    # submit(p2, part="b", day=6, year=2023)
