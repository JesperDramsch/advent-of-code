import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day11 import *

@pytest.fixture(scope="function")
def day():
    day = Day(11)
    day.load(typing=str)
    return day

def test_example(day):
    data = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
    day.load(data, typing=str)
    assert main(day, part=1) == 37

def test_example_p2(day):
    data = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
    day.load(data, typing=str)
    assert main(day, part=2) == 26

def test_part1(day):
    assert main(day, part=1) == 2281

def test_part2(day):
    assert main(day, part=2) == 2085
