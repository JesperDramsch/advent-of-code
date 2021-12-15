from util import Day
from aocd import submit
import networkx as nx
import matplotlib.pyplot as plt

def parse_graph(data):
    graph = nx.DiGraph()
    for i in range(len(data)):
        for ii in range(len(data[0])):
            for offset in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                x, y = offset
                if 0 <= ii + x < len(data[0]) and 0 <= i + y < len(data):
                    graph.add_weighted_edges_from([((i, ii), (i+y, ii+x), int(data[i+y][ii+x]))])
    return graph         

def main(day, part=1):
    if part == 1:
        graph = parse_graph(day.data)
        return nx.shortest_path_length(graph, source=(0, 0), target=(len(day.data[0])-1, len(day.data)-1), weight='weight')

if __name__ == "__main__":
    day = Day(15)
    #day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    # submit(p1, part="a", day=15, year=2021)

    # day.load(typing=str)
    # p2 = main(day, part=2)
    # print(p2)
    # submit(p2, part="b", day=15, year=2021)
