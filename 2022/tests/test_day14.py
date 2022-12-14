import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day14 import *

@pytest.fixture(scope="function")
def example():
    day = Day(14)
    data = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

    day.load(data)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(14)
    day.load()
    return day

## Part 1
def test_example(example):
    assert main(example, part=1) == 24

def test_part1(day):
    assert main(day, part=1) == 638

## Part 2
def test_example_p2(example):
    assert main(example, part=2) == 93

def test_part2(day):
    assert main(day, part=2) == 31722
