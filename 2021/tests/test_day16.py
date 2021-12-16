import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day16 import *

@pytest.fixture(scope="function")
def example():
    day = Day(16)
    data = """A0016C880162017C3686B18A3D4780"""

    day.load(data, typing=str)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(16)
    day.load(typing=str)
    return day

def test_hex_conversion():
    assert hex_to_bin("D2FE28") == "110100101111111000101000"

def test_literal_packet():
    a, _ = literal_packet("110100101111111000101000")
    assert a == "011111100101"

def test_literal_assemble():
    _, x, _ = decode(hex_to_bin("D2FE28"))
    assert x == 2021

# Only works on part 1
# def test_operational_num_packet():
#     a, b, c = decode(hex_to_bin("EE00D40C823060"))
#     assert a == 6


# Only works on part 1
# def test_operational_total_length():
#     a, b, c = decode(hex_to_bin("38006F45291200"))
#     assert b == 30

def test_example1():
    vals = (
        ("8A004A801A8002F478", 16),
        ("620080001611562C8802118E34", 12),
        ("C0015000016115A2E0802F182340", 23),
        ("A0016C880162017C3686B18A3D4780", 31),
    )
    for data, expected in vals:
        v, _, _ = decode(hex_to_bin(data))
        assert v == expected
    

def test_example(example):
    assert main(example, part=1) == 31

#  finds the sum of 1 and 2, resulting in the value 3.
#  finds the product of 6 and 9, resulting in the value 54.
#  finds the minimum of 7, 8, and 9, resulting in the value 7.
#  finds the maximum of 7, 8, and 9, resulting in the value 9.
#  produces 1, because 5 is less than 15.
#  produces 0, because 5 is not greater than 15.
#  produces 0, because 5 is not equal to 15.
#  produces 1, because 1 + 3 = 2 * 2.
def test_add():
    _, x, _ = decode(hex_to_bin("C200B40A82"))
    assert x == 3

def test_prod():
    _, x, _ = decode(hex_to_bin("04005AC33890"))
    assert x == 54

def test_min():
    _, x, _ = decode(hex_to_bin("880086C3E88112"))
    assert x == 7

def test_max():
    _, x, _ = decode(hex_to_bin("CE00C43D881120"))
    assert x == 9

def test_gt():
    _, x, _ = decode(hex_to_bin("D8005AC2A8F0"))
    assert x == 1

def test_lt():
    _, x, _ = decode(hex_to_bin("F600BC2D8F"))
    assert x == 0

def test_eq():
    _, x, _ = decode(hex_to_bin("9C005AC2F8F0"))
    assert x == 0
    
def test_eq_assemble():
    _, x, _ = decode(hex_to_bin("9C0141080250320F1802104A08"))
    assert x == 1

def test_part1(day):
    assert main(day, part=1) == 936

def test_part2(day):
    assert main(day, part=2) == 6802496672062
