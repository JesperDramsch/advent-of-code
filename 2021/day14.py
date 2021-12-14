from util import Day
from aocd import submit
from collections import Counter

def parse_input(data):
    template = data[0]

    instructions = dict(line.split(" -> ") for line in data[2:])
    return template, instructions

def process_instructions(template, instructions):
    new_template = []
    for i, letter in enumerate(template[:-1]):
        new_template.append(letter)
        instruction = letter+template[i+1]
        if instruction in instructions:
            new_template.append(instructions[instruction])
    new_template.append(template[-1])
    return new_template

def apply_steps(steps, template, instructions):
    for _ in range(steps):
        template = process_instructions(template, instructions)
    return template

def main(day, part=1):
    day.data = parse_input(data=day.data)
    if part == 1:
        steps = 10
    if part == 2:
        steps = 40
    template = apply_steps(steps, *day.data)
    count = Counter(template).most_common()
    return count[0][1] - count[-1][1]

if __name__ == "__main__":
    day = Day(14)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=14, year=2021)

    # day.load(typing=str)
    # p2 = main(day, part=2)
    # print(p2)
    # submit(p2, part="b", day=14, year=2021)
