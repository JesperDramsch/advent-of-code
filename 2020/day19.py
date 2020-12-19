from util import Day
from aocd import submit
import re


def preprocess(data):
    out = {}
    for row in data:
        x, y = row.split(": ")
        out[int(x)] = y.replace('"', "").strip().split(" | ")
    for k, v in out.items():
        if "a" not in v and "b" not in v:
            inner_list = []
            for a in v:
                inner_list.append(list(map(int, a.strip().split())))
            out[k] = inner_list
    return out


def make_regex(rules, start_num=0, depth=0):
    if depth > 30:
        return ""
    sub_rules = rules[start_num]
    if isinstance(sub_rules[0], str):
        return sub_rules[0]
    else:
        out = []
        for sub_rule in sub_rules:
            out2 = ""
            for val in sub_rule:
                out2 += make_regex(rules, val, depth + 1)
            if out2:
                out.append(out2)
        return "((" + ")|(".join(out) + "))"


def main(day, part=1):
    rules, data = day.data.split("\n\n")
    data = data.strip().split("\n")
    if part == 2:
        rules = rules + "\n8: 42 | 42 8\n11: 42 31 | 42 11 31"
    rules = rules.strip().split("\n")
    rules = preprocess(rules)
    auto_reg = "^" + make_regex(rules) + "$"
    reg = re.compile(auto_reg)
    out = sum([1 for msg in data if reg.match(msg)])
    return out


if __name__ == "__main__":
    day = Day(19)
    day.download()

    day.load(process=False)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=19, year=2020)

    day.load(process=False)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=19, year=2020)
