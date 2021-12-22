import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day22 import *

@pytest.fixture(scope="function")
def example():
    day = Day(22)
    data = """on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11
on x=10..10,y=10..10,z=10..10"""

    day.load(data, typing=str)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(22)
    day.load(typing=str)
    return day

def test_example(example):
    assert main(example, part=1) == 39

def test_example_p2(example):
    assert main(example, part=2) == False

def test_part1(day):
    assert main(day, part=1) == 598616

def test_part2(day):
    assert main(day, part=2) == False
