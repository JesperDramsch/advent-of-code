import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day23 import *


@pytest.fixture(scope="function")
def example():
    day = Day(23)
    data = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""

    day.load(data)
    return day


@pytest.fixture(scope="function")
def day():
    day = Day(23)
    day.load()
    return day


## Part 1
def test_example(example):
    assert main(example, part=1) == 94


def test_part1(day):
    assert main(day, part=1) == 2206


## Part 2
def test_example_p2(example):
    assert main(example, part=2) == 154


def test_part2(day):
    assert main(day, part=2) == False
