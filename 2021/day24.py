from util import Day
from aocd import submit
from itertools import product
from numba import njit

def process_input(data):
    out = []
    for i, instruction in enumerate(data):
        if (i%18)==15:
            out.append(int(instruction.split()[-1]))
    return out

def test_alu(instructions):
    for model_number in product(range(9, 0, -1), repeat=14):
        if 0 in model_number:
            continue
        z = 0
        for program, n in zip(instructions, model_number):
            z = z * 26 + program + n
        if z == 0:
            return model_number


def main(day, part=1):
    day.data = process_input(day.data)
    if part == 1:
        return test_alu(instructions=day.data)
    if part == 2:
        pass

if __name__ == "__main__":
    day = Day(24)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    # submit(p1, part="a", day=24, year=2021)

    # day.load(typing=str)
    # p2 = main(day, part=2)
    # print(p2)
    # submit(p2, part="b", day=24, year=2021)
