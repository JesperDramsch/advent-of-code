import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day12 import *

@pytest.fixture(scope="function")
def example():
    day = Day(12)
    data = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

    day.load(data)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(12)
    day.load()
    return day

## Part 1
def test_example(example):
    assert main(example, part=1) == 31

def test_part1(day):
    assert main(day, part=1) == 468

## Part 2
def test_example_p2(example):
    assert main(example, part=2) == 29

def test_part2(day):
    assert main(day, part=2) == 459
