from util import Day
from aocd import submit
import re
from itertools import permutations


def find_largets(data):
    max_magnitude = 0
    for a, b in permutations(data, 2):
        data = reduce(add(a, b))
        mag = magnitude(data)
        if mag > max_magnitude:
            max_magnitude = mag
    return max_magnitude


def add_all(all_data):
    data = all_data[0]
    for right in all_data[1:]:
        data = reduce(add(data, right))
    return data


def add(a, b):
    return f"[{a},{b}]"


def reduce(original_data):
    # print("orig:\t", original_data)
    while True:
        # Explode as long as explosion is possible
        data = explode(original_data)
        if data != original_data:
            # print("explode:", data)
            original_data = data
            continue
        # Split once
        data = split(data)
        # print("split:\t", data)
        if original_data == data:
            # If the data is unchanged return the data
            break
        original_data = data
    return data


def explode(data):
    # Find Nested
    depth = 0
    r = None
    # Find nested brackets, no idea how to do this regex only
    for i, char in enumerate(data):
        if char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
        if depth > 4:
            # Find nested pair without a ] before]
            r = re.search("^\]*\[(\d+),(\d+)\]", data[i:])
            if r is not None:
                break
    # If regex doesn't find any return data
    if r is None:
        return data
    # Get the numbers
    a, b = r.groups()

    # Find number on the left and sum
    left_data = data[: i + r.start()]
    left = re.search("(\d+)(?!.*\d)", left_data)
    if left is not None:
        a = int(left.groups()[0]) + int(a)
        left_data = left_data[: left.start()] + str(a) + left_data[left.end() :]
        data = left_data + data[i + r.start() :]
    # Find number on the right and sum
    right_data = data[i + r.end() :]
    right = re.search("(\d+)", right_data)
    if right is not None:
        b = int(right.groups()[0]) + int(b)
        data = data[: i + r.end()] + right_data[: right.start()] + str(b) + right_data[right.end() :]
    # Replace the original snail number with 0
    data = data[:i] + data[i:].replace(r[0], "0", 1)
    return data


def split(original_data):
    # Find number with two digits
    r = re.search("(\d{2})", original_data)
    if r is None:
        return original_data
    n = r.groups()[0]
    num = int(n)
    # Split data and insert instead of double digits 
    left = num // 2
    right = num - left
    original_data = original_data[: r.start()] + "[" + str(left) + "," + str(right) + "]" + original_data[r.end() :]
    return original_data


def magnitude(data):
    while True:
        # Find all snail numbers
        r = re.findall("\[(\d+),(\d+)\]", data)
        # Only magnitude left then return
        if len(r) == 0:
            return int(data)
        # Replace all snail numbers with 3*x+2*y of numbers
        for a, b in r:
            data = data.replace(f"[{a},{b}]", str(int(a) * 3 + int(b) * 2))


def main(day, part=1):
    if part == 1:
        x = add_all(day.data)
        return magnitude(x)
    if part == 2:
        return find_largets(day.data)


if __name__ == "__main__":
    day = Day(18)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=18, year=2021)
    
    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=18, year=2021)
