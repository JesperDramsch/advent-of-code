from day import Day
from aocd import submit
from utils.parser import Parser
from functools import cached_property

# Increase recursion limit
import sys

sys.setrecursionlimit(10000000)


class Pipe:
    pass

    # | is a vertical pipe connecting north and south.
    # - is a horizontal pipe connecting east and west.
    # ╰ is a 90-degree bend connecting north and east.
    # ╯ is a 90-degree bend connecting north and west.
    # ╮ is a 90-degree bend connecting south and west.
    # ╭ is a 90-degree bend connecting south and east.
    # . is ground; there is no pipe in this tile.
    # S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.


class PipeSystem(Parser):
    def __init__(self, data):
        super().__init__(data)
        self.data = self.convert_string(self.data)
        self.parse_list_of_lists(sep="\n", sep2="")
        self.parse_map()
        self.loop = list(self.find_loop(self.start))

    def __str__(self):
        return self.print(self.data)

    def convert_string(self, string):
        return (
            string.replace(".", " ")
            .replace("J", "╯")
            .replace("L", "╰")
            .replace("7", "╮")
            .replace("F", "╭")
            .replace("S", "⭐")
        )

    def print(self, data):
        return "\n".join("".join(line) for line in data)

    def print_data(self, data):
        for i, line in enumerate(self.data):
            if all(val == " " for val in line):
                continue
            for ii, val in enumerate(line):
                if (i + ii * 1j) in data:
                    print(val, end="")
                else:
                    print(" ", end="")
            print()

    def print_map(self):
        self.print_data(self.map)

    def print_loop(self):
        self.print_data(self.loop)

    def parse_map(self):
        self.map = {}
        for i, line in enumerate(self.data):
            for ii, val in enumerate(line):
                if val != " ":
                    self.map[i + ii * 1j] = val
                if val == "⭐":
                    self.start = i + ii * 1j
        if self.start is None:
            raise ValueError("No start found")

    def find_valid_neighbours(self, pos: complex) -> list:
        connections = {
            "|": (pos + 1, pos - 1),
            "-": (pos + 1j, pos - 1j),
            "╯": (pos - 1, pos - 1j),
            "╰": (pos - 1, pos + 1j),
            "╮": (pos + 1, pos - 1j),
            "╭": (pos + 1, pos + 1j),
            "⭐": (pos + 1, pos - 1, pos + 1j, pos - 1j),
        }
        neighbours = {
            pos + 1j: ("-", "╯", "╮"),
            pos - 1j: ("-", "╰", "╭"),
            pos + 1: ("|", "╰", "╯"),
            pos - 1: ("|", "╮", "╭"),
        }
        these_neighbours = {connection: neighbours[connection] for connection in connections[self.map[pos]]}

        return [neighbour for neighbour, valid in these_neighbours.items() if self.map.get(neighbour) in valid]

    @cached_property
    def neighbours(self):
        neighbours = {}
        for pos in self.map.keys():
            neighbours[pos] = self.find_valid_neighbours(pos)
        return neighbours

    def find_loop(self, pos: complex, prev: complex = None, visited: set = None) -> set:
        if visited is None:
            visited = set()
        if pos in visited:
            return visited
        visited.add(pos)
        for neighbour in self.neighbours[pos]:
            if neighbour != prev:
                if self.find_loop(neighbour, pos, visited):
                    return visited
        return set()


def main(day, part=1):
    pipes = PipeSystem(day.data)
    if part == 1:
        pipes.print_map()
        pipes.print_loop()
        return len(pipes.loop) // 2
    if part == 2:
        pass


if __name__ == "__main__":
    day = Day(10)
    day.download()

    day.load(process=False)
    #     data = """.FF7F
    # .FJ|.
    # SJ.L7
    # |F--J
    # LJ..."""

    #     day.load(data, process=False)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=10, year=2023)

    # day.load()
    # p2 = main(day, part=2)
    # print(p2)
    # submit(p2, part="b", day=10, year=2023)
