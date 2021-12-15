import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day15 import *

@pytest.fixture(scope="function")
def example():
    day = Day(15)
    data = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

    day.load(data, typing=str)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(15)
    day.load(typing=str)
    return day

def test_example(example):
    assert main(example, part=1) == 40

def test_example_p2(example):
    assert main(example, part=2) == 315

def test_part1(day):
    assert main(day, part=1) == 717

def test_part2(day):
    assert main(day, part=2) == False
