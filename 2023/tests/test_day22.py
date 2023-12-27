import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day22 import *


@pytest.fixture(scope="function")
def example():
    day = Day(22)
    data = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""

    day.load(data)
    return day


@pytest.fixture(scope="function")
def day():
    day = Day(22)
    day.load()
    return day


## Part 1


def test_part1(day):
    assert main(day, part=1) == 480


## Part 2
def test_part2(day):
    assert main(day, part=2) == 84021
