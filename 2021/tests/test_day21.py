import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day21 import *

@pytest.fixture(scope="function")
def example():
    day = Day(21)
    data = """Player 1 starting position: 4
Player 2 starting position: 8"""

    day.load(data, typing=str)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(21)
    day.load(typing=str)
    return day

def test_example(example):
    assert main(example, part=1) == 739785

def test_example_p2(example):
    assert main(example, part=2) == 444356092776315

def test_part1(day):
    assert main(day, part=1) == 671580

# def test_part2(day):
#     assert main(day, part=2) == False
