from day import Day
from aocd import submit


class Parabol(list):
    def __init__(self, raw_data):
        self._data = raw_data
        self.height = len(self._data)
        self.width = len(self._data[0])
        self.cube = list()
        self.round = list()
        self.parse()
        self.cache = dict()
        self.tilt_offset = 0
        self.tilt_length = 0

    def __repr__(self):
        output = ""
        x = self.round.copy()
        for i in range(self.height):
            for ii in range(self.width):
                if i + ii * 1j in self.round:
                    output += "O"
                    x.pop(x.index(i + ii * 1j))
                elif i + ii * 1j in self.cube:
                    output += "#"
                else:
                    output += "."
            output += "\n"
        return output + f"Round: {len(self.round)}\nCube: {len(self.cube)}\n {x}\n"

    def parse(self):
        for i, line in enumerate(self._data):
            for ii, char in enumerate(line):
                if char == "#":
                    self.cube.append(i + ii * 1j)
                if char == "O":
                    self.round.append(i + ii * 1j)

    def tilt(self, direction=-1):
        if direction.imag < 0 or direction.real < 0:
            self.round = sorted(self.round, key=lambda x: x.imag + x.real)
        else:
            self.round = sorted(self.round, key=lambda x: x.imag + x.real, reverse=True)
        self.tilt_offset += 1
        if (tuple(self.round), direction) in self.cache:
            offset, self.round = self.cache[(tuple(self.round), direction)]
            print(f"Bingo! Start: {self.tilt_offset} with end: {offset}")
            return self.tilt_offset - offset
        max_range = min(self.width, self.height)
        for key in self.round:
            for i in range(max_range):
                next_pos = key + direction * (i + 1)
                if (
                    next_pos in self
                    or next_pos in self.cube
                    or next_pos.imag < 0
                    or next_pos.real < 0
                    or next_pos.imag >= self.height
                    or next_pos.real >= self.width
                ):
                    self.append(key + direction * i)
                    break
        self.cache[(tuple(self.round), direction)] = (self.tilt_offset, list(self))
        self.round = list(self)
        self.clear()

    def circle(self, num=1):
        while self.tilt_offset / 4 < num:
            for i in [-1, -1j, 1, 1j]:
                out = self.tilt(i)
                if out:
                    x = num * 4 - self.tilt_offset
                    self.tilt_offset += (x // out) * out
                    self.cache.clear()
            if self.tilt_offset % 100 == 0:
                # I have no patience...
                print(self.tilt_offset)

    def calculate_load(self):
        return sum([self.height - int(val.real) for val in self.round])


def main(day, part=1):
    mirror = Parabol(day.data)
    if part == 1:
        mirror.tilt(-1)
        return mirror.calculate_load()
    if part == 2:
        mirror.circle(1_000_000_000)
        return mirror.calculate_load()


if __name__ == "__main__":
    day = Day(14)
    day.download()

    day.load()
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=14, year=2023)

    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=14, year=2023)
