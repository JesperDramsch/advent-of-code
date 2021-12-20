import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day20 import *


@pytest.fixture(scope="function")
def example():
    day = Day(20)
    data = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""

    day.load(data, typing=str)
    return day


@pytest.fixture(scope="function")
def day():
    day = Day(20)
    day.load(typing=str)
    return day


def test_example(example):
    assert main(example, part=1) == 35


def test_example_p2(example):
    assert main(example, part=2) == 3351


def test_part1(day):
    assert main(day, part=1) == 5571


# def test_part2(day):
#     assert main(day, part=2) == False
