from day import Day
from aocd import submit
from utils.parser import Parser


class Plots(Parser):
    def __init__(self, data):
        super().__init__(data)
        self._data = data
        self.width = data.index("\n")
        self.height = data.count("\n") + 1
        self.data = set()
        self.start = None
        self.directions = (1, -1, 1j, -1j)
        self.parse()

    def parse(self):
        for i, line in enumerate(self._data.split("\n")):
            for ii, plot in enumerate(line):
                if plot == ".":
                    self.data.add(i + ii * 1j)
                if plot == "S":
                    self.start = i + ii * 1j
                    self.data.add(i + ii * 1j)

    def complex_mod(self, val):
        return val.real % self.height + val.imag % self.width * 1j

    def step(self, current=None):
        if current is None:
            current = (self.start,)

        next = set()
        for c in current:
            for direction in self.directions:
                new = c + direction
                if self.complex_mod(new) in self.data:
                    next.add(new)
        return next

    def run(self, steps=1):
        current = (self.start,)
        for _ in range(steps):
            current = self.step(current)
            if not current:
                break
        return current

    def lagrange_polynomial(self, steps=26501365):
        # 1. find a pattern
        # 2. find a way to exploit it
        # 3. profit

        # This was a huge help in understanding what I'm supposed to do:
        # https://github.com/p3rki3/AoC2023/blob/main/Day21_solution.py
        # Finding factors of the Lagrange Polynomial
        # Thisd vidoe was also helpful:
        # https://www.youtube.com/watch?v=bzp_q7NDdd4

        factors = []
        current = (self.start,)
        # Search for a pattern
        for count in range(1, steps + 1):
            # Move forward one step
            current = self.step(current)

            # At regular steps, outside of the starting square, evaluate the different types of plots
            if count == self.height // 2 + self.height * len(factors):
                factors.append(len(current))

                if len(factors) == 3:
                    delta = (
                        factors[0],
                        factors[1] - factors[0],
                        factors[2] - 2 * factors[1] + factors[0],
                    )
                    lagrange = (
                        delta[0]
                        + delta[1] * (steps // self.height)
                        + delta[2] * ((steps // self.height) * ((steps // self.height) - 1) // 2)
                    )
                    print(self.height, factors, delta, lagrange)
                    return lagrange


def main(day, part=1):
    plots = Plots(day.data)
    print(plots.start)
    if part == 1:
        return len(plots.run(steps=64))
    if part == 2:
        return plots.lagrange_polynomial()


if __name__ == "__main__":
    day = Day(21)
    day.download()

    day.load(process=False)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=21, year=2023)

    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=21, year=2023)
