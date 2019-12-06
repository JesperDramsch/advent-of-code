from util import Day

def get_endpoints(pairs: list) -> list:
    x, y = zip(*pairs)
    return list(set(y)-set(x))

def get_chain(pairs:list) -> dict:
    return {y: (x if x != "COM" else 1) for x, y in pairs}

def traverse_orbits(chain: dict, end_points: list) -> int:
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
        sub_orbits = [node + x for x in sub_orbits] # add rest of chain from stop node
        orbits += sum(sub_orbits[1:])
        
        # Populate chain with node values and mark them visited
        for j, el in enumerate(nodes[::-1]):
            chain[el] = j + node

    return(orbits)


if __name__ == "__main__":
    part1 = Day(6,1)
    part1.load()
    part1.apply(str.split, sep=")")
    
    chain = get_chain(part1.data)
    end_points = get_endpoints(part1.data)
    
    part1.answer(traverse_orbits(chain, end_points), v=True)

