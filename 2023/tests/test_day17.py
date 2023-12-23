import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day17 import *


@pytest.fixture(scope="function")
def example():
    day = Day(17)
    data = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""

    day.load(data)
    return day


@pytest.fixture(scope="function")
def example2():
    day = Day(17)
    data = """111111111111
999999999991
999999999991
999999999991
999999999991"""

    day.load(data)
    return day


@pytest.fixture(scope="function")
def day():
    day = Day(17)
    day.load()
    return day


## Part 1
def test_example(example):
    assert main(example, part=1) == 102


def test_part1(day):
    assert main(day, part=1) == 686


## Part 2
def test_example_p2(example):
    assert main(example, part=2) == 94


def test_example_p2_2(example2):
    assert main(example2, part=2) == 71


def test_part2(day):
    assert main(day, part=2) == 801
