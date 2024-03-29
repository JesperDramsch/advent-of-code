import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day05 import *

@pytest.fixture(scope="function")
def example():
    day = Day(5)
    data = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

    day.load(data, strip=False)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(5)
    day.load(strip=None)
    return day

def test_example(example):
    assert main(example, part=1) == "CMZ"

def test_example_p2(example):
    assert main(example, part=2) == "MCD"

def test_part1(day):
    assert main(day, part=1) == "HNSNMTLHQ"

def test_part2(day):
    assert main(day, part=2) == "RNLFDJMCT"
