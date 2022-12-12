from day import Day
from aocd import submit
import networkx as nx


def build_graph(data):
    G = nx.DiGraph()

    for x, row in enumerate(data):
        for y, val in enumerate(row):
            # Forward
            if x < len(data) - 1 and data[x + 1][y] <= val + 1:
                G.add_edge((x, y), (x + 1, y))
            if y < len(row) - 1 and data[x][y + 1] <= val + 1:
                G.add_edge((x, y), (x, y + 1))
            # Backward
            if 0 < x and data[x - 1][y] <= val + 1:
                G.add_edge((x, y), (x - 1, y))
            if 0 < y and data[x][y - 1] <= val + 1:
                G.add_edge((x, y), (x, y - 1))
    return G


def find_square(carta, square):
    squares = []
    square = [ord(s) for s in square]
    for x, row in enumerate(carta):
        for y, col in enumerate(row):
            if col in square:
                squares.append((x, y))
    return squares


def main(day, part=1):
    day.parse_list_of_lists(sep="\n", sep2="")
    day.apply(ord)
    S, E = find_square(day.data, ["S", "E"])
    day.data[S[0]][S[1]] = ord("a")
    day.data[E[0]][E[1]] = ord("z")
    graph = build_graph(day.data)
    if part == 1:
        return nx.shortest_path_length(graph, source=S, target=E)
    if part == 2:
        possible_starts = find_square(day.data, ["a"])

        path_lengths = []
        for start in possible_starts:
            try:
                path_lengths.append(nx.shortest_path_length(graph, source=start, target=E))
            except nx.exception.NetworkXNoPath:
                pass
        return min(path_lengths)


if __name__ == "__main__":
    day = Day(12)
    day.download()

    day.load()
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=12, year=2022)

    day.load()
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=12, year=2022)
