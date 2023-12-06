import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day05 import *


@pytest.fixture(scope="function")
def example():
    day = Day(5)
    data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

    day.load(data, process=False)
    return day


@pytest.fixture(scope="function")
def day():
    day = Day(5)
    day.load(process=False)
    return day


## Part 1
def test_example(example):
    assert main(example, part=1) == 35


def test_part1(day):
    assert main(day, part=1) == 323142486


## Part 2
def test_example_p2(example):
    assert main(example, part=2) == 46


def test_part2(day):
    assert main(day, part=2) == 79874951
