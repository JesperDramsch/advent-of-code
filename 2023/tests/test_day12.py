import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day12 import *


@pytest.fixture(scope="function")
def example():
    day = Day(12)
    data = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

    day.load(data)
    return day


@pytest.fixture(scope="function")
def day():
    day = Day(12)
    day.load()
    return day


## Part 1
def test_example(example):
    assert main(example, part=1) == 21


def test_part1(day):
    assert main(day, part=1) == 7771


## Part 2
def test_example_p2(example):
    assert main(example, part=2) == 525152


def test_part2(day):
    assert main(day, part=2) == 10861030975833
