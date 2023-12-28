from day import Day
from aocd import submit
from heapq import heappush, heappop
import networkx as nx
import time
import sys

sys.setrecursionlimit(10000)


class Clouds:
    def __init__(self, data):
        self.parse(data)
        self.max = len(self.grid)
        self.visited = set()
        self.graph = nx.Graph()

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
            if pos + i in self.grid:
                yield pos + i

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

    def create_graph(self, dist=0, last_node=None, pos=None, last_pos=None):
        if last_node is None:
            last_node = self.start
        if pos is None:
            pos = self.start

        # End of the grid
        if pos == self.end:
            self.graph.add_edge(last_node, pos, weight=dist)
            return
        # Already visited
        if self.graph.has_edge(last_node, pos):
            return

        neighbors = list(self.get_neighbors(pos))
        # Adding a node to the graph when it's a junction
        if len(neighbors) > 2:
            self.graph.add_edge(last_node, pos, weight=dist)
            last_node = pos
            dist = 0
        # Moving further in the grid
        for neighbor in neighbors:
            if neighbor in self.grid and neighbor != last_pos:
                self.create_graph(dist + 1, last_node, neighbor, pos)

    def unconstrained_longest(self):
        self.create_graph()
        print(self.graph)
        # Find longest Path in graph
        max_dist = 0
        for path in nx.all_simple_paths(G=self.graph, source=self.start, target=self.end):
            max_dist = max(max_dist, nx.path_weight(self.graph, path, weight="weight"))
        return max_dist

    def print(self):
        for i in range(1 + int(max(x.real for x in self.grid))):
            print(i, end=" ")
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
    if part == 1:
        x = clouds.longest_hike()
        clouds.print()
        return x
    if part == 2:
        return clouds.unconstrained_longest()


if __name__ == "__main__":
    day = Day(23)
    day.download()

    day.load()
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=23, year=2023)

    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=23, year=2023)
