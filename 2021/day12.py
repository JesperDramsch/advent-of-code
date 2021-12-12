from util import Day
from aocd import submit
import networkx as nx


def build_graph(data):
    G = nx.Graph()

    for line in data:
        node1, node2 = line.split("-")
        G.add_edge(node1, node2)

        G.nodes[node1]["smol"] = node1.islower()
        G.nodes[node2]["smol"] = node2.islower()
    return G


def traverse_graph(graph, node="start", visited=None, part=1):

    # End node always returns
    if node == "end":
        return 1

    # Prepare the visited set or generate a copy to not modify common memory
    if visited is None:
        visited = set()
    else:
        visited = visited.copy()

    # If the cave is small, add to visited, big caves can be ignored
    if graph.nodes[node]["smol"]:
        visited.add(node)

    count = 0
    # Iterate through neighbouring caves
    for neighbor in graph.neighbors(node):
        # If the cave is visited and it's part 2, go and switch to part 1 implementation
        if neighbor in visited and part == 2 and neighbor != "start":
            count += traverse_graph(graph, neighbor, visited, 1)
        # If the cave is not visited, go there
        elif neighbor not in visited:
            count += traverse_graph(graph, neighbor, visited, part)
    return count


def main(day, part=1):
    day.data = build_graph(day.data)
    return traverse_graph(day.data, part=part)


if __name__ == "__main__":
    day = Day(12)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=12, year=2021)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=12, year=2021)
