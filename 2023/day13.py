from day import Day
from aocd import submit
from utils.parser import Parser


class Pattern:
    def __init__(self, pattern):
        self.pattern = pattern
        self.width = len(pattern[0])
        self.height = len(pattern)
        self.parse()

    def parse(self):
        self.transpose = [""] * self.width
        for i in range(self.height):
            for j in range(self.width):
                self.transpose[j] += self.pattern[i][j]

    def find_midpoint(self):
        midpoints, modpints = [], []
        for i in range(self.width - 1):
            if self.transpose[i] == self.transpose[i + 1]:
                midpoints.append(i)  # 0-indexed

        for midpoint in midpoints:
            for i, ii in zip(range(midpoint + 1, self.width), range(midpoint, -1, -1)):
                if self.transpose[i] != self.transpose[ii]:
                    break
            else:
                return midpoint + 1

        for i in range(self.height - 1):
            if self.pattern[i] == self.pattern[i + 1]:
                modpints.append(i)  # 0-indexed

        for modpint in modpints:
            for i, ii in zip(range(modpint + 1, self.height), range(modpint, -1, -1)):
                if self.pattern[i] != self.pattern[ii]:
                    break
            else:
                return (modpint + 1) * 100

    def find_midpoint_error(self):
        midpoints, modpints = [], []
        for i in range(self.width - 1):
            if self.transpose[i] == self.transpose[i + 1]:
                midpoints.append(i)  # 0-indexed

        for midpoint in midpoints:
            for i, ii in zip(range(midpoint + 1, self.width), range(midpoint, -1, -1)):
                if self.transpose[i] != self.transpose[ii]:
                    break
            else:
                return midpoint + 1

        for i in range(self.height - 1):
            if self.pattern[i] == self.pattern[i + 1]:
                modpints.append(i)  # 0-indexed

        for modpint in modpints:
            for i, ii in zip(range(modpint + 1, self.height), range(modpint, -1, -1)):
                if self.pattern[i] != self.pattern[ii]:
                    break
            else:
                return (modpint + 1) * 100


def main(day, part=1):
    patterns = Parser(day.data)
    patterns.parse_list_of_lists()
    if part == 1:
        return sum(Pattern(data).find_midpoint() for data in patterns.data)
    if part == 2:
        pass


if __name__ == "__main__":
    day = Day(13)
    day.download()

    day.load(process=False)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=13, year=2023)

    data = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

    day.load(data, process=False)
    p2 = main(day, part=2)
    print(p2)
    # submit(p2, part="b", day=13, year=2023)
