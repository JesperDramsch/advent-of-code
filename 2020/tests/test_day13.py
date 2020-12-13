import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day13 import *

@pytest.fixture(scope="function")
def day():
    day = Day(13)
    day.load(typing=str, process=False)
    return day

def test_example(day):
    data = """939
7,13,x,x,59,x,31,19"""
    day.load(data, typing=str, process=False)
    assert main(day, part=1) == 295

def test_example_p2(day):
    data = """939
7,13,x,x,59,x,31,19"""
    day.load(data, typing=str, process=False)
    assert main(day, part=2) == 1068781
    data = """0
17,x,13,19"""
    day.load(data, typing=str, process=False)
    assert main(day, part=2) == 3417
    data = """0
67,7,59,61"""
    day.load(data, typing=str, process=False)
    assert main(day, part=2) == 754018
    data = """0
1789,37,47,1889"""
    day.load(data, typing=str, process=False)
    assert main(day, part=2) == 1202161486

def test_part1(day):
    assert main(day, part=1) == 3269

def test_part2(day):
    assert main(day, part=2) == 672754131923874
