import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day10 import *

@pytest.fixture(scope="function")
def example():
    day = Day(10)
    data = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

    day.load(data)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(10)
    day.load()
    return day

def test_example(example):
    assert main(example, part=1) == 13140

def test_example_p2(example):
    assert main(example, part=2) == """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""

def test_part1(day):
    assert main(day, part=1) == 13680

def test_part2(day):
    assert main(day, part=2) == """###..####..##..###..#..#.###..####.###..
#..#....#.#..#.#..#.#.#..#..#.#....#..#.
#..#...#..#....#..#.##...#..#.###..###..
###...#...#.##.###..#.#..###..#....#..#.
#....#....#..#.#....#.#..#....#....#..#.
#....####..###.#....#..#.#....####.###.."""
