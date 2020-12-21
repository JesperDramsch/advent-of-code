import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day21 import *

@pytest.fixture(scope="function")
def example():
    day = Day(21)
    data = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""

    day.load(data, typing=str)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(21)
    day.load(typing=str)
    return day

def test_example(example):
    assert main(example, part=1) == 5

def test_example_p2(example):
    assert main(example, part=2) == "mxmxvkd,sqjhc,fvjkl"

def test_part1(day):
    assert main(day, part=1) == 2324

def test_part2(day):
    assert main(day, part=2) == "bxjvzk,hqgqj,sp,spl,hsksz,qzzzf,fmpgn,tpnnkc"
