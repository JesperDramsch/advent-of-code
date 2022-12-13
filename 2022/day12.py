from day import Day
from aocd import submit
import networkx as nx


def build_graph(data):
    """Build graph from 2D structure

    Parameters
    ----------
    data : List(List(int)
        Data of map

    Returns
    -------
    G : networkx.DiGraph
        Directed graph of map
    """
    # Build graph from 2 dimensional array
    G = nx.grid_2d_graph(len(data), len(data[0]), create_using=nx.DiGraph)
    # Remove edges that are not valid
    G.remove_edges_from([(a, b) for a, b in G.edges if data[b[0]][b[1]] > data[a[0]][a[1]] + 1])
    # Faster than building the graph from scratch
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
