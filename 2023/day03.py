from day import Day
from aocd import submit
import re
import uuid


class Part:
    def __init__(self, y, x, value):
        self.location = [y + i * 1j for i in range(x[0], x[1])]
        self.value = value
        self.id = uuid.uuid4()


class Engine(dict):
    def __init__(self):
        self.parts = {}
        self.symbols = {}

    def add_part(self, part):
        self.parts[part.id] = part
        for location in part.location:
            self[location] = part.id

    def add_symbol(self, symbol, location):
        self.symbols[location] = symbol

    def parse_map(self, data):
        engine_re = re.compile(r"(\d+)")
        symbol_re = re.compile(r"[^.\d]")
        for y, line in enumerate(data):
            for part in engine_re.finditer(line):
                self.add_part(Part(y, part.span(), int(part.group())))
            for x, symbol in enumerate(symbol_re.finditer(line)):
                self.add_symbol(symbol.group(), y + x * 1j)


def main(day, part=1):
    engine = Engine()
    engine.parse_map(day.data)
    if part == 1:
        print(engine)
        print(engine.symbols)
    if part == 2:
        pass


if __name__ == "__main__":
    day = Day(3)
    day.download()

    day.load()
    data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

    day.load(data)

    p1 = main(day)
    print(p1)
    # submit(p1, part="a", day=3, year=2023)

    # day.load()
    # p2 = main(day, part=2)
    # print(p2)
    # submit(p2, part="b", day=3, year=2023)
