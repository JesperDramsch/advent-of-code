import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day05 import *

@pytest.fixture(scope="function")
def example():
    day = Day(5)
    data = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

    day.load(data, typing=str)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(5)
    day.load(typing=str)
    return day

def test_example(example):
    assert main(example, part=1) == 5

def test_example_p2(example):
    assert main(example, part=2) == 12

def test_part1(day):
    assert main(day, part=1) == 6189

def test_part2(day):
    assert main(day, part=2) == 19164
