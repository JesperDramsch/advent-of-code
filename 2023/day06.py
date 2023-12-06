from day import Day
from aocd import submit
from dataclasses import dataclass

import re
import math


@dataclass
class ToyBoatRace:
    time: int
    winning_distance: int

    def count_wins(self):
        # Nullstelle finden von x * (time - x) = self.winning_distance
        # self.time * x - x^2 = self.winning_distance
        # x^2 - self.time * x + self.winning_distance = 0
        # PQ-Formel!
        # x1, x2 = (-p/2) ± sqrt((p/2)^2 - q)
        # p = -self.time
        # q = self.winning_distance
        x1 = math.ceil((self.time / 2) - math.sqrt((self.time / 2) ** 2 - self.winning_distance))
        x2 = math.floor((self.time / 2) + math.sqrt((self.time / 2) ** 2 - self.winning_distance))

        return x2 - x1 + 1

    def __repr__(self):
        return f"{self.time=}, {self.winning_distance=}"


def parse_data(data):
    return (map(int, re.findall(r"\d+", line)) for line in data)


def main(day, part=1):
    time, distance = parse_data(day.data)
    if part == 1:
        races = [ToyBoatRace(t, d + 1) for t, d in zip(time, distance)]
        return math.prod([race.count_wins() for race in races])
    if part == 2:
        time = int("".join(map(str, time)))
        distance = int("".join(map(str, distance)))
        return ToyBoatRace(time, distance + 1).count_wins()


if __name__ == "__main__":
    day = Day(6)
    day.download()

    day.load()
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=6, year=2023)

    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=6, year=2023)
