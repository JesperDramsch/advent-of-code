from day import Day
from aocd import submit
from itertools import combinations

import networkx as nx


def check_neighbours(data):
    for pair in combinations(data, 2):
        diffs = (abs(a - b) for a, b in zip(*pair))
        if sum(diffs) == 1:
            data[pair[0]] -= 1
            data[pair[1]] -= 1
    return data


def steam(data):
    min_x, max_x, min_y, max_y, min_z, max_z = find_extents(data)
    min_all, max_all = min(min_x, min_y, min_z), max(max_x, max_y, max_z)

    cube = nx.grid_graph(dim=[range(min_all - 2, max_all + 2)] * 3)

    hole = cube.copy()
    hole.remove_nodes_from(data.keys())

    lava = max(nx.connected_components(hole), key=len)
    return nx.edge_boundary(cube, lava)


def find_extents(data):
    min_x = min(data, key=lambda x: x[0])[0]
    max_x = max(data, key=lambda x: x[0])[0]
    min_y = min(data, key=lambda x: x[1])[1]
    max_y = max(data, key=lambda x: x[1])[1]
    min_z = min(data, key=lambda x: x[2])[2]
    max_z = max(data, key=lambda x: x[2])[2]
    return min_x, max_x, min_y, max_y, min_z, max_z


def main(day, part=1):
    day.parse_list_of_lists(sep="\n", sep2=",", typing=int)
    day.data = {tuple(d): 6 for d in day.data}
    if part == 1:
        return sum(x for x in check_neighbours(day.data).values())
    if part == 2:
        return sum(1 for _ in steam(day.data))


if __name__ == "__main__":
    day = Day(18)
    day.download()

    day.load()
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=18, year=2022)

    day.load()
    #     data = """2,2,2
    # 1,2,2
    # 3,2,2
    # 2,1,2
    # 2,3,2
    # 2,2,1
    # 2,2,3
    # 2,2,4
    # 2,2,6
    # 1,2,5
    # 3,2,5
    # 2,1,5
    # 2,3,5"""

    #     day.load(data)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=18, year=2022)
