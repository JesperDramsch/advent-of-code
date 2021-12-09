import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day09 import *

@pytest.fixture(scope="function")
def example():
    day = Day(9)
    data = """2199943210
3987894921
9856789892
8767896789
9899965678"""

    day.load(data, typing=str)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(9)
    day.load(typing=str)
    return day

def test_example(example):
    assert main(example, part=1) == 15

def test_example_p2(example):
    assert main(example, part=2) == 1134

def test_part1(day):
    assert main(day, part=1) == 522

def test_part2(day):
    assert main(day, part=2) == 916688
