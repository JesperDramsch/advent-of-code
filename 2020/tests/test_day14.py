import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day14 import *

@pytest.fixture(scope="function")
def day():
    day = Day(14)
    day.load(typing=str)
    return day

def test_example(day):
    data = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""
    day.load(data, typing=str)
    assert main(day, part=1) == 165

def test_example_p2(day):
    data = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""
    day.load(data, typing=str)
    assert main(day, part=2) == 208

def test_part1(day):
    assert main(day, part=1) == 14862056079561

def test_part2(day):
    assert main(day, part=2) == 3296185383161
