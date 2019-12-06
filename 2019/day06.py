from util import Day


def get_endpoints(pairs: list) -> list:
    list_pairs = pairs.copy()
    x, y = zip(*pairs)
    return list(set(y) - set(x))


def get_chain(pairs: list) -> dict:
    list_pairs = pairs.copy()
    return {y: (x if x != "COM" else 1) for x, y in list_pairs}


def traverse_orbits(all_orbits: dict, end_points: list):
    chain = all_orbits.copy()
    list_points = end_points.copy()
    orbits = 1
    for point in end_points:
        node = point
        nodes = []
        sub_orbits = []
        i = 0
        # Traverse Chain from endpoint until a "visited" node appears
        while type(node) != int:
            nodes.append(node)
            sub_orbits.append(i)
            node = chain[node]
            i += 1
        sub_orbits = [node + x for x in sub_orbits]  # add rest of chains from stop node
        orbits += sum(sub_orbits[1:])
        # print(sub_orbits)
        # Populate chains with node values and mark them visited
        for j, el in enumerate(nodes[::-1]):
            chain[el] = j + node
    [chain.pop(k) for k in all_orbits if type(chain[k]) != int]
    return orbits, chain


def center_search(orbits: list, end_one: str, end_two: str):
    chain = orbits.copy()
    center_one, one = traverse_orbits(chain, [end_one])
    center_two, two = traverse_orbits(chain, [end_two])

    common = set(one.keys()) & set(two.keys())
    closest = max(one[x] for x in common)

    return one[end_one] - 1 + two[end_two] - 1 - closest * 2


if __name__ == "__main__":
    part1 = Day(6, 1)
    part1.load()
    part1.apply(str.split, sep=")")

    chain = get_chain(part1.data)
    end_points = get_endpoints(part1.data)
    orbits, traverse = traverse_orbits(chain, end_points)
    part1.answer(orbits, v=True)

    part2 = Day(6, 2)
    part2.load()
    part2.apply(str.split, sep=")")

    chain = get_chain(part2.data)

    part2.answer(center_search(chain, "SAN", "YOU"), v=True)
