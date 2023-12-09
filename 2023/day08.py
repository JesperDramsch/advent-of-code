from day import Day
from aocd import submit
from utils.parser import Parser
from itertools import cycle


class Map(dict):
    def __init__(self, data):
        data = Parser(data)
        data.parse_list_of_lists()
        self._instructions = data.data[0][0]
        self._mapping = data.data[1:][0]
        self.current = "AAA"
        self.steps = 0
        self.rl_to_index = {"R": 1, "L": 0}
        self._parse()

    def _parse(self):
        for mapping in self._mapping:
            a, b = mapping.split(" = ")
            self[a] = b[1:-1].split(", ")

    def run(self):
        for instruction in cycle(self._instructions):
            self.current = self[self.current][self.rl_to_index[instruction]]
            self.steps += 1
            if self.current == "ZZZ":
                return self.steps


def main(day, part=1):
    if part == 1:
        return Map(day.data).run()
    if part == 2:
        pass


if __name__ == "__main__":
    day = Day(8)
    day.download()

    day.load(process=False)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=8, year=2023)

    # day.load()
    # p2 = main(day, part=2)
    # print(p2)
    # submit(p2, part="b", day=8, year=2023)
