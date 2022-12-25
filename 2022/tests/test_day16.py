import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day16 import *

@pytest.fixture(scope="function")
def example():
    day = Day(16)
    data = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

    day.load(data)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(16)
    day.load()
    return day

## Part 1
def test_example(example):
    assert main(example, part=1) == 1651

# def test_part1(day):
#     assert main(day, part=1) == 1862

## Part 2
def test_example_p2(example):
    assert main(example, part=2) == 1707

# def test_part2(day):
#     assert main(day, part=2) == 2422
