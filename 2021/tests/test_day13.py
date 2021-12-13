import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day13 import *

@pytest.fixture(scope="function")
def example():
    day = Day(13)
    data = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

    day.load(data, typing=str)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(13)
    day.load(typing=str)
    return day

def test_example(example):
    assert main(example, part=1) == 17

def test_example_p2(example):
    assert main(example, part=2) == "BCZRCEAB"

def test_part1(day):
    assert main(day, part=1) == 847

def test_part2(day):
    assert main(day, part=2) == "BCZRCEAB"
