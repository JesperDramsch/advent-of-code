# Test Working solutions to Build a nice Day Class
import sys
sys.path.insert(0, '.')
from util import Day
from day01 import *

def test_part1():
    part1 = Day(1,1)
    part1.load(int)
    assert sum(part1.apply(fuel)) == 3279287

def test_part1_given_0():
    part1 = Day(1,1)
    part1.load(typing=int, data=[12])
    part1.answer(sum(part1.apply(fuel)))
    assert part1.result == 2

def test_part1_given_1():
    part1 = Day(1,1)
    part1.load(typing=int, data=[14])
    part1.answer(sum(part1.apply(fuel)))
    assert part1.result == 2

def test_part1_given_2():
    part1 = Day(1,1)
    part1.load(typing=int, data=[1969])
    part1.answer(sum(part1.apply(fuel)))
    assert part1.result == 654

def test_part1_given_3():
    part1 = Day(1,1)
    part1.load(typing=int, data=[100756])
    part1.answer(sum(part1.apply(fuel)))
    assert part1.result == 33583

def test_part2():
    part2 = Day(1,2)
    part2.load(int)
    assert sum(part2.apply(fuelchain)) == 4916076

def test_part2_given_0():
    part2 = Day(1,2)
    part2.load(typing=int, data=[14])
    part2.answer(sum(part2.apply(fuelchain)))
    assert part2.result == 2

def test_part2_given_1():
    part2 = Day(1,2)
    part2.load(typing=int, data=[1969])
    part2.answer(sum(part2.apply(fuelchain)))
    assert part2.result == 966

def test_part2_given_3():
    part2 = Day(1,2)
    part2.load(typing=int, data=[100756])
    part2.answer(sum(part2.apply(fuelchain)))
    assert part2.result == 50346