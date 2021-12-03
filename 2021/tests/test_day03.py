import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day03 import *

@pytest.fixture(scope="function")
def example():
    day = Day(3)
    data = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

    day.load(data, typing=str)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(3)
    day.load(typing=str)
    return day

def test_example(example):
    assert main(example, part=1) == 198

def test_example_p2(example):
    assert main(example, part=2) == 230

def test_part1(day):
    assert main(day, part=1) == 3969000

def test_part2(day):
    assert main(day, part=2) == 4267809
