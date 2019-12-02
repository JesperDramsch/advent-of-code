# Test Working solutions to Build a nice Day Cass
import sys
sys.path.insert(0, '.')
from util import Day
from day02 import *

def test_part1():
    part1 = Day(2,1)
    part1.load(int, ",")
    
    part1.data[1] = 12
    part1.data[2] = 2
    assert compute(part1.data)[0] == 3101878

def test_part2():
    part2 = Day(2,2)
    part2.load(int, ",")

    part2.data[1] = 84
    part2.data[2] = 44
    assert compute(part2.data)[0] == 19690720