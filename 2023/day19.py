from day import Day
from aocd import submit
from utils.parser import Parser
import re
from collections import defaultdict
from itertools import product
from tqdm import tqdm


class Inst(list):
    def __init__(self, instruct):
        self._data = instruct
        self._pattern = re.compile(r"([xmas])([<>])(\d+):([a-zAR]+)")
        self.used = set()
        self._process()
        self.cache = {}

    def _process(self):
        for key, op, val, reg in re.findall(self._pattern, self._data):
            self.append((key, op, int(val), reg))

        last = self._data.split(",")[-1][:-1]

        while self and last == self[-1][-1]:
            self.pop(-1)
        self.append(last)

        for key, _, _, _ in self[:-1]:
            self.used.add(key)
        self.used = sorted(self.used)

    def run(self, part):
        filter_part = tuple((key, part[key]) for key in self.used)
        if filter_part in self.cache:
            return self.cache[filter_part]
        for instruct in self:
            if isinstance(instruct, str):
                self.cache[filter_part] = instruct
                return instruct
            key, op, val, reg = instruct

            if key in part:
                if op == "<":
                    if part[key] < val:
                        self.cache[filter_part] = reg
                        return reg
                if op == ">":
                    if part[key] > val:
                        self.cache[filter_part] = reg
                        return reg


class Part(dict):
    def __init__(self, part):
        self.part = part
        self._pattern = re.compile(r"x=(\d+),m=(\d+),a=(\d+),s=(\d+)")
        self._process()

    def _process(self):
        for key, val in zip("xmas", re.findall(self._pattern, self.part)[0]):
            self[key] = int(val)

    def val(self):
        return sum(self.values())


class Instructions(dict):
    def __init__(self, instructions):
        self.instructions = instructions
        self.cache = dict()
        self.coche = defaultdict(dict)
        self.process()

    def process(self):
        shortcuts = {}
        new_shortcuts = {"A": "A"}
        while shortcuts != new_shortcuts:
            self.clear()
            shortcuts = new_shortcuts.copy()
            for instruct in sorted(self.instructions, key=len):
                for word, initial in shortcuts.items():
                    instruct = re.sub("([^a-zA-Z])" + word + "([^a-zA-Z])", "\g<1>" + initial + "\g<2>", instruct)
                key = instruct.split("{")[0]
                inst = Inst(instruct)
                if len(inst) == 1:
                    new_shortcuts[key] = inst[0]
                    continue
                self[key] = inst

    def get_splits(self):
        splits = {xmas: [0, 4000] for xmas in "xmas"}
        for instruct in self.values():
            for key, op, val, _ in instruct[:-1]:
                splits[key].append(val - (op == "<"))
        self.splits = {key: sorted(set(val)) for key, val in splits.items()}

    def run_all_ranges(self):
        accepted = 0
        for (x, x_), (m, m_), (a, a_), (s, s_) in tqdm(
            product(
                zip(self.splits["x"][1:], self.splits["x"]),
                zip(self.splits["m"][1:], self.splits["m"]),
                zip(self.splits["a"][1:], self.splits["a"]),
                zip(self.splits["s"][1:], self.splits["s"]),
            ),
            total=(len(self.splits["x"][1:]) - 1) ** 4,
        ):
            if self.run(dict(x=x, m=m, a=a, s=s)):
                accepted += (x - x_) * (m - m_) * (a - a_) * (s - s_)
        return accepted

    def run(self, part):
        key = "in"
        used = set()
        while True:
            instruct = self[key]
            used.update(instruct.used)
            port = tuple((key, part[key]) for key in sorted(used))
            if port in self.cache:
                return self.cache[port]
            pirt = tuple((key, part[key]) for key in instruct.used)
            if pirt in self.coche[key]:
                key = self.coche[key][pirt]
            else:
                self.coche[key][pirt] = key = instruct.run(part)

            if key == "R":
                if len(used) != len(part):
                    self.cache[port] = False
                return False
            if key == "A":
                if len(used) != len(part):
                    self.cache[port] = True
                return True


def parse(data):
    paper = Parser(data)
    paper.parse_list_of_lists()
    instruct, parts = paper.data
    parts = [Part(part) for part in parts]
    instruct = Instructions(instruct)
    return instruct, parts


def main(day, part=1):
    instruct, parts = parse(day.data)
    if part == 1:
        return sum(part.val() for part in parts if instruct.run(part))
    if part == 2:
        instruct.get_splits()
        return instruct.run_all_ranges()


if __name__ == "__main__":
    day = Day(19)
    day.download()

    day.load(process=False)
    #     data = """px{a<2006:qkq,m>2090:A,rfg}
    # pv{a>1716:R,A}
    # lnx{m>1548:A,A}
    # rfg{s<537:gd,x>2440:R,A}
    # qs{s>3448:A,lnx}
    # qkq{x<1416:A,crn}
    # crn{x>2662:A,R}
    # in{s<1351:px,qqz}
    # qqz{s>2770:qs,m<1801:hdj,R}
    # gd{a>3333:R,R}
    # hdj{m>838:A,pv}

    # {x=787,m=2655,a=1222,s=2876}
    # {x=1679,m=44,a=2067,s=496}
    # {x=2036,m=264,a=79,s=2244}
    # {x=2461,m=1339,a=466,s=291}
    # {x=2127,m=1623,a=2188,s=1013}"""

    #     day.load(data, process=False)
    p1 = main(day)
    print(p1)
    # submit(p1, part="a", day=19, year=2023)

    # day.load()
    p2 = main(day, part=2)
    print(p2)
    # submit(p2, part="b", day=19, year=2023)
