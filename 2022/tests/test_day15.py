import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day15 import *

@pytest.fixture(scope="function")
def example():
    day = Day(15)
    data = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

    day.load(data)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(15)
    day.load()
    return day

## Part 1
def test_example(example):
    assert main(example, part=1, y=(10,11)) == 26

# def test_part1(day):
#     assert main(day, part=1) == 4717631

## Part 2
def test_example_p2(example):
    assert main(example, part=2, y=(0, 21)) == 56000011

# def test_part2(day):
#     assert main(day, part=2, y=(0, 4_000_001)) == 13197439355220
