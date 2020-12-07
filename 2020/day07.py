from util import Day
from aocd import submit
from collections import ChainMap
import re


def flatten(t):
    return [item for sublist in t for item in sublist]


def node(row):
    container, bags = row[:-1].split(" bags contain ")
    if "no other" in row:
        return {container: {}}
    else:
        bag_count = dict((" ".join(bag.split()[1:-1]), int(bag.split()[0])) for bag in bags.split(", "))
        return {container: bag_count}


def all_starts(graph, end):
    out = []
    for start in graph:
        out.extend(list(find_all_paths(graph, start, end, path=[])))
    out = set(flatten(out))
    out.remove("shiny gold")
    return out


def find_all_paths(graph, start, end=None, path=None):
    if path is None:
        path = []
    path = path + [start]
    if end is None or start == end:
        yield path
    if start not in graph:
        yield []
        return
    for node, val in graph[start].items():
        if node not in path:
            yield from find_all_paths(graph, node, end, path)


def bags(graph, start):
    total = 0
    for inside, num in graph[start].items():
        total += num + num * bags(graph, inside)
    return total


def main(day, part=1):
    day.apply(node)
    day.data = dict(ChainMap(*day.data))
    if part == 1:
        out = len(all_starts(day.data, "shiny gold"))
    if part == 2:
        out = bags(day.data, "shiny gold")
    return out


if __name__ == "__main__":
    day = Day(7)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=7, year=2020)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=7, year=2020)
