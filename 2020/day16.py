from util import Day
from aocd import submit
import re
import numpy as np
from scipy.stats import rankdata


def process_my_ticket(my_ticket):
    return list(map(int, my_ticket.split(":")[1].strip().split(",")))


def process_neighbours(neighbours):
    nums = neighbours.split(":")[1].strip()
    return [list(map(int, x.split(","))) for x in nums.split()]


def process_rules(rules):
    out = {}
    # Kinda like the template matching trick!
    m_str = (
        r"(?P<key>[a-z ]+): (?P<one_lower>[0-9]*)-(?P<one_upper>[0-9]*) or (?P<two_lower>[0-9]*)-(?P<two_upper>[0-9]*)"
    )
    for rule in rules.split("\n"):
        m = re.match(m_str, rule)
        out[m.group("key")] = (
            (int(m.group("one_lower")), int(m.group("one_upper"))),
            (int(m.group("two_lower")), int(m.group("two_upper"))),
        )
    return out


def validate_rule(rule, num):
    et = rule[0]
    to = rule[1]
    return (et[0] <= num <= et[1]) or (to[0] <= num <= to[1])


def validate_v1(rules, neighbours):
    not_ok = []
    for n in neighbours:
        validated = False
        for _, v in rules.items():
            if validate_rule(v, n):
                validated = True
                break
        if not validated:
            not_ok.append(n)
    return not_ok


def search_field(rules, neighbours):
    counter = np.zeros((len(rules), len(neighbours[0])))
    for j, (_, v) in enumerate(rules.items()):
        for neighbour in neighbours:
            for i, n in enumerate(neighbour):
                if validate_rule(v, n):
                    counter[j, i] += 1

    max_counter = counter == np.max(counter, axis=1)
    # This is probably really stupid but it'll sieve
    i = 0
    # Create a prototype all true mask to copy
    mask_prototype = np.ones_like(max_counter).astype(bool)
    while any(np.sum(max_counter, axis=1) > 1):
        row = max_counter[i, :]
        # All true mask
        mask = mask_prototype.copy()
        # If this row has a single Maximum value
        if sum(row) == 1:
            # Set the mask column of the single maximum value to false
            mask = mask * ~row
            # Except for that one value of our row
            mask[i, :] += row
            # mask the max_counter
            max_counter *= mask
        # Wrap around the counter
        i = (i + 1) % max_counter.shape[0]

    # Build a dictionary that has our index values for each rule key
    likely_column = {k: np.argmax(max_counter[i, :]) for i, (k, _) in enumerate(rules.items())}
    return likely_column


def preprocess(data):
    rules, my_ticket, neighbours = data.split("\n\n")
    a = process_my_ticket(my_ticket)
    b = process_neighbours(neighbours)
    c = process_rules(rules)
    return c, a, b


def main(day, part=1):
    rules, my, neighb = preprocess(day.data)
    if part == 1:
        out = 0
        for n in neighb:
            out += sum(validate_v1(rules, n))
    if part == 2:
        # Filter tickets for valids
        valid_neighb = [n for n in neighb if not validate_v1(rules, n)]
        # Get the ticket fields
        fields = search_field(rules, valid_neighb)
        out = 1
        # print once, because it's awesome
        print(fields)
        # go through fields and only take the ones that have departure
        for k, v in fields.items():
            if "departure" in k:
                out *= my[v]
    return out


if __name__ == "__main__":
    day = Day(16)
    day.download()

    day.load(process=False)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=16, year=2020)

    day.load(process=False)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=16, year=2020)
