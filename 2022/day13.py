from day import Day
from aocd import submit
import ast
from functools import cmp_to_key

def compare(left, right):
    # Match types
    match left, right:
        case int(), int():
            return left - right
        case list(), list():
            for items in zip(left, right):
                out = compare(*items)
                if out:
                    return out 
            return compare(len(left), len(right))
        case int(), list():
            return compare([left], right)
        case list(), int():
            return compare(left, [right])

def distress_signal(data):
    flat = [item for sublist in data for item in sublist]
    distress = [[[2]], [[6]]]
    flat.extend(distress)
    sorted_list = sorted(flat, key=cmp_to_key(compare))
    return [i for i, item in enumerate(sorted_list, 1) if item in distress]

def main(day, part=1):
    day.parse_list_of_lists()
    day.apply(ast.literal_eval)
    if part == 1:
        return sum(i for i, outcome in enumerate(day.data, 1) if compare(*outcome) < 0)
    if part == 2:
        signal = distress_signal(day.data)
        return signal[0] * signal[1]

if __name__ == "__main__":
    day = Day(13)
    day.download()

    day.load()
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=13, year=2022)

    day.load()
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=13, year=2022)
