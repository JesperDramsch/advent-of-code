from day import Day
from aocd import submit
from collections import defaultdict


class Lagoon(list):
    def __init__(self, data):
        self._data = data
        self.parse()

    @property
    def directions(self):
        return {"R": (0, 1), "L": (0, -1), "U": (1, 0), "D": (-1, 0)}

    def parse(self):
        for line in self._data:
            _direction, distance, color = line.split()
            direction = self.directions[_direction]
            distance = int(distance)

            self.append((direction, distance, color[2:-1]))

    def volume(self):
        # Shoelace
        pos = 0
        volume = 0
        perimeter = 0
        for (x, y), distance, _ in self:
            pos += x * distance
            volume += pos * y * distance
            perimeter += distance
        return volume + perimeter // 2 + 1

    def reencode(self):
        values = self.copy()
        self.clear()
        for _, _, color in values:
            distance = int(color[:-1], 16)
            direction = "RDLU"[int(color[-1])]
            self.append((self.directions[direction], distance, color))


def main(day, part=1):
    lagoon = Lagoon(day.data)
    if part == 2:
        lagoon.reencode()
    return lagoon.volume()


if __name__ == "__main__":
    day = Day(18)
    day.download()

    day.load()
    #     data = """R 6 (#70c710)
    # D 5 (#0dc571)
    # L 2 (#5713f0)
    # D 2 (#d2c081)
    # R 2 (#59c680)
    # D 2 (#411b91)
    # L 5 (#8ceee2)
    # U 2 (#caa173)
    # L 1 (#1b58a2)
    # U 2 (#caa171)
    # R 2 (#7807d2)
    # U 3 (#a77fa3)
    # L 2 (#015232)
    # U 2 (#7a21e3)"""

    #     day.load(data)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=18, year=2023)

    # day.load()
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=18, year=2023)
