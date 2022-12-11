from day import Day
from aocd import submit


def process_instruction(instruction, cycles, X):
    add = 0
    match instruction.split(" "):
        case "noop",:
            inc = 1
        case "addx", add:
            inc = 2
            add = int(add)
    return inc, add


def draw_crt(instructions):
    cycles, X = 0, 1
    crt = []
    for line in instructions:
        inc, add = process_instruction(line, cycles, X)
        for i in range(inc):
            if X - 1 <= cycles % 40 <= X + 1:
                crt.append("#")
            else:
                crt.append(".")
            cycles += 1
        X += add
    return crt


def plot_crt(crt):
    return "\n".join("".join(crt[i : i + 40]) for i in range(0, len(crt), 40))


def check_program(instructions, checks):
    cycles, X = 0, 1
    check = 20
    for line in instructions:
        inc, add = process_instruction(line, cycles, X)
        if cycles < check <= cycles + inc:
            checks[check] = X
            check += 40
        cycles += inc
        X += add
    return checks


def main(day, part=1):
    day.parse_list()
    if part == 1:
        checks = {20 + n * 40: None for n in range(6)}
        checks = check_program(day.data, checks)
        return sum(cycle * X for cycle, X in checks.items())
    if part == 2:
        return plot_crt(draw_crt(day.data))


if __name__ == "__main__":
    day = Day(10)
    day.download()

    day.load()
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=10, year=2022)

    day.load()
    p2 = main(day, part=2)
    print(p2)
    # submit(p2, part="b", day=10, year=2022)
