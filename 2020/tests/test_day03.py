import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day03 import *


@pytest.fixture(scope="function")
def day():
    day = Day(3)
    day.load(typing=str)
    return day


def test_example(day):
    data = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
    day.load(data, typing=str)
    assert main(day, part=1) == 7


def test_example_2(day):
    data = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
    day.load(data, typing=str)
    assert main(day, part=2) == 336


def test_part1(day):
    assert main(day, part=1) == 276


def test_part2(day):
    assert main(day, part=2) == 7812180000
