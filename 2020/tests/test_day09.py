import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day09 import *

@pytest.fixture(scope="function")
def day():
    day = Day(9)
    day.load()
    return day

def test_example(day):
    data = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""
    day.load(data)
    assert main(day, part=1, preamble=5) == 127

def test_example_p2(day):
    data = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""
    day.load(data)
    assert main(day, part=2, preamble=5) == 62

def test_part1(day):
    assert main(day, part=1) == 1930745883

def test_part2(day):
    assert main(day, part=2) == 268878261
