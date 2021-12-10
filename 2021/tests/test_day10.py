import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day10 import *


@pytest.fixture(scope="function")
def example():
    day = Day(10)
    data = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

    day.load(data, typing=str)
    return day


@pytest.fixture(scope="function")
def day():
    day = Day(10)
    day.load(typing=str)
    return day


def test_example(example):
    assert main(example, part=1) == 26397


def test_example_p2(example):
    assert main(example, part=2) == 288957


def test_part1(day):
    assert main(day, part=1) == 319329


def test_part2(day):
    assert main(day, part=2) == 3515583998
