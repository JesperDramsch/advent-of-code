import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day07 import *

@pytest.fixture(scope="function")
def example():
    day = Day(7)
    data = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

    day.load(data, typing=str)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(7)
    day.load(typing=str)
    return day

def test_example(example):
    assert main(example, part=1) == 95437

def test_example_p2(example):
    assert main(example, part=2) == 24933642

def test_part1(day):
    assert main(day, part=1) == 1989474

def test_part2(day):
    assert main(day, part=2) == 1111607
