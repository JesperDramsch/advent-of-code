import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day10 import *

@pytest.fixture(scope="function")
def day():
    day = Day(10)
    day.load()
    return day

def test_example(day):
    data = """16
10
15
5
1
11
7
19
6
12
4"""
    day.load(data)
    assert main(day, part=1) == 35

    data = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""
    day.load(data)
    assert main(day, part=1) == 220

def test_example_p2(day):
    
    data = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""
    day.load(data)
    assert main(day, part=2) == 19208

def test_part1(day):
    assert main(day, part=1) == 1917

def test_part2(day):
    assert main(day, part=2) == 113387824750592
