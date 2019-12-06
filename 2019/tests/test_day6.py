import sys

sys.path.insert(0, ".")
from util import Day
from day06 import *


def test_given():
    part1 = Day(6, 1)
    part1.load(
        """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L""".split()
    )
    part1.apply(str.split, sep=")")

    chain = get_chain(part1.data)
    end_points = get_endpoints(part1.data)
    orbits, _ = traverse_orbits(chain, end_points)
    part1.answer(orbits)

    assert part1.result == 42


def test_part1():
    part1 = Day(6, 1)
    part1.load()
    part1.apply(str.split, sep=")")

    chain = get_chain(part1.data)
    end_points = get_endpoints(part1.data)

    orbits, _ = traverse_orbits(chain, end_points)

    part1.answer(orbits)

    assert part1.result == 315757


def test_given2():
    part2 = Day(6, 2)
    part2.load(
        """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN""".split()
    )
    part2.apply(str.split, sep=")")

    chain = get_chain(part2.data)

    part2.answer(center_search(chain, "SAN", "YOU"))

    assert part2.result == 4


def test_part2():
    part2 = Day(6, 2)
    part2.load()
    part2.apply(str.split, sep=")")

    chain = get_chain(part2.data)

    part2.answer(center_search(chain, "SAN", "YOU"))

    assert part2.result == 481
