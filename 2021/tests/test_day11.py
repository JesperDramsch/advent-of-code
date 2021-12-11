import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day11 import *

@pytest.fixture(scope="function")
def example():
    day = Day(11)
    data = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

    day.load(data, typing=str)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(11)
    day.load(typing=str)
    return day

def test_example(example):
    assert main(example, part=1) == 1656

def test_example_p2(example):
    assert main(example, part=2) == 195

def test_part1(day):
    assert main(day, part=1) == 1613

def test_part2(day):
    assert main(day, part=2) == 510
