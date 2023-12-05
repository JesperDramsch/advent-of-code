from typing import Any
from day import Day
from aocd import submit
from functools import cached_property
from utils.parser import Parser


class Page:
    def __init__(self, page_data):
        self.src = page_data[0].split("-to-")[0]
        self.dest = page_data[0].split("-to-")[1].split(" ")[0]
        self._data = page_data[1:]
        self.build_map()

    def build_map(self):
        self._map = {}
        for line in self._data:
            target, source, rng = map(int, line.split())
            self._map[source, source + rng] = (target, target + rng)

    def __repr__(self):
        return f"{self.src} to {self.dest}"

    def __getitem__(self, __key: Any) -> Any:
        for (source_low, source_high), (target_low, _) in self._map.items():
            if source_low <= __key < source_high:
                return target_low + (__key - source_low)
        return __key


class Almanach(dict):
    def __init__(self, data):
        parser = Parser(data)
        parser.parse_list_of_lists(sep="\n\n", sep2="\n")
        self._data = parser.data
        self.build_pages()

    @cached_property
    def seeds(self):
        return list(map(int, self._data[0][0].split(" ")[1:]))

    def build_pages(self):
        for page in self._data[1:]:
            page = Page(page)
            self[page.src] = page

    def seed_location(self, seed):
        page = "seed"
        key = seed
        while page != "location":
            key = self[page][key]
            page = self[page].dest
        return key


def main(day, part=1):
    almanach = Almanach(day.data)
    if part == 1:
        return min(almanach.seed_location(seed) for seed in almanach.seeds)
    if part == 2:
        pass


if __name__ == "__main__":
    day = Day(5)
    day.download()

    day.load(process=False)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=5, year=2023)

    # day.load()
    # p2 = main(day, part=2)
    # print(p2)
    # submit(p2, part="b", day=5, year=2023)
