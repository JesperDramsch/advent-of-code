import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day08 import *

@pytest.fixture(scope="function")
def example():
    day = Day(8)
    data = """30373
25512
65332
33549
35390"""

    day.load(data)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(8)
    day.load()
    return day

def test_example(example):
    assert main(example, part=1) == 21

def test_example_p2(example):
    assert main(example, part=2) == 8

def test_part1(day):
    assert main(day, part=1) == 1684

def test_part2(day):
    assert main(day, part=2) == 486540
