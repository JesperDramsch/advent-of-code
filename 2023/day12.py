from day import Day
from aocd import submit

from itertools import product


class Record(list):
    def __init__(self, data, repeat=1):
        record, checksum = data.split(" ")
        self.checksum = list(map(int, checksum.split(","))) * repeat
        self.parse("?".join([record] * repeat))
        self.cache = dict()

    def __hash__(self):
        return hash(tuple(self))

    def __repr__(self):
        return f"{self.checksum} {super().__repr__()}"

    def parse(self, record):
        self.flippable = list()
        for i, val in enumerate(record):
            if val == "#":
                self.append(True)
            elif val == ".":
                self.append(False)
            elif val == "?":
                self.append(None)
                self.flippable.append(i)
            else:
                raise ValueError(f"Unknown value {val}")

    def flippedifloppedi(self):
        num_valid = 0
        for flips in product([True, False], repeat=len(self.flippable)):
            record = self.copy()
            for i, flip in zip(self.flippable, flips):
                record[i] = flip
            num_valid += self.check_valid(tuple(record))
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

    # Recursive solution
    def recursive_flippedifloppedi(self, i_record, i_checksum, current_segment):
        cache_key = (i_record, i_checksum, current_segment)
        if cache_key in self.cache:
            return self.cache[cache_key]
        if i_record == len(self):
            if i_checksum == len(self.checksum) - 1 and self.checksum[i_checksum] == current_segment:
                return 1
            elif i_checksum > len(self.checksum) - 1 and current_segment == 0:
                return 1
            else:
                return 0
        out = 0
        for flip in [True, False]:
            if self[i_record] is None or self[i_record] == flip:
                if flip is True:
                    # Increment current segment
                    out += self.recursive_flippedifloppedi(i_record + 1, i_checksum, current_segment + 1)
                elif flip is False and current_segment == 0:
                    # Just go to next position
                    out += self.recursive_flippedifloppedi(i_record + 1, i_checksum, 0)
                elif (
                    flip is False
                    and current_segment > 0
                    and i_checksum < len(self.checksum)
                    and self.checksum[i_checksum] == current_segment
                ):
                    # End segment
                    out += self.recursive_flippedifloppedi(i_record + 1, i_checksum + 1, 0)
        self.cache[cache_key] = out
        return out


def main(day, part=1):
    if part == 1:
        data = [Record(line) for line in day.data]
        return sum([record.flippedifloppedi() for record in data])
    if part == 2:
        data = [Record(line, 5) for line in day.data]
        return sum([record.recursive_flippedifloppedi(0, 0, 0) for record in data])


if __name__ == "__main__":
    day = Day(12)
    day.download()

    day.load()
    # p1 = main(day)
    # print(p1)
    # submit(p1, part="a", day=12, year=2023)

    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=12, year=2023)
