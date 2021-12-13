from util import Day
from aocd import submit
import matplotlib.pyplot as plt


def parse_input(data):
    points = set()
    instructions = []
    flip_flop = False
    for line in data:
        if line == "":
            flip_flop = True
            continue
        if flip_flop:
            if "x" in line:
                num = int(line.split("=")[1]) + 0j
            if "y" in line:
                num = int(line.split("=")[1]) * 1j
            instructions.append(num)
        else:
            points.add(complex(*map(int, line.split(","))))
    return points, instructions


def fold(sheet, instruction):
    new_sheet = set()
    for point in sheet:
        if point.real >= instruction.real and point.imag >= instruction.imag:
            if instruction.real == 0:
                folded = point.real + instruction - (point.imag * 1j - instruction)
            elif instruction.imag == 0:
                folded = point.imag * 1j + instruction - (point.real - instruction)
            new_sheet.add(folded)
        else:
            new_sheet.add(point)

    return new_sheet


def follow_instructions(sheet, instructions):
    plot_sheet(sheet, 0)
    for i, instruction in enumerate(instructions):
        sheet = fold(sheet, instruction)
        plot_sheet(sheet, i + 1)
    return sheet


def plot_sheet(sheet, name):
    fig, ax = plt.subplots(figsize=(20, 3))
    ax.plot([p.real for p in sheet], [-p.imag for p in sheet], "*", color=(0.96, 0.96, 0.356))
    ax.set_facecolor((0.075, 0.075, 0.17))
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    plt.savefig(f"images/day13_{name}.png", bbox_inches="tight")


def main(day, part=1):
    day.data = parse_input(day.data)
    if part == 1:
        return len(fold(day.data[0], day.data[1][0]))
    if part == 2:
        sheet = follow_instructions(*day.data)
        plot_sheet(sheet, "final")
        return "BCZRCEAB"


if __name__ == "__main__":
    day = Day(13)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=13, year=2021)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=13, year=2021)
