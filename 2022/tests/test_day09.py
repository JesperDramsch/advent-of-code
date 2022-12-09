import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day09 import *

@pytest.fixture(scope="function")
def example():
    day = Day(9)
    data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

    day.load(data, typing=str)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(9)
    day.load(typing=str)
    return day

def test_example(example):
    assert main(example, part=1) == 13

def test_example_p2(example):
    assert main(example, part=2) == 36

def test_part1(day):
    assert main(day, part=1) == 6339

def test_part2(day):
    assert main(day, part=2) == False
