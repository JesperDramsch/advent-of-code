# Test Working solutions to Build a nice Day Cass
import sys
sys.path.insert(0, '.')
from util import Day
from day01 import *

def test_part1():
    part1 = Day(1,1)
    part1.load(int)
    assert sum(part1.apply(fuel)) == 3279287

def test_part2():
    part2 = Day(1,2)
    part2.load(int)
    assert sum(part2.apply(fuelchain)) == 4916076