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

    def search_midpoint(self, dim, pattern, tolerance):
        midpoints = []
        for i in range(dim - 1):
            if self.equal_parts(pattern[i], pattern[i + 1]) <= tolerance:
                midpoints.append(i)  # 0-indexed
        return midpoints

    def check_mirror(self, midpoints, dim, pattern, tolerance):
        tmp = tolerance
        for midpoint in midpoints:
            tolerance = tmp
            for i, ii in zip(range(midpoint + 1, dim), range(midpoint, -1, -1)):
                tolerance -= self.equal_parts(pattern[i], pattern[ii])
                if tolerance < 0:
                    break
            else:
                if tolerance == 0:
                    return midpoint + 1

    def find_midpoint(self, tolerance):
        midpoints = self.search_midpoint(self.width, self.transpose, tolerance)
        midpoint = self.check_mirror(midpoints, self.width, self.transpose, tolerance)
        if midpoint is not None:
            return midpoint

        modpints = self.search_midpoint(self.height, self.pattern, tolerance)
        modpint = self.check_mirror(modpints, self.height, self.pattern, tolerance)
        if modpint is not None:
            return modpint * 100

    def equal_parts(self, one, two):
        return len(one) - sum(a == b for a, b in zip(one, two))


def main(day, part=1):
    patterns = Parser(day.data)
    patterns.parse_list_of_lists()
    if part == 1:
        return sum([Pattern(data).find_midpoint(0) for data in patterns.data])
    if part == 2:
        return sum([Pattern(data).find_midpoint(1) for data in patterns.data])


if __name__ == "__main__":
    day = Day(13)
    day.download()

    day.load(process=False)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=13, year=2023)

    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=13, year=2023)
