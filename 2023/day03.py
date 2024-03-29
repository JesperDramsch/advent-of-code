import re
import uuid

from aocd import submit
from day import Day
from itertools import product
from functools import cached_property


class Part:
    def __init__(self, y, x, value):
        self.location = [y + i * 1j for i in range(x[0], x[1])]
        self.value = value
        self.id = uuid.uuid4()
        self.valid = False

    def __repr__(self):
        return f"Part({self.location=}, {self.value=})"


class Symbol:
    def __init__(self, location, symbol):
        self.location = location
        self.symbol = symbol
        self.id = uuid.uuid4()
        self.neighbours = None

    def __repr__(self):
        return f"Symbol({self.location=}, {self.symbol=})"

    @cached_property
    def gear_ratio(self):
        if self.symbol == "*" and len(self.neighbours) == 2:
            return self.neighbours[0].value * self.neighbours[1].value
        return 0


class Engine(dict):
    def __init__(self):
        self.parts = {}
        self.symbols = {}

    def add_part(self, part):
        self.parts[part.id] = part
        for location in part.location:
            self[location] = part.id

    def add_symbol(self, symbol):
        self.symbols[symbol.id] = symbol

    def parse_map(self, data):
        engine_re = re.compile(r"(\d+)")
        symbol_re = re.compile(r"[^.\d]")
        for y, line in enumerate(data):
            for part in engine_re.finditer(line):
                self.add_part(Part(y, part.span(), int(part.group())))
            for symbol in symbol_re.finditer(line):
                self.add_symbol(Symbol(y + symbol.span()[0] * 1j, symbol.group()))
        self._add_symbol_neighbours()

    def _neighbours(self, location):
        # The 8 adjacent locations are the given location plus each of the 8 directions
        return [location + coord[0] + coord[1] * 1j for coord in product((-1, 0, 1), repeat=2)]

    def _parts_next_to(self, location):
        return list(
            set(
                self.parts[self[part_location]]
                for part_location in self._neighbours(location)
                if part_location in self.keys()
            )
        )

    def _add_symbol_neighbours(self):
        for symbol in self.symbols.values():
            self.symbols[symbol.id].neighbours = self._parts_next_to(symbol.location)
            for valid_parts in self.symbols[symbol.id].neighbours:
                self.parts[valid_parts.id].valid = True

    @cached_property
    def gear_ratio_sum(self):
        return sum(symbol.gear_ratio for symbol in self.symbols.values())

    @cached_property
    def engine_sum(self):
        return sum(part.value for part in self.parts.values() if part.valid)


def main(day, part=1):
    engine = Engine()
    engine.parse_map(day.data)
    if part == 1:
        return engine.engine_sum
    if part == 2:
        return engine.gear_ratio_sum


if __name__ == "__main__":
    day = Day(3)
    day.download()

    day.load()

    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=3, year=2023)

    day.load()
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=3, year=2023)
