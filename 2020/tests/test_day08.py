import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day08 import *

@pytest.fixture(scope="function")
def day():
    day = Day(8)
    day.load(typing=str)
    return day

def test_example(day):
    data = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
    day.load(data, typing=str)
    assert main(day, part=1) == 5

def test_example_p2(day):
    data = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
    day.load(data, typing=str)
    assert main(day, part=2) == 8

def test_part1(day):
    assert main(day, part=1) == 1753

def test_part2(day):
    assert main(day, part=2) == 733
