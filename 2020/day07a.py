from util import Day
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def flatten(t):
    return [item for sublist in t for item in sublist]


def snackworkx(data):
    G = nx.DiGraph()
    nodes = []
    edges = []
    for row in data:
        container, bags = row[:-1].split(" bags contain ")
        clr = container.split()[1]
        if clr in ["bronze"]:
            clr = "peru"
        nodes.append((container, {"color": clr}))
        if "no other" in row:
            continue

        edges += [(container, " ".join(bag.split()[1:-1]), int(bag.split()[0])) for bag in bags.split(", ")]
    G.add_nodes_from(nodes)
    G.add_weighted_edges_from(edges)
    return G

def plot_graph(G):
    # pos = nx.layout.spring_layout(G)
    plt.figure(figsize=(20,10))
    pos = nx.layout.circular_layout(G)
    M = G.number_of_edges()

    num = {name: i for i, name in enumerate(np.unique(list(nx.get_node_attributes(G,'color').values())))}
    node_colors = [num[x] for x in list(nx.get_node_attributes(G,'color').values())]
    my_cmap = mpl.colors.ListedColormap([mpl.colors.to_rgba(x) for x in num.keys()])
    edge_colors = np.arange(2, M + 2, 1) / M * max(nx.get_edge_attributes(G,'weight').values())
    edge_alphas = [(5 + i) / (M + 4) for i in nx.get_edge_attributes(G,'weight').values()]

    nodes = nx.draw_networkx_nodes(G, pos, node_size=3, node_color=node_colors, cmap=my_cmap)
    edges = nx.draw_networkx_edges(
        G,
        pos,
        node_size=3,
        arrowstyle="->",
        arrowsize=5,
        edge_color=edge_colors,
        edge_cmap=plt.cm.Blues,
        width=1,
    )


    pc = mpl.collections.PatchCollection(edges, cmap=plt.cm.Blues)
    pc.set_array(edge_colors)
    plt.colorbar(pc)

    ax = plt.gca()
    ax.set_axis_off()
    # plt.show()
    plt.savefig("day07-suitcases.png", bbox_inches='tight')


if __name__ == "__main__":
    day = Day(7)
    day.download()

    day.load(typing=str)
    G = snackworkx(day.data)
    plot_graph(G)