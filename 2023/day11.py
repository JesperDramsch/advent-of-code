from day import Day
from aocd import submit
from itertools import combinations


class Galaxy(set):
    def __init__(self, data):
        self.raw_data = data

    def find_empty_rows(self):
        empty_rows = set()

    def find_empty_cols(self):
        empty_cols = set()
        for i, line in enumerate(self.raw_data):
            for ii, point in enumerate(line):
                if point == ".":
                    empty_cols.add(ii)
        return empty_cols

    def parse_map(self, space=2):
        empty_rows = set()
        empty_cols = set([i for i in range(len(self.raw_data[0]))])
        points = set()
        for i, line in enumerate(self.raw_data):
            if line == "." * len(line):
                empty_rows.add(i)
                continue
            for ii, point in enumerate(line):
                if point == "#":
                    points.add((i, ii))
                    if ii in empty_cols:
                        empty_cols.remove(ii)

        v_offset = {}
        v_tracker = 0
        for i in range(len(self.raw_data)):
            v_offset[i] = v_tracker
            if i in empty_rows:
                v_tracker += space - 1

        h_offset = {}
        h_tracker = 0
        for i in range(len(self.raw_data[0])):
            h_offset[i] = h_tracker
            if i in empty_cols:
                h_tracker += space - 1

        for i in range(len(self.raw_data)):
            for ii in range(len(self.raw_data[0])):
                if (i, ii) in points:
                    self.add(i + v_offset[i] + (ii + h_offset[ii]) * 1j)

    def distances(self):
        for a, b in combinations(self, 2):
            yield abs(a.real - b.real) + abs(a.imag - b.imag)


def main(day, part=1, space=1_000_000):
    galaxy = Galaxy(day.data)
    if part == 1:
        galaxy.parse_map()
        return int(sum(galaxy.distances()))
    if part == 2:
        galaxy.parse_map(space=space)
        return int(sum(galaxy.distances()))


if __name__ == "__main__":
    day = Day(11)
    day.download()

    day.load()

    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=11, year=2023)

    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=11, year=2023)
