from util import Day
from aocd import submit
from collections import Counter


def parse_input(data):
    template = data[0]
    instructions = dict(line.split(" -> ") for line in data[2:])
    return template, instructions


def process_instructions(steps, template, instructions):

    # Create Counters for pairs and letters
    pairs = Counter([a + b for (a, b) in zip(template, template[1:])])
    letters = Counter(template)

    # Iterate through steps
    for _ in range(steps):
        # Iterate through pair counts (copy to modify pair in loop)
        for pair, count in pairs.copy().items():
            # Check if pair is in instruction
            c = instructions.get(pair)
            if c is not None:
                # Split pair into two letters
                a, b = pair
                # Remove pair from pairs
                pairs[pair] -= count
                # Add the two new pair to pairs
                pairs[a + c] += count
                pairs[c + b] += count
                # Add new letter
                letters[c] += count
    return letters


def main(day, part=1):
    day.data = parse_input(data=day.data)
    if part == 1:
        steps = 10
    if part == 2:
        steps = 40
    count = process_instructions(steps, *day.data).most_common()
    return count[0][1] - count[-1][1]


if __name__ == "__main__":
    day = Day(14)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=14, year=2021)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=14, year=2021)
