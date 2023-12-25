import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day19 import *


@pytest.fixture(scope="function")
def example():
    day = Day(19)
    data = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""

    day.load(data, process=False)
    return day


@pytest.fixture(scope="function")
def day():
    day = Day(19)
    day.load(process=False)
    return day


## Part 1
def test_example(example):
    assert main(example, part=1) == 19114


def test_part1(day):
    assert main(day, part=1) == 350678


## Part 2
def test_example_p2(example):
    assert main(example, part=2) == 167409079868000


def test_part2(day):
    assert main(day, part=2) == 124831893423809
