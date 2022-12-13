import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day13 import *

@pytest.fixture(scope="function")
def example():
    day = Day(13)
    data = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

    day.load(data)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(13)
    day.load()
    return day

## Part 1
def test_example(example):
    assert main(example, part=1) == 13

def test_part1(day):
    assert main(day, part=1) == 5003

## Part 2
def test_example_p2(example):
    assert main(example, part=2) == 140

def test_part2(day):
    assert main(day, part=2) == 20280
