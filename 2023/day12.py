from day import Day
from aocd import submit

from itertools import product


class Record(dict):
    def __init__(self, data, repeat=1):
        record, checksum = data.split(" ")
        self.checksum = list(map(int, checksum.split(","))) * repeat
        self.parse(record * repeat)

    def parse(self, record):
        self.flippable = set()
        for i, val in enumerate(record):
            if val == "#":
                self[i] = True
            elif val == ".":
                self[i] = False
            elif val == "?":
                self[i] = None
                self.flippable.add(i)
            else:
                raise ValueError(f"Unknown value {val}")

    def flippedifloppedi(self):
        num_valid = 0
        for flips in product([True, False], repeat=len(self.flippable)):
            record = self.copy()
            for i, flip in zip(self.flippable, flips):
                record[i] = flip
            num_valid += self.check_valid(record)
        return num_valid

    def check_valid(self, other):
        checksum = []
        segment_length = 0
        for i in range(len(other)):
            if other[i] is False and segment_length > 0:
                checksum.append(segment_length)
                segment_length = 0
            elif other[i] is True:
                segment_length += 1
        if segment_length > 0:
            checksum.append(segment_length)
        return self.checksum == checksum


def main(day, part=1):
    if part == 1:
        data = [Record(line) for line in day.data]
        return sum([record.flippedifloppedi() for record in data])
    if part == 2:
        data = [Record(line, 5) for line in day.data]
        return sum([record.flippedifloppedi() for record in data])


if __name__ == "__main__":
    day = Day(12)
    day.download()

    day.load()
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=12, year=2023)

    #     data = """???.### 1,1,3
    # .??..??...?##. 1,1,3
    # ?#?#?#?#?#?#?#? 1,3,1,6
    # ????.#...#... 4,1,1
    # ????.######..#####. 1,6,5
    # ?###???????? 3,2,1"""

    #     day.load(data)
    # p2 = main(day, part=2)
    # print(p2)
    # submit(p2, part="b", day=12, year=2023)
