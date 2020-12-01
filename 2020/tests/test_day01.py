import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day01 import *

@pytest.fixture(scope='session')
def day():
    day = Day(1)
    day.load()
    return day

def test_day01_01(day):
    assert combine(day.data) == 927684

def test_day01_02(day):
    assert combine(day.data, 3) == 292093004