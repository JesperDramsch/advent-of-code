import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day18 import *

@pytest.fixture(scope="function")
def example():
    day = Day(18)
    data = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""

    day.load(data)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(18)
    day.load()
    return day

## Part 1
def test_example(example):
    assert main(example, part=1) == 64

def test_part1(day):
    assert main(day, part=1) == 4308

## Part 2
def test_example_p2(example):
    assert main(example, part=2) == 58

def test_part2(day):
    assert main(day, part=2) == 2540
