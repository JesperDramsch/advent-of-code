from util import Day
from aocd import submit


def preprocess(row):
    op, val = row.strip().split()
    return op, int(val)


def flipper(instructions):
    for i, instruction in enumerate(instructions):
        fixed = instructions.copy()
        if instruction[0] == "nop":
            fixed[i] = ("jmp", instruction[1])
        elif instruction[0] == "jmp":
            fixed[i] = ("nop", instruction[1])
        else:
            continue
        status, val = intcode(fixed)

        if status == 0:
            return val
    return "Could not fix input."


def intcode(instructions):
    n_instructions = len(instructions)
    pointer = 0
    accumulator = 0
    history = []

    while True:
        if pointer in history:
            return 1, accumulator
        else:
            history.append(pointer)

        op, val = instructions[pointer]

        if op == "nop":
            pointer += 1
        elif op == "acc":
            pointer += 1
            accumulator += val
        elif op == "jmp":
            pointer += val

        if pointer == n_instructions:
            return (0, accumulator)
        pointer = pointer % n_instructions


def main(day, part=1):
    day.apply(preprocess)
    if part == 1:
        out = intcode(day.data)[1]
    if part == 2:
        out = flipper(day.data)
    return out


if __name__ == "__main__":
    day = Day(8)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=8, year=2020)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=8, year=2020)
