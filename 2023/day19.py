from day import Day
from aocd import submit
from utils.parser import Parser
import re


class Inst(list):
    def __init__(self, instruct):
        self._data = instruct
        self._pattern = re.compile(r"([xmas])([<>])(\d+):([a-zAR]+)")
        self._process()

    def _process(self):
        for key, op, val, reg in re.findall(self._pattern, self._data):
            self.append((key, op, int(val), reg))
        self.append(self._data.split(",")[-1][:-1])

    def run(self, part):
        for instruct in self:
            if isinstance(instruct, str):
                return instruct
            key, op, val, reg = instruct

            if key in part:
                if op == "<":
                    if part[key] < int(val):
                        return reg
                elif op == ">":
                    if part[key] > int(val):
                        return reg


class Part(dict):
    def __init__(self, part):
        self.part = part
        self._pattern = re.compile(r"x=(\d+),m=(\d+),a=(\d+),s=(\d+)")
        self._process()

    def _process(self):
        for key, val in zip("xmas", re.findall(self._pattern, self.part)[0]):
            self[key] = int(val)
        self.val = sum(self.values())


class Instructions(dict):
    def __init__(self, instructions):
        self.instructions = instructions
        self.process()

    def process(self):
        for instruct in self.instructions:
            key = instruct.split("{")[0]
            self[key] = Inst(instruct)

    def run(self, part):
        key = "in"
        while True:
            instruct = self[key]
            key = instruct.run(part)
            if key == "R":
                return False
            elif key == "A":
                return part.val


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
        return sum(instruct.run(part) for part in parts)
    if part == 2:
        pass


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
    submit(p1, part="a", day=19, year=2023)

    # day.load()
    # p2 = main(day, part=2)
    # print(p2)
    # submit(p2, part="b", day=19, year=2023)
