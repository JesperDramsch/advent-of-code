import sys
sys.path.insert(0, '.')
from util import Day
from day06 import *


def test_given():
    part1 = Day(6,1)
    part1.load("""COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L""".split())
    part1.apply(str.split, sep=")")
    
    chain = get_chain(part1.data)
    end_points = get_endpoints(part1.data)
    
    part1.answer(traverse_orbits(chain, end_points), v=True)

    assert part1.result == 42

def test_part1():
    part1 = Day(6,1)
    part1.load()
    part1.apply(str.split, sep=")")
    
    chain = get_chain(part1.data)
    end_points = get_endpoints(part1.data)
    
    part1.answer(traverse_orbits(chain, end_points), v=True)

    assert part1.result == 315757