import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day22 import *

@pytest.fixture(scope="function")
def example():
    day = Day(22)
    data = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""

    day.load(data, process=False)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(22)
    day.load(process=False)
    return day

def test_example(example):
    assert main(example, part=1) == 306

def test_example_p2(example):
    assert main(example, part=2) == 291

def test_example2_p2(example):
    day = Day(22)
    data = """Player 1:
43
19

Player 2:
2
29
14"""

    day.load(data, process=False)
    return day
    assert main(example, part=2) == 105

def test_part1(day):
    assert main(day, part=1) == 33434

def test_part2(day):
    assert main(day, part=2) == 31657
