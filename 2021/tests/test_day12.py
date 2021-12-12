import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day12 import *


@pytest.fixture(scope="function")
def example():
    day = Day(12)
    data = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

    day.load(data, typing=str)
    return day


@pytest.fixture(scope="function")
def medium_example():
    day = Day(12)
    data = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

    day.load(data, typing=str)
    return day


@pytest.fixture(scope="function")
def big_example():
    day = Day(12)
    data = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

    day.load(data, typing=str)
    return day


@pytest.fixture(scope="function")
def day():
    day = Day(12)
    day.load(typing=str)
    return day


def test_example(example):
    assert main(example, part=1) == 10


def test_medium_example(medium_example):
    assert main(medium_example, part=1) == 19


def test_big_example(big_example):
    assert main(big_example, part=1) == 226


def test_example_p2(example):
    assert main(example, part=2) == 36


def test_medium_example_p2(medium_example):
    assert main(medium_example, part=2) == 103


def test_big_example_p2(big_example):
    assert main(big_example, part=2) == 3509


def test_part1(day):
    assert main(day, part=1) == 5333


def test_part2(day):
    assert main(day, part=2) == 146553
