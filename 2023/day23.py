from day import Day
from aocd import submit
from heapq import heappush, heappop


class Clouds:
    def __init__(self, data):
        self.parse(data)
        self.max = len(self.grid)
        self.visited = set()

    def __repr__(self):
        return f"Clouds({self.start}, {self.end})"

    def parse(self, data):
        self.grid = {}
        self.start = None
        self.end = None
        for i, line in enumerate(data):
            for ii, char in enumerate(line):
                if char != "#":
                    self.grid[i + ii * 1j] = char
                    if i == 0:
                        self.start = i + ii * 1j
                    if i == len(data) - 1:
                        self.end = i + ii * 1j

    def get_neighbors(self, pos):
        for i in [1j, -1j, 1, -1]:
            yield pos - i

    def longest_hike(self):
        dummy = 0
        queue = [(0, dummy, self.start, set())]

        max_dist = 0
        while queue:
            dist, _, pos, visited = heappop(queue)
            if pos in visited:
                continue
            visited.add(pos)
            if pos == self.end:
                if max_dist > dist:
                    self.visited = visited
                    max_dist = dist

            match self.grid[pos]:
                case "<":
                    neighbors = (pos - 1j,)
                case ">":
                    neighbors = (pos + 1j,)
                case "^":
                    neighbors = (pos - 1,)
                case "v":
                    neighbors = (pos + 1,)
                case ".":
                    neighbors = self.get_neighbors(pos)
            for neighbor in neighbors:
                if neighbor in self.grid:
                    heappush(queue, (dist - 1, dummy := dummy + 1, neighbor, visited.copy()))
        return -max_dist

    def print(self):
        for i in range(1 + int(max(x.real for x in self.grid))):
            for ii in range(1 + int(max(x.imag for x in self.grid))):
                if i + ii * 1j in self.visited:
                    print("O", end="")
                elif i + ii * 1j == self.start:
                    print("S", end="")
                elif i + ii * 1j == self.end:
                    print("E", end="")
                else:
                    print(self.grid.get(i + ii * 1j, "#"), end="")
            print()


def main(day, part=1):
    clouds = Clouds(day.data)
    print(clouds)
    clouds.longest_hike()
    clouds.print()
    if part == 1:
        return clouds.longest_hike()
    if part == 2:
        pass


if __name__ == "__main__":
    day = Day(23)
    day.download()

    day.load()
    #     data = """#.#####################
    # #.......#########...###
    # #######.#########.#.###
    # ###.....#.>.>.###.#.###
    # ###v#####.#v#.###.#.###
    # ###.>...#.#.#.....#...#
    # ###v###.#.#.#########.#
    # ###...#.#.#.......#...#
    # #####.#.#.#######.#.###
    # #.....#.#.#.......#...#
    # #.#####.#.#.#########v#
    # #.#...#...#...###...>.#
    # #.#.#v#######v###.###v#
    # #...#.>.#...>.>.#.###.#
    # #####v#.#.###v#.#.###.#
    # #.....#...#...#.#.#...#
    # #.#########.###.#.#.###
    # #...###...#...#...#.###
    # ###.###.#.###v#####v###
    # #...#...#.#.>.>.#.>.###
    # #.###.###.#.###.#.#v###
    # #.....###...###...#...#
    # #####################.#"""

    #     day.load(data)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=23, year=2023)

    # day.load()
    # p2 = main(day, part=2)
    # print(p2)
    # submit(p2, part="b", day=23, year=2023)
