import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day20 import *


@pytest.fixture(scope="function")
def example():
    day = Day(20)
    data = r"""broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""

    day.load(data)
    return day


@pytest.fixture(scope="function")
def example2():
    day = Day(20)
    data = r"""broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""

    day.load(data)
    return day


@pytest.fixture(scope="function")
def day():
    day = Day(20)
    day.load()
    return day


def test_broadcaster():
    target = ["a", "b", "c"]
    broadcaster = BroadCaster(target)
    assert isinstance(broadcaster, BroadCaster)


def test_flipflop():
    target = ["b"]
    flipflop = FlipFlop(target)
    assert isinstance(flipflop, FlipFlop)
    assert isinstance(flipflop.state, bool)

    assert flipflop.state == False
    assert flipflop(True) == ((None,), None)
    assert flipflop.state == False
    assert flipflop(False) == (("b",), True)
    assert flipflop.state == True
    assert flipflop(True) == ((None,), None)
    assert flipflop.state == True
    assert flipflop(False) == (("b",), False)
    assert flipflop.state == False


def test_conjunction():
    target = ["a"]
    conjunction = Conjunction(target)
    assert isinstance(conjunction, Conjunction)
    assert isinstance(conjunction.state, dict)

    assert conjunction.state == {}
    conjunction("broadcaster", True)
    assert conjunction.state == {"broadcaster": True}


# Part 1
def test_example(example):
    assert main(example, part=1) == 32_000_000


def test_example2(example2):
    assert main(example2, part=1) == 11_687_500


def test_part1(day):
    assert main(day, part=1) == 812609846


# ## Part 2
def test_part2(day):
    assert main(day, part=2) == 245114020323037
