from util import Day
from aocd import submit

def use_all(data):
    data = [0] + sorted(data)
    one, three = 0, 1

    for x, y in zip(data[:-1], data[1:]):
        diff = y-x
        print(x, y)
        one += (diff == 1)
        three += (diff == 3)
    return one, three


def crawl_back_graph(data):
    data = [0] + sorted(data) + [max(data)+3]
    graph = {max(data)+3: 1}
    for i in range(max(data)+3, -1, -1):
        if i in data:
            graph[i] = sum(graph.get(i+k, 0) for k in range(1, 4))
    return graph



def build_graph(data):
    graph = {}
    for i in range(max(data)+3):
        graph[i] = [i+k in data for k in range(1, 4)]
    return graph

def main(day, part=1):
    if part == 1:
        one, three = use_all(day.data)
        print(one, three)
        out = one * three
    if part == 2:
        out = crawl_back_graph(day.data)[0]
    return out


if __name__ == "__main__":
    day = Day(10)
    day.download()

    day.load()
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=10, year=2020)

    day.load()
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=10, year=2020)
