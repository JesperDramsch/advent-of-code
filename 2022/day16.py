from day import Day
from aocd import submit
from functools import cache
from collections import abc, deque
from dataclasses import dataclass

from cProfile import run

class FrozenDict(abc.Mapping):
    """A hashable dictionary that is immutable once created."""
    
    def __init__(self, *args, **kwargs):
        self._d = dict(*args, **kwargs)
        self._hash = None

    def __repr__(self):
        return str(self._d)

    def __iter__(self):
        return iter(self._d)

    def __len__(self):
        return len(self._d)
    
    def __delitem__(self, key):
        del self._d[key]
        self._hash = None

    def pop(self, key, default=None):
        self._hash = None
        return self._d.pop(key, default)

    def __getitem__(self, key):
        return self._d[key]
    
    def __setitem__(self, key, value):
        self._d[key] = value

    def __hash__(self):
        # It would have been simpler and maybe more obvious to 
        # use hash(tuple(sorted(self._d.iteritems()))) from this discussion
        # so far, but this solution is O(n). I don't know what kind of 
        # n we are going to run into, but sometimes it's hard to resist the 
        # urge to optimize when it will gain improved algorithmic performance.
        if self._hash is None:
            hash_ = 0
            for pair in self.items():
                hash_ ^= hash(pair)
            self._hash = hash_
        return self._hash


@dataclass
class Valve:
    name: str
    flow: int
    tunnels: tuple
    neighbours: FrozenDict = None
    hash: int = None

    def __repr__(self):
        return f"""Valve {self.name} has 
        flow rate={self.flow}; 
        tunnels lead to valves {', '.join(self.tunnels)}, 
        with shortest paths: {self.neighbours}\n"""
    
    def __len__(self):
        return len(self.tunnels)

    def __hash__(self):
        return hash((self.name, self.flow, self.tunnels))

        
def parse(data):
    valves = FrozenDict()
    
    for line in data:
        name, flow, tunnel = list(line)
        flow = int(flow)
        tunnels = tuple(tunnel.split(", "))
        valves[name] = Valve(name, flow, tunnels)

    return valves

def find_shortest_path(valves, start, end):
    # BFS
    visited = set()
    queue = deque([(start, 0)])
    while queue:
        current, steps = queue.popleft()
        if current == end:
            return steps
        visited.add(current)
        for tunnel in valves[current].tunnels:
            if tunnel not in visited:
                queue.append((tunnel, steps + 1))

def compress_valves(valves):
    # Find all valves with flow
    flow_valves = [valve.name for valve in valves.values() if valve.flow != 0] 

    # find the shortest path between all valves with flow
    for v in flow_valves+ ["AA"]:
        valves[v].neighbours = FrozenDict()
        for v2 in flow_valves:
            if v != v2:
                valves[v].neighbours[v2] = find_shortest_path(valves, v, v2)

    for v in flow_valves:
        if valves[v].flow == 0 and not v == "AA":
            valves.pop(v)
    
    return valves

@cache
def tunneling(valves, opened=(), valve="AA", minutes=30):
    
    if minutes <= 0:
        return 0

    if len(opened) == len(valves)-1:
        return 0

    max_steam = 0
    minutes -= 1
    current_steam = 0
    
    if valve not in opened:
        current_steam = minutes * valves[valve].flow
        opened = tuple(sorted(opened + (valve,)))

    for tunnel, steps in valves[valve].neighbours.items():
        max_steam = max(max_steam, current_steam + tunneling(valves, opened, valve=tunnel, minutes=minutes - steps + (current_steam == 0)))
    
    return max_steam

@cache
def floptunneling(valves, opened=(), all_valves=("AA", "AA"), all_minutes=(26, 26)):

    eleflop = all_minutes[0] > all_minutes[1]

    minutes = all_minutes[eleflop]
    valve = all_valves[eleflop]

    if max(all_minutes) <= 0:
        return 0

    if len(opened) == len(valves)-1:
        return 0

    if minutes <= 0:
        eleflop = not eleflop
        minutes = all_minutes[eleflop]
        valve = all_valves[eleflop]

    # print(all_valves, end="")
    max_steam = 0
    current_steam = 0
    minutes -= 1
    
    if valve not in opened:
        current_steam = minutes * valves[valve].flow
        opened = tuple(sorted(opened + (valve,)))

    for tunnel, steps in valves[valve].neighbours.items():
        new_minutes = minutes - steps + (current_steam == 0)
        if new_minutes < all_minutes[not eleflop]:
            all_minutes = (new_minutes, all_minutes[not eleflop])
            all_valves = (tunnel, all_valves[not eleflop])
        else:
            all_minutes = (all_minutes[not eleflop], new_minutes)
            all_valves = (all_valves[not eleflop], tunnel)
        # all_minutes = all_minutes[:eleflop] + (new_minutes,) + all_minutes[eleflop+1:]
        # all_valves = all_valves[:eleflop] + (tunnel,) + all_valves[eleflop+1:]
        max_steam = max(max_steam, current_steam + floptunneling(valves, opened, all_valves=all_valves, all_minutes=all_minutes))
    return max_steam


def main(day, part=1):
    regex = r"Valve ([A-Z]+)[a-z ]+\=(-?\d+)\;[a-z ]+([A-Z, ]+)"
    day.parse_regex(regex, typing=(str, int, str))
    day.data = parse(day.data)
    day.data = compress_valves(day.data)
    if part == 1:
        # return day.data
        return tunneling(day.data)
    if part == 2:
        # return elephant_tunneling(day.data)
        return floptunneling(day.data)


if __name__ == "__main__":
    day = Day(16)
    day.download()

    day.load()
    # p1 = main(day)
    # print(p1)
    # submit(p1, part="a", day=16, year=2022)

    day.load()
#     data = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
# Valve BB has flow rate=13; tunnels lead to valves CC, AA
# Valve CC has flow rate=2; tunnels lead to valves DD, BB
# Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
# Valve EE has flow rate=3; tunnels lead to valves FF, DD
# Valve FF has flow rate=0; tunnels lead to valves EE, GG
# Valve GG has flow rate=0; tunnels lead to valves FF, HH
# Valve HH has flow rate=22; tunnel leads to valve GG
# Valve II has flow rate=0; tunnels lead to valves AA, JJ
# Valve JJ has flow rate=21; tunnel leads to valve II"""

#     day.load(data)
    p2 = main(day, part=2)
    print(p2)
    # submit(p2, part="b", day=16, year=2022)
