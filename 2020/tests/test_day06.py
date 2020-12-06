import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day06 import *

@pytest.fixture(scope="function")
def day():
    day = Day(6)
    day.load(typing=str, process=False)
    return day

def test_example(day):
    data = """abc

a
b
c

ab
ac

a
a
a
a

b"""
    day.load(data, typing=str, process=False)
    assert main(day, part=1) == 11

def test_example_p2(day):
    data = """abc

a
b
c

ab
ac

a
a
a
a

b"""
    day.load(data, typing=str, process=False)
    assert main(day, part=2) == 6

def test_part1(day):
    assert main(day, part=1) == 6911

def test_part2(day):
    assert main(day, part=2) == 3473
