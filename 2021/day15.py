from util import Day
from aocd import submit
import networkx as nx
import numpy as np


def process_tiling(tile, tiling=1):
    tile = np.array([[x for x in row] for row in tile], dtype=np.uint8)

    out_tiling = np.zeros((tile.shape[0] * tiling, tile.shape[1] * tiling), dtype=np.uint8)

    for i in range(tiling):
        for ii in range(tiling):
            new_tile = tile + i + ii
            new_tile[new_tile > 9] -= 9
            out_tiling[
                i * tile.shape[0] : (i + 1) * tile.shape[0], ii * tile.shape[1] : (ii + 1) * tile.shape[0]
            ] = new_tile
    return out_tiling


def parse_graph(data):
    graph = nx.DiGraph()
    for i in range(data.shape[0]):
        for ii in range(data.shape[1]):
            adjacent_edges = [
                ((i, ii), (i + y, ii + x), data[i + y, ii + x])
                for x, y in ((-1, 0), (1, 0), (0, 1), (0, -1))
                if 0 <= ii + x < data.shape[0] and 0 <= i + y < data.shape[1]
            ]
            graph.add_weighted_edges_from(adjacent_edges)
    return graph


def main(day, part=1):
    if part == 1:
        tiling = 1
    elif part == 2:
        tiling = 5
    day.data = process_tiling(day.data, tiling=tiling)
    graph = parse_graph(day.data)
    return nx.shortest_path_length(
        graph, source=(0, 0), target=(len(day.data[0]) - 1, len(day.data) - 1), weight="weight"
    )


if __name__ == "__main__":
    day = Day(15)
    # day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    # submit(p1, part="a", day=15, year=2021)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    # submit(p2, part="b", day=15, year=2021)
